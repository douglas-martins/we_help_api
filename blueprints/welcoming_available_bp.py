from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.models_create_aux import set_welcoming
from models.welcoming_available_model import WelcomingAvailable

welcoming_available_api = Blueprint('welcoming_available_api', __name__)


@welcoming_available_api.route('/welcoming-available', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()
    on_chat = False

    welcoming_id = set_welcoming(content['welcoming'], created_at)

    welcoming_available = WelcomingAvailable(
        welcoming_id=welcoming_id,
        on_chat=on_chat,
        created_at=created_at
    )

    try:
        db.session.add(welcoming_available)
        db.session.commit()

        return "Welcoming Available. welcoming_available id={}".format(welcoming_available.id)
    except Exception as e:
        return str(e)


@welcoming_available_api.route('/welcomings-availables', methods=['GET'])
def fetch_all():
    try:
        welcomings_availables = WelcomingAvailable.query.all()

        return jsonify([e.serialize() for e in welcomings_availables])
    except Exception as e:
        return str(e)


@welcoming_available_api.route('/welcoming-available/<id_>', methods=['GET'])
def fetch(id_):
    try:
        welcoming_available = WelcomingAvailable.query.filter_by(id=id_).first()

        return jsonify(welcoming_available.serialize())
    except Exception as e:
        return str(e)
