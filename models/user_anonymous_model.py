from app import db


class UserAnonymous(db.Model):
    __tablename__ = 'user_anonymous'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    chat_history = db.relationship('ChatHistory', back_populates='user_anonymous')
    chat_room = db.relationship('ChatRoom', back_populates='user_anonymous')

    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def __init__(self, name, created_at):
        self.name = name
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
