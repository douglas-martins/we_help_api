from app import db


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


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.Integer())
    email = db.Column(db.String())
    created_at = db.Column(db.Date())
    updated_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    person = db.relationship("Person", back_populates="contact")

    def __init__(self, telephone, email, created_at):
        self.telephone = telephone
        self.email = email
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'telephone': self.telephone,
            'email': self.email,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at,
        }


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
