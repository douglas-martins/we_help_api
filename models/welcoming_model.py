from app import db


class Welcoming(db.Model):
    __tablename__ = 'welcoming'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)

    person_id = db.Column(db.Integer, db.ForeignKey('person_id'))
    person = db.relationship('Person', back_populates='welcoming')

    created_at = db.Column(db.Date())
    updated_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    def __int__(self, password, person_id, created_at):
        self.password = password
        self.person_id = person_id
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'person': self.person.serialize(),
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
