from src.app import db


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship("Contact", back_populates="person")

    file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    file = db.relationship("File", back_populates="person")

    created_at = db.Column(db.Date())
    updated_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    def __init__(self, name, contact, file, created_at):
        self.name = name
        self.contact = contact
        self.file = file
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact': self.contact,
            'file': self.file,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
