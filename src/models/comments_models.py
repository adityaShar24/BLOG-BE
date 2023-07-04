from database.mongo import Comments_Collection
from bson.objectid import ObjectId

class Comment:
    def __init__(self , comment , blog_ID , user_ID , parent_comment_ID):
        self.comment = comment
        self.blog_ID = ObjectId(blog_ID)
        self.user_ID = ObjectId(user_ID)
        self.parent_comment_ID = ObjectId(parent_comment_ID) if parent_comment_ID else None 
        self.reply = []
        
    def save_comment(self):
        commented_id = Comments_Collection.insert_one({'comment': self.comment , 'blog_ID': self.blog_ID , 'user_ID':self.user_ID , 'parent_comment_ID': self.parent_comment_ID , 'reply': self.reply}).inserted_id
        return commented_id

    def reply_comment(self, reply):
        reply_data = {
            'comment': reply,
            'user_id': self.user_ID
        }
        self.replies.append(reply_data)
