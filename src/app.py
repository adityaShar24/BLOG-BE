from flask import Flask
from routes.auth_router import auth_bp
from routes.blog_router import blog_bp
from routes.commet_router import com_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"

app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(com_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug= True)