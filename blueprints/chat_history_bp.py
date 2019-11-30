from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.chat_history_model import ChatHistory
from models.models_create_aux import set_welcoming, set_user_anonymous

chat_history_api = Blueprint('chat_history_api', __name__)


@chat_history_api.route('/chat-history', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()

    welcoming_id = set_welcoming(content['welcoming'], created_at)
    user_anonymous_id = set_user_anonymous(content['userAnonymous'], created_at)

    chat_history = ChatHistory(
        message=content['message'],
        welcoming_id=welcoming_id,
        user_anonymous_id=user_anonymous_id,
        created_at=created_at
    )

    try:
        db.session.add(chat_history)
        db.session.commit()

        return "Chat History add. chat_history id={}".format(chat_history.id)
    except Exception as e:
        return str(e)


@chat_history_api.route('/chats-history', methods=['GET'])
def fetch_all():
    try:
        chats_history = ChatHistory.query.all()

        return jsonify([e.serialize() for e in chats_history])
    except Exception as e:
        return str(e)


@chat_history_api.route('/chat-history/<id_>', methods=['GET'])
def fetch(id_):
    try:
        chat_history = ChatHistory.query.filter_by(id=id_).first()

        return jsonify(chat_history.serialize())
    except Exception as e:
        return str(e)