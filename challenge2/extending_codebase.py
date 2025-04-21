# This is a file to be used for prompt engineering challenge 2

import logging

class UserService:
    def __init__(self, db):
        self.db = db
        self.logger = logging.getLogger('UserService')

    def create_user(self, name, email):
        user = {'name': name, 'email': email}
        self.logger.info(f"Creating user: {name}")
        self.save_to_db(user)
        return user

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.logger.info(f"Deleting user ID: {user_id}")
            self.remove_from_db(user_id)
            return True
        return False

    def save_to_db(self, user):
        self.db.save(user)

    def get_user(self, user_id):
        return self.db.get(user_id)

    def remove_from_db(self, user_id):
        self.db.delete(user_id)
