import models
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
import utils
from typing import List

router = APIRouter(tags=['Post'],
                   prefix="/post")

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.Post, db: Session = Depends(get_db)):
    #new_post = models.Posts(title=post.title, content=post.content, published=post.published)
    new_post = models.Posts(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.post("/{id}")
def get_post(id: int, db:Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id:{id} was not found')
    return post
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db:Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id)
    if post.first() == None:#if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, post:schemas.Post, db:Session = Depends(get_db)):
    post_query = db.query(models.Posts).filter(models.Posts.id == id)
    if post_query.first() == None:#if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
    print(post)
    post_query.update(post.dict(),synchronize_session=False)
    db.commit()
    
    return {"data":"successfull"}

@router.get("/all", response_model=List[schemas.PostOut])
def get_all_post(db:Session = Depends(get_db)):
    post = db.query(models.Posts).all()
    print(post[0].__dict__)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post not found')
    return post