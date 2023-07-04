from flask import request , make_response
from models.comments_models import Comment
import json 
import bson.json_util as json_util


def comment():
    body = json.loads(request.data)
    comment = body['comment']
    blog_ID = body['blog_ID']
    user_ID = body['user_ID']    
    all_comments = Comment(comment = comment , blog_ID=blog_ID , user_ID= user_ID)
    if not all_comments.blog_ID and all_comments.comment:
        return make_response({"message":"comment and blog_ID cannnot be empty"} , 401)
    
    saved_comments = all_comments.save_comment()
    json_Version = json_util.dumps(saved_comments)
    return make_response({"message":'Your comment has been saved succesfully' , 'Comment':json_Version} , 201)

def reply():
    body = json.loads(request.data)
    comment = body['comment']
    blog_ID = body['blog_ID']
    user_ID = body['user_ID']    
    parent_comment_ID = body['parent_comment_ID']
    replies = body['replies']
    Comments = Comment(comment = comment , user_ID = user_ID , blog_ID = blog_ID , parent_comment_ID = parent_comment_ID)
    if not comment and blog_ID and user_ID:
        return make_response({"message": "comment, blog_ID and user_ID cannot be empty"} , 401)
    
    reply_comment = Comments.save_comment()
    print(reply_comment)
    return make_response({'message':'Your reply has been saved successfully' , 'reply': reply_comment} , 201)
