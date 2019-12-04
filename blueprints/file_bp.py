from flask import request, Blueprint, jsonify
from datetime import date

from jsonpatch import JsonPatch

from app import db
from models.file_model import File

file_api = Blueprint('file_api', __name__)


@file_api.route("/file", methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()

    file = File(
        url=content['url'],
        created_at=created_at
    )

    try:
        db.session.add(file)
        db.session.commit()

        # return "File added. file id={}".format(file.id)
        return jsonify(file.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)


@file_api.route("/file/<id_>", methods=['PATCH'])
def patch(id_):
    file = File.query.filter_by(id=id_).first()
    file.patch_model(request.get_json())

    try:
        db.session.add(file)
        db.session.commit()

        return jsonify(file.serialize())
    except Exception as e:
        db.session.rollback()
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


@file_api.route('/file/<id_>', methods=['DELETE'])
def delete(id_):
    file = File.query.filter_by(id=id_).first()

    try:
        db.session.delete(file)
        db.session.commit()

        return jsonify(file.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)
