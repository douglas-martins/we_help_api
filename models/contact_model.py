from app import db


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.Integer())
    email = db.Column(db.String())
    created_at = db.Column(db.Date())
    updated_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    person = db.relationship("Person", back_populates="contact")
    aid_institution = db.relationship("AidInstitution", back_populates="contact")

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
