from flask import request , make_response
from models.comments_models import comments
import json 
import bson.json_util as json_util


def Comment():
    body = json.loads(request.data)
    comment = body['comment']
    blog_ID = body['blog_ID']
    user_ID = body['user_ID']
    
    all_comments = comments(comment = comment , blog_ID=blog_ID , user_ID= user_ID)
    if not all_comments.blog_ID and all_comments.comment:
        return make_response({"message":"comment and blog_ID cannnot be empty"} , 401)
    
    saved_comments = all_comments.save_comment()
    json_Version = json_util.dumps(saved_comments)
    return make_response({"message":'Your comment has been saved succesfully' , 'Comment':json_Version} , 201)


