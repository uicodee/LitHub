import shutil
import uuid

from fastapi import APIRouter, Query, Depends, Path, HTTPException, status, UploadFile

from app import dto
from app.api import schems
from app.api.dependencies import dao_provider
from app.infrastructure.database.dao import HolderDao

router = APIRouter(prefix="/book")


@router.get(path="/all")
async def get_books(
        dao: HolderDao = Depends(dao_provider)
) -> list[dto.Book]:
    return await dao.book.get_books()


@router.get(path="/{book_id}")
async def get_book(
        book_id: int = Path(),
        dao: HolderDao = Depends(dao_provider)
) -> dto.Book:
    book = await dao.book.get_book(book_id=book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book not found"
        )
    return book


@router.post(path="/new")
async def new_book(
        book: schems.Book,
        dao: HolderDao = Depends(dao_provider)
) -> dto.Book:
    return await dao.book.add_book(book=book)


@router.post(path="/upload-book")
async def upload_book(
        file: UploadFile,
        dao: HolderDao = Depends(dao_provider)
):
    file_parts = file.filename.split(".")
    file_path = "app/api/media/" + uuid.uuid4().hex + "." + file_parts[-1]
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        return await dao.file.add_file(path=file_path)


@router.put(path="/edit")
async def edit_book(
        book: schems.EditBook,
        dao: HolderDao = Depends(dao_provider)
) -> dto.Book:
    return await dao.book.edit_book(book=book)


# /path/params
# query?param=ewjfsd
@router.delete(path="/delete")
async def delete_book(
        book_id: int = Query(alias="bookId", gt=0),
        dao: HolderDao = Depends(dao_provider)
):
    await dao.book.delete_book(book_id=book_id)
