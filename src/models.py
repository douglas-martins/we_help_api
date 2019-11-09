from app import db


# class Person(db.Model):
#     __tablename__ = 'person'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     contact = db.relationship('contact', backref='person', lazy=True)
#     file = db.relationship('file', backref='person', lazy=True)
#     created_at = db.Column(db.Date())
#     updated_at = db.Column(db.Date())
#     deleted_at = db.Column(db.Date())
#
#     def __init__(self, name, contact, file, created_at):
#         self.name = name
#         self.contact = contact
#         self.file = file
#         self.created_at = created_at
#
#     def __repr__(self):
#         return '<id {}>'.format(self.id)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'contact': self.contact,
#             'file': self.file,
#             'createdAt': self.created_at,
#             'updatedAt': self.updated_at,
#             'deletedAt': self.deleted_at
#         }


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.Integer())
    email = db.Column(db.String())
    created_at = db.Column(db.Date())
    updated_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

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
