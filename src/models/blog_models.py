from database.mongo import Blogs_Collection
from bson.objectid import ObjectId



class blog:
    def __init__(self ,  title, content, author , user_ID):
        self.title = title
        self.content = content
        self.author = author
        self.userID = ObjectId(user_ID)
        
    def save_blog(self):
        blog_id = Blogs_Collection.insert_one({'title':self.title , 'content':self.content , 'author':self.author , 'user_ID':self.userID}).inserted_id
        return blog_id
    
    def get_blogs(self):
        blogs = Blogs_Collection.find()
        blog_list = list(blogs)
        return blog_list