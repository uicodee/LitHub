from fastapi import APIRouter, Depends, Path, Query

from app.api import schems
from app.api.dependencies import dao_provider
from app.infrastructure.database.dao import HolderDao

router = APIRouter(prefix="/author")


@router.get(path="/all")
async def get_authors(
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.author.get_authors()


@router.get(path="/{author_id}")
async def get_author(
        author_id: int = Path(),
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.author.get_author(author_id=author_id)


@router.post(path="/new")
async def new_author(
        author: schems.Author,
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.author.add_author(author=author)


@router.put(path="/edit")
async def edit_author(
        author: schems.EditAuthor,
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.author.edit_author(author=author)


@router.delete(path="/delete")
async def delete_author(
        author_id: int = Query(alias="authorId"),
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.author.delete_author(author_id=author_id)

