from flask import Blueprint
from controllers.comments_controller import Comment

com_bp = Blueprint('com_bp' , __name__)

@com_bp.post("/comment")
def comment_wrapper():
    return Comment()