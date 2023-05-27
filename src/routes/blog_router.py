from controllers.blog_controller import Blog
from flask import Blueprint

blog_bp = Blueprint('blog' , __name__)

@blog_bp.post('/blog')
def Blog_wrapper():
    return Blog()

