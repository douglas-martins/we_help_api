from app import db
import models.models_create_aux


class Welcoming(db.Model):
    __tablename__ = 'welcoming'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', back_populates='welcoming')

    welcoming_available = db.relationship('WelcomingAvailable', back_populates='welcoming')
    chat_history = db.relationship('ChatHistory', back_populates='welcoming')

    created_at = db.Column(db.Date())
    updated_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    def __int__(self, password, person_id, created_at):
        self.password = password
        self.person_id = person_id
        self.created_at = created_at

    def patch_model(self, content):
        self.password = content['password'] if content.get('password') else self.password

        if content.get('person'):
            set_person_id(content['person'], self.person_id)

        self.updated_at = content['updatedAt'] if content.get('updatedAt') else self.created_at
        self.deleted_at = content['deletedAt'] if content.get('deletedAt') else self.deleted_at
        # self.person.deleted_at = self.deleted_at

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
