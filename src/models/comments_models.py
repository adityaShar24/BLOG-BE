from database.mongo import Comments_Colection
from bson.objectid import ObjectId

class comments:
    def __init__(self , comment , blog_ID , user_ID):
        self.comment = comment,
        self.blog_ID = ObjectId(blog_ID)
        self.user_ID = ObjectId(user_ID)
        
    def save_comment(self):
        commented_id = Comments_Colection.insert_one({'comment': self.comment , 'blog_ID': self.blog_ID , 'user_ID':self.user_ID }).inserted_id
        return commented_id