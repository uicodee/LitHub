from fastapi import APIRouter, Query

from app import dto
from app.api import schems

router = APIRouter(prefix="/book")


@router.get(path="/all")
async def get_books() -> list[dto.Book]:
    ...


@router.post(path="/new")
async def new_book(book: schems.Book):
    print(book)


@router.put(path="/edit")
async def edit_book(book: schems.EditBook):
    ...


# /path/params
# query?param=ewjfsd
@router.delete(path="/delete")
async def delete_book(
        book_id: int = Query(alias="bookId", gt=1)
):
    ...
