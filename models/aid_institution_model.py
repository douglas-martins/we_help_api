from app import db


class AidInstitution(db.Model):
    __tablename__ = 'aid_institution'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url_site = db.Column(db.String)

    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship('Contact', back_populates='aid_institution')

    file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    file = db.relationship('File', back_populates='aid_institution')

    created_at = db.Column(db.Date())
    updated_at = db.Column(db.Date())
    deleted_at = db.Column(db.Date())

    def __int__(self, name, url_site, contact_id, file_id, created_at):
        self.name = name
        self.url_site = url_site
        self.contact_id = contact_id
        self.file_id = file_id
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'urlSite': self.url_site,
            'contact': self.contact.serialize(),
            'file': self.file.serialize(),
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
