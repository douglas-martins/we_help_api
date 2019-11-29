from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.contact_model import Contact
from models.file_model import File
from models.person_model import Person
from models.welcoming_model import Welcoming

welcoming_api = Blueprint('welcoming_api', __name__)


@welcoming_api.route('/welcoming', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()
    person_id = __set_person(content, created_at)

    welcoming = Welcoming(
        person_id=person_id,
        password=content['password'],
        created_at=created_at
    )

    try:
        db.session.add(welcoming)
        db.session.commit()

        return "Welcoming added. welcoming id={}".format(welcoming.id)
    except Exception as e:
        return str(e)


@welcoming_api.route("/welcomings", methods=['GET'])
def fetch_all():
    try:
        welcomings = Welcoming.query.all()

        return jsonify([e.serialize()] for e in welcomings)
    except Exception as e:
        return str(e)


@welcoming_api.route("/welcomings/<id_>", methods=['GET'])
def fetch(id_):
    try:
        welcoming = Welcoming.query.filter_by(id=id_).first()

        return jsonify(welcoming.serialize())
    except Exception as e:
        return str(e)


def __set_person(content, created_at):
    contact_id = __set_contact(content, created_at)
    file_id = __set_file(content, created_at)

    person = Person(
        contact_id=contact_id,
        file_id=file_id,
        name=content['person']['name'],
        created_at=created_at
    )

    try:
        db.session.add(person)
        db.session.commit()

        return person.id
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
