from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.person_model import Person
from models.contact_model import Contact
from models.file_model import File

person_api = Blueprint('person_api', __name__)


@person_api.route("/person", methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()
    contact_id = __set_contact(content, created_at)
    file_id = __set_file(content, created_at)

    person = Person(
        contact_id=contact_id,
        file_id=file_id,
        name=content['name'] if content.get('name') else None,
        created_at=created_at
    )

    try:
        db.session.add(person)
        db.session.commit()

        return "Person added. person id={}".format(person.id)
    except Exception as e:
        return str(e)


@person_api.route("/persons", methods=['GET'])
def fetch_all():
    try:
        persons = Person.query.all()

        return jsonify([e.serialize() for e in persons])
    except Exception as e:
        return str(e)


@person_api.route("/persons/<id_>", methods=['GET'])
def fetch(id_):
    try:
        person = Person.query.filter_by(id=id_).first()

        return jsonify(person.serialize())
    except Exception as e:
        return str(e)


def __set_contact(content, created_at):
    contact = Contact(
        telephone=content['contact']['telephone'],
        email=content['contact']['email'],
        created_at=created_at
    )

    try:
        db.session.add(contact)
        db.session.commit()

        return contact.id
    except Exception as e:
        return str(e)


def __set_file(content, created_at):
    file = File(
        url=content['file']['url'],
        created_at=created_at
    )

    try:
        db.session.add(file)
        db.session.commit()

        return file.id
    except Exception as e:
        return str(e)
