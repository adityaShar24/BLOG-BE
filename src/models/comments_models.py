from database.mongo import Comments_Collection
from bson.objectid import ObjectId

class Comment:
    def __init__(self , comment , blog_ID , user_ID , parent_comment_ID):
        self.comment = comment
        self.blog_ID = ObjectId(blog_ID)
        self.user_ID = ObjectId(user_ID)
        self.parent_comment_ID = ObjectId(parent_comment_ID) if parent_comment_ID else None 
        
    def save_comment(self):
        commented_id = Comments_Collection.insert_one({'comment': self.comment , 'blog_ID': self.blog_ID , 'user_ID':self.user_ID , 'parent_comment_ID': self.parent_comment_ID , 'reply': self.replies}).inserted_id
        return commented_id
    
    def list_all_parent_comments():
        all_parent_comments = Comments_Collection.find({'blog_Id':blog_ID})
        return all_parent_comments

    def list_all_replies():
        all_replies = Comments_Collection.find({'parent_comment_ID':parent_comment_ID})
        return list_all_replies