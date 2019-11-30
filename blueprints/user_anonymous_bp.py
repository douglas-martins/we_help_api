from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.user_anonymous_model import UserAnonymous

user_anonymous_api = Blueprint('user_anonymous_api', __name__)


@user_anonymous_api.route('/user-anonymous', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()

    user_anonymous = UserAnonymous(
        name=content['name'],
        created_at=created_at
    )

    try:
        db.session.add(user_anonymous)
        db.session.commit()

        return "User Anonymous add. user_anonymous id={}".format(user_anonymous.id)
    except Exception as e:
        db.session.rollback()
        return str(e)


@user_anonymous_api.route('/users-anonymous', methods=['GET'])
def fetch_all():
    try:
        users_anonymous = UserAnonymous.query.all()

        return jsonify([e.serialize() for e in users_anonymous])
    except Exception as e:
        return str(e)


@user_anonymous_api.route('/user-anonymous/<id_>', methods=['GET'])
def fetch(id_):
    try:
        user_anonymous = UserAnonymous.query.filter_by(id=id_).first()

        return jsonify(user_anonymous.serialize())
    except Exception as e:
        return str(e)
