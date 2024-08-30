from typing import Annotated

from fastapi import APIRouter

from app.api.posts.schema import PostBase


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("")
def get_posts():
    return {"posts": []}


@router.get("/{id}")
def get_post():
    return {"post": {}}


@router.post("")
def create_posts(payload: PostBase):
    return payload


@router.put("/{id}")
def update_post(id: int, payload: PostBase):
    return payload


@router.delete("/{id}")
def delete_post(id: int):
    return {"id": id}
