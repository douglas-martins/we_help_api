from app import db


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
