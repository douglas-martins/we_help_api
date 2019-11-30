from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.aid_institution_model import AidInstitution
from models.models_create_aux import set_contact, set_file

aid_institution_api = Blueprint('aid_institution_api', __name__)


@aid_institution_api.route('/aid-institution', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()
    contact_id = set_contact(content['contact'], created_at)
    file_id = set_file(content['file'], created_at)

    aid_institution = AidInstitution(
        name=content['name'] if content.get('name') else None,
        url_site=content['urlSite'] if content.get('urlSite') else None,
        contact_id=contact_id,
        file_id=file_id,
        created_at=created_at
    )

    try:
        db.session.add(aid_institution)
        db.session.commit()

        return "Aid Institution add. aid_institution id={}".format(aid_institution.id)
    except Exception as e:
        db.session.rollback()
        return str(e)


@aid_institution_api.route('/aid-institutions', methods=['GET'])
def fetch_all():
    try:
        aid_institutions = AidInstitution.query.all()

        return jsonify([e.serialize() for e in aid_institutions])
    except Exception as e:
        return str(e)


@aid_institution_api.route('/aid-institution/<id_>', methods=['GET'])
def fetch(id_):
    try:
        aid_institution = AidInstitution.query.filter_by(id=id_).first()

        return jsonify(aid_institution.serialize())
    except Exception as e:
        return str(e)
