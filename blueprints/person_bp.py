from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.person_model import Person

person_api = Blueprint('person_api', __name__)


# @contact_api.route("/person", methods=['POST'])
# def add():
#     content = request.get_json()
#     created_at = date.today()
#
#     try:
#         person = Person(
#             telephone=content['telephone'],
#             email=content['email'],
#             created_at=created_at
#         )
#
#         db.session.add(person)
#         db.session.commit()
#
#         return "Person added. person id={}".format(person.id)
#     except Exception as e:
#         return str(e)


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
