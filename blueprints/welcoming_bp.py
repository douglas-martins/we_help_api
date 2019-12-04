from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.models_create_aux import set_person
from models.welcoming_model import Welcoming

welcoming_api = Blueprint('welcoming_api', __name__)


@welcoming_api.route('/welcoming', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()
    person_id = set_person(content['person'], created_at)

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
        db.session.rollback()
        return str(e)


@welcoming_api.route("/welcoming/<id_>", methods=['PATCH'])
def patch(id_):
    welcoming = Welcoming.query.filter_by(id=id_).first()
    welcoming.patch_model(request.get_json())

    try:
        db.session.add(welcoming)
        db.session.commit()

        return jsonify(welcoming.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)


@welcoming_api.route("/welcomings", methods=['GET'])
def fetch_all():
    try:
        welcomings = Welcoming.query.all()

        return jsonify([e.serialize() for e in welcomings])
    except Exception as e:
        return str(e)


@welcoming_api.route("/welcoming/<id_>", methods=['GET'])
def fetch(id_):
    try:
        welcoming = Welcoming.query.filter_by(id=id_).first()

        return jsonify(welcoming.serialize())
    except Exception as e:
        return str(e)
