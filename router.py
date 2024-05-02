from fastapi.routing import APIRouter
from db import get_db
from sqlalchemy.orm import Session
from model import Blog
from schema import BlogIn
from sqlalchemy import update
from datetime import datetime
from fastapi import HTTPException

blog_router = APIRouter(prefix='/blogs')

@blog_router.get('')
def get_all_blogs():
    db: Session = get_db('blog')
    
    blogs = db.query(Blog) \
        .filter(Blog.deleted_at == None) \
        .order_by(Blog.created_at.desc()) \
        .all()
    
    return blogs

@blog_router.get('/{blog_id}')
def get_single_blog(blog_id: int):
    db: Session = get_db('blog')
    
    blog = db.query(Blog) \
        .filter(Blog.id == blog_id) \
        .first()
    
    return blog

@blog_router.post('')
def create_blog(body: BlogIn):
    db = get_db("blogs")
    
    now = datetime.now()
    
    blog = Blog(
                title = body.title,
                description = body.description,
                created_by = body.created_by,
                created_at = now,
                updated_at = now
            )
    db.add(blog)
    db.commit()
    db.flush()
    db.refresh(blog)
    
    return f"Create a blog with id: {blog.id}"

@blog_router.patch('/{blog_id}')
def modify_blog(blog_id: int, body: BlogIn):
    db = get_db("blogs")
    now = datetime.now()
    blog = db.query(Blog).get(blog_id)
    
    blog.updated_at = now
    blog.title = body.title
    blog.description = body.description
    blog.created_by = body.created_by

    db.commit()
    db.flush()
    db.refresh(blog)
    
    return blog

@blog_router.delete('/{blog_id}')
def delete_blog(blog_id: int):
    db = get_db("blogs")
    
    now = datetime.now()

    blog = db.query(Blog).get(blog_id)

    if blog.deleted_at is not None:
        raise HTTPException(400, "Already deleted")
    
    blog.deleted_at = now
    db.commit()
    
    return f"Delete blog with id: {blog_id}"

@blog_router.patch('/restore/{blog_id}')
def restore_blog(blog_id: int):
    db = get_db("blogs")
    
    now = datetime.now()

    blog = db.query(Blog).get(blog_id)

    if blog.deleted_at is None:
        raise HTTPException(400, "Already restored")
    
    blog.deleted_at = None
    db.commit()
    
    return f"Restored blog with id: {blog_id}"
