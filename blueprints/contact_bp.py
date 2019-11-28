from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.contact_model import Contact

contact_api = Blueprint('contact_api', __name__)


@contact_api.route("/contact", methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()

    contact = Contact(
        telephone=content['telephone'] if content.get('telephone') else None,
        email=content['email'] if content.get('email') else None,
        created_at=created_at
    )

    try:
        db.session.add(contact)
        db.session.commit()

        return "Contact added. contact id={}".format(contact.id)
    except Exception as e:
        return str(e)


@contact_api.route("/contacts", methods=['GET'])
def fetch_all():
    try:
        contacts = Contact.query.all()

        return jsonify([e.serialize() for e in contacts])
    except Exception as e:
        return str(e)


@contact_api.route("/contact/<id_>", methods=['GET'])
def fetch(id_):
    try:
        contact = Contact.query.filter_by(id=id_).first()

        return jsonify(contact.serialize())
    except Exception as e:
        return str(e)
