from flask import request , make_response
from models.user_model import User
import json
import bson.json_util as json_util
import bcrypt
import jwt
import datetime



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
    
    hash = bcrypt.hashpw( users.password.encode('utf-8') , bcrypt.gensalt())
    
    check_hashedpw = bcrypt.checkpw(users.password.encode('utf-8') , hash)
    
    json_serialize = (json_util.dumps(str(existing_user)))
    
    if check_hashedpw == True:
        token = jwt.encode({"_id": json_serialize , "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15) } , "secret_key")
        return make_response({'token':token},200)
    
    if check_hashedpw == False:
        return make_response({'message':"Could not verify"} , 400)
        
    
    