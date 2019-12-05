from app import db
import models.models_create_aux


class WelcomingAvailable(db.Model):
    __tablename__ = 'welcoming_available'

    id = db.Column(db.Integer, primary_key=True)
    on_chat = db.Column(db.Boolean)

    welcoming_id = db.Column(db.Integer, db.ForeignKey('welcoming.id'))
    welcoming = db.relationship('Welcoming', back_populates='welcoming_available')

    chat_room = db.relationship('ChatRoom', back_populates='welcoming_available')

    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def __init__(self, welcoming_id, on_chat, created_at):
        self.welcoming_id = welcoming_id
        self.on_chat = on_chat
        self.created_at = created_at

    def patch_model(self, content):
        self.on_chat = content['onChat'] if content.get('onChat') else self.on_chat

        if content.get('welcoming'):
            models.models_create_aux.set_welcoming_id(content['welcoming'], self.welcoming_id)

        self.updated_at = content['updatedAt'] if content.get('updatedAt') else self.created_at
        self.deleted_at = content['deletedAt'] if content.get('deletedAt') else self.deleted_at
        # self.welcoming.deleted_at = self.deleted_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'welcoming': self.welcoming.serialize(),
            'onChat': self.on_chat,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
