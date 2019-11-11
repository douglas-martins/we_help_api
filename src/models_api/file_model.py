from src.app import db


class File(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    created_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    person = db.relationship("Person", back_populates="file")

    def __init__(self, url, created_at):
        self.url = url
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'created_at': self.created_at,
            'deleted_at': self.deleted_at
        }
