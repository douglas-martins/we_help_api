from app import db


class File(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    created_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    person = db.relationship("Person", back_populates="file")
    aid_institution = db.relationship("AidInstitution", back_populates="file")
    chat_history_media = db.relationship('ChatHistoryMedia', back_populates='file')

    def __init__(self, url, created_at):
        self.url = url
        self.created_at = created_at

    def patch_model(self, content):
        self.url = content['url'] if content.get('url') else self.url
        self.deleted_at = content['deletedAt'] if content.get('deletedAt') else self.deleted_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'createdAt': self.created_at,
            'deletedAt': self.deleted_at
        }
