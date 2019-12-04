from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.models_create_aux import set_contact, set_file
from models.person_model import Person

person_api = Blueprint('person_api', __name__)


@person_api.route("/person", methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()
    contact_id = set_contact(content['contact'], created_at)
    file_id = set_file(content['file'], created_at)

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
        db.session.rollback()
        return str(e)


@person_api.route("/person/<id_>", methods=['PATCH'])
def patch(id_):
    person = Person.query.filter_by(id=id_).first()
    person.patch_model(request.get_json())

    try:
        db.session.add(person)
        db.session.commit()

        return jsonify(person.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)


@person_api.route("/persons", methods=['GET'])
def fetch_all():
    try:
        persons = Person.query.all()

        return jsonify([e.serialize() for e in persons])
    except Exception as e:
        return str(e)


@person_api.route("/person/<id_>", methods=['GET'])
def fetch(id_):
    try:
        person = Person.query.filter_by(id=id_).first()

        return jsonify(person.serialize())
    except Exception as e:
        return str(e)
