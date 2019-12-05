from app import db
import models.models_create_aux


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

    def patch_model(self, content):
        self.name = content['name'] if content.get('name') else self.name
        self.url_site = content['urlSite'] if content.get('urlSite') else self.urlSite

        if content.get('contact'):
            set_contact_id(content['contact'], self.contact_id)

        if content.get('file'):
            set_file_id(content['file'], self.file_id)

        self.updated_at = content['updatedAt'] if content.get('updatedAt') else self.created_at
        self.deleted_at = content['deletedAt'] if content.get('deletedAt') else self.deleted_at
        self.contact.deleted_at = self.deleted_at
        self.file.deleted_at = self.deleted_at

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
