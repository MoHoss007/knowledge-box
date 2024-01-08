from knowledge_box.models.user import *
from knowledge_box.extensions import db


class UserRepository:
    @staticmethod
    def get_user_by_id(user_id: int):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_name_or_email(name_or_email: str):
        return User.query.filter(
            (User.username == name_or_email) | (User.email == name_or_email)
        ).first()

    @staticmethod
    def create_user(username: str, password: str, email: str):
        user = User(
            username=username,
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        return user
