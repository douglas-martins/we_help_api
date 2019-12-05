from app import db
from models.models_create_aux import set_chat_history_id, set_file_id


class ChatHistoryMedia(db.Model):
    __tablename__ = 'chat_history_media'

    id = db.Column(db.Integer, primary_key=True)

    chat_history_id = db.Column(db.Integer, db.ForeignKey('chat_history.id'))
    chat_history = db.relationship('ChatHistory', back_populates='chat_history_media')

    file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    file = db.relationship('File', back_populates='chat_history_media')

    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def __init__(self, chat_history_id, file_id, created_at):
        self.chat_history_id = chat_history_id,
        self.file_id = file_id,
        self.created_at = created_at

    def patch_model(self, content):
        if content.get('chatHistory'):
            set_chat_history_id(content['contact'], self.chat_history_id)

        if content.get('file'):
            set_file_id(content['file'], self.file_id)

        self.updated_at = content['updatedAt'] if content.get('updatedAt') else self.created_at
        self.deleted_at = content['deletedAt'] if content.get('deletedAt') else self.deleted_at
        # self.file.deleted_at = self.deleted_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'chatHistory': self.chat_history.serialize(),
            'file': self.file.serialize(),
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
