from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.chat_history_media_model import ChatHistoryMedia
from models.models_create_aux import set_chat_history
from models.models_create_aux import set_file

chat_history_media_api = Blueprint('chat_history_media_api', __name__)


@chat_history_media_api.route('/chat-history-media', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()

    chat_history_id = set_chat_history(content['chatHistory'], created_at)
    file_id = set_file(content['file'], created_at)

    chat_history_media = ChatHistoryMedia(
        chat_history_id=chat_history_id,
        file_id=file_id,
        created_at=created_at
    )

    try:
        db.session.add(chat_history_media)
        db.session.commit()

        return "Chat History Media add. chat_history_media id={}".format(chat_history_media.id)
    except Exception as e:
        return str(e)


@chat_history_media_api.route('/chats-history-medias', methods=['GET'])
def fetch_all():
    try:
        chats_history_medias = ChatHistoryMedia.query.all()

        return jsonify([e.serialize() for e in chats_history_medias])
    except Exception as e:
        return str(e)


@chat_history_media_api.route('/chat-history-media/<id_>', methods=['GET'])
def fetch(id_):
    try:
        chat_history_media = ChatHistoryMedia.query.filter_by(id=id_).first()

        return jsonify(chat_history_media.serialize())
    except Exception as e:
        return str(e)
