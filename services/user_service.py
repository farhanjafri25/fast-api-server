from src.db_connection import db

class UserService:
    def __init__(self):
        self.collection = db['users']
