from flask import Blueprint
from controllers.user_controller import Register , Login

auth_bp = Blueprint('auth' , __name__)

@auth_bp.post('/register')
def Register_wrapper():
    return Register()
    
@auth_bp.post('/login')
def Login_wrapper():
    return Login()