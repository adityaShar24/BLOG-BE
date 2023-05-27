from database.mongo import Users_Collection

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        
        
    def save_user(self):
        user_id = Users_Collection.insert_one({'username':self.username , 'password':self.password}).inserted_id
        return user_id
    
    def del_user(self):
        result = Users_Collection.delete_one({'username':self.username , 'password':self.password})
        return result
    
    def find_by_username(username):
        user_data = Users_Collection.find_one({'username': username})
        return user_data
    