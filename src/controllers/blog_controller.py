from flask import request , make_response
from models.blog_models import blog
import json
import bson.json_util as json_util



def Blog():
    body = json.loads(request.data)
    title = body['title']
    author = body['author']
    content = body['content']
    user_ID = body['user_ID']
    
    blogs = blog(title = title , author=author , content= content , user_ID= user_ID)
    
    if not blogs.title and blogs.content:
        return make_response ({"message":"auhtor and content cannot be empty"} , 401)
    
    saved_blog = blogs.save_blog()
    json_version = json_util.dumps(saved_blog)
    
    return make_response({'message':"Your blog has been posted successfully" , "blog": json_version} , 201)

    
        