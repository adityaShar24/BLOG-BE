from flask import request , make_response
from models.user_model import User
import json
import bson.json_util as json_util
from flask_jwt_extended import create_access_token , get_jwt_identity 
from app import app



def Register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    users = User(username = username , password = password)
    
    if not (users.password and users.username):
        return make_response({"message":"Username and password cannot be empty"} , 400)
    
    registered_user = User.find_by_username(username)
    
    if registered_user:
        return make_response(f"username {username} already exits please enter unique username" , 401)
    
    saved_user = users.save_user()
    json_version = json_util.dumps(saved_user)
    
    return make_response({"message": "User has been registered successfully", "user": json_version}, 201)


def Login():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    users = User(username=username, password=password)
    
    existing_user = User.find_by_username(username) #users.password.encode('utf-8')
    
    if not existing_user:
        return make_response({"message":"No user found"} , 401)
    access_token = create_access_token(identity= username)
    return make_response({"access_token": access_token} , 201)
        
def getAllUsers():
    users = User.get_Users()
    json_Version = json_util.dumps(users)
    return make_response(json_Version , 201)