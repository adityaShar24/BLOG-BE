from controllers.blog_controller import Blog , GetAllBLogs
from flask_jwt import jwt_required
from flask import Blueprint

blog_bp = Blueprint('blog' , __name__)

@blog_bp.post('/blog')
@jwt_required()
def Blog_wrapper():
    return Blog()

@blog_bp.get('/allBlogs')
@jwt_required()
def GetAllBLogs_wrapper():
    return GetAllBLogs