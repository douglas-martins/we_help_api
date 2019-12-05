from app import db
from models.models_create_aux import set_welcoming_id, set_user_anonymous_id


class ChatHistory(db.Model):
    __tablename__ = 'chat_history'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)

    welcoming_id = db.Column(db.Integer, db.ForeignKey('welcoming.id'))
    welcoming = db.relationship('Welcoming', back_populates='chat_history')

    user_anonymous_id = db.Column(db.Integer, db.ForeignKey('user_anonymous.id'))
    user_anonymous = db.relationship('UserAnonymous', back_populates='chat_history')

    chat_history_media = db.relationship('ChatHistoryMedia', back_populates='chat_history')
    chat_room = db.relationship('ChatRoom', back_populates='chat_history')

    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def __init__(self, message, welcoming_id, user_anonymous_id, created_at):
        self.message = message
        self.welcoming_id = welcoming_id
        self.user_anonymous_id = user_anonymous_id
        self.created_at = created_at

    def patch_model(self, content):
        self.message = content['message'] if content.get('message') else self.message

        if content.get('welcoming'):
            set_welcoming_id(content['welcoming'], self.welcoming_id)

        if content.get('userAnonymous'):
            set_user_anonymous_id(content['userAnonymous'], self.user_anonymous_id)

        self.updated_at = content['updatedAt'] if content.get('updatedAt') else self.created_at
        self.deleted_at = content['deletedAt'] if content.get('deletedAt') else self.deleted_at
        # self.welcoming.deleted_at = self.deleted_at
        # self.user_anonymous.deleted_at = self.deleted_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'message': self.message,
            'welcoming': self.welcoming.serialize(),
            'userAnonymous': self.user_anonymous.serialize(),
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
