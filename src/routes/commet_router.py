from flask import Blueprint
from controllers.comments_controller import comment , reply
from flask_jwt import jwt_required

com_bp = Blueprint('com_bp' , __name__)

@com_bp.post("/comment")
@jwt_required()
def comment_wrapper():
    return comment()

@com_bp.post('/reply_comment')
def reply_comment_wrapper():
    return reply()