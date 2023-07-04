from flask import Blueprint
from flask_jwt import jwt_required
from controllers.user_controller import Register , Login , getAllUsers



auth_bp = Blueprint('auth' , __name__)

@auth_bp.post('/register')
def Register_wrapper():
    return Register()
    
@auth_bp.post('/login')
def Login_wrapper():
    return Login()

@auth_bp.get('/AllUsers')
@jwt_required()
def getAllUsers_wrapper():
    return getAllUsers()

