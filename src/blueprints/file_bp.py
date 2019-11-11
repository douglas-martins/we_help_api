from flask import request, Blueprint, jsonify
from datetime import date
from src.app import db
from src.models_api.file_model import File

file_api = Blueprint('file_api', __name__)


@file_api.route("/file", methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()

    try:
        file = File(
            url=content['url'],
            created_at=created_at
        )

        db.session.add(file)
        db.session.commit()

        return "File added. file id={}".format(file.id)
    except Exception as e:
        return str(e)


@file_api.route("/files", methods=['GET'])
def fetch_all():
    try:
        contacts = File.query.all()

        return jsonify([e.serialize() for e in contacts])
    except Exception as e:
        return str(e)


@file_api.route("/file/<id_>", methods=['GET'])
def fetch(id_):
    try:
        file = File.query.filter_by(id=id_).first()

        return jsonify(file.serialize())
    except Exception as e:
        return str(e)
