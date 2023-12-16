from fastapi import APIRouter, Depends, Path, Query

from app.api import schems
from app.api.dependencies import dao_provider
from app.infrastructure.database.dao import HolderDao

router = APIRouter(prefix="/genre")


@router.get(path="/all")
async def get_genres(
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.genre.get_genres()


@router.get(path="/{genre_id}")
async def get_genre(
        genre_id: int = Path(),
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.genre.get_genre(genre_id=genre_id)


@router.post(path="/new")
async def new_genre(
        genre: schems.Genre,
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.genre.add_genre(genre=genre)


@router.put(path="/edit")
async def edit_genre(
        genre: schems.EditGenre,
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.genre.edit_genre(genre=genre)


@router.delete(path="/delete")
async def delete_genre(
        genre_id: int = Query(alias="genreId"),
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.genre.delete_genre(genre_id=genre_id)
