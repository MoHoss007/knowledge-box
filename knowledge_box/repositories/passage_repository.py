from knowledge_box.models.passage import *
from knowledge_box.models.user import User
from knowledge_box.extensions import db


class PassageRepository:

    @staticmethod
    def create_passage(topic: str, title: str, text: str, user: User):
        passage = Passage(
            topic=topic,
            title=title,
            text=text,
            user=user
        )

        db.session.add(passage)
        db.session.commit()
        return passage

    @staticmethod
    def get_all_passages():
        return Passage.query.all()

    @staticmethod
    def get_passage_by_title(title: str):
        return Passage.query.filter_by(title=title).first()
