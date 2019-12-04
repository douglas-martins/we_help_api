from app import db


class ChatRoom(db.Model):
    __tablename__ = 'chat_room'

    id = db.Column(db.Integer, primary_key=True)

    welcoming_available_id = db.Column(db.Integer, db.ForeignKey('welcoming_available.id'))
    welcoming_available = db.relationship('WelcomingAvailable', back_populates='chat_room')

    user_anonymous_id = db.Column(db.Integer, db.ForeignKey('user_anonymous.id'))
    user_anonymous = db.relationship('UserAnonymous', back_populates='chat_room')

    chat_history_id = db.Column(db.Integer, db.ForeignKey('chat_history.id'))
    chat_history = db.relationship('ChatHistory', back_populates='chat_room')

    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def __init__(self, welcoming_available_id, user_anonymous_id, chat_history_id, created_at):
        self.welcoming_available_id = welcoming_available_id
        self.user_anonymous_id = user_anonymous_id
        self.chat_history_id = chat_history_id
        self.created_at = created_at

    def patch_model(self, content):
        self.welcoming_available = content['welcomingAvailable'] if content.get('welcomingAvailable') else self.welcoming_available
        self.user_anonymous = content['userAnonymous'] if content.get('userAnonymous') else self.user_anonymous
        self.chat_history = content['chatHistory'] if content.get('chatHistory') else self.chat_history
        self.updated_at = content['updatedAt'] if content.get('updatedAt') else self.created_at
        self.deleted_at = content['deletedAt'] if content.get('deletedAt') else self.deleted_at


    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'welcomingAvailable': self.welcoming_available.serialize(),
            'userAnonymous': self.user_anonymous.serialize(),
            'chatHistory': self.chat_history.serialize(),
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
