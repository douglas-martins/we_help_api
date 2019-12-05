from datetime import date

from flask import request, jsonify, Blueprint

from app import db
from models.chat_room_model import ChatRoom
from models.models_create_aux import set_user_anonymous, set_chat_history, set_welcoming_available

chat_room_api = Blueprint('chat_room_api', __name__)


@chat_room_api.route('/chat-room', methods=['POST'])
def add():
    content = request.get_json()
    created_at = date.today()
    chat_history = {
        'welcoming': content['welcomingAvailable']['welcoming'],
        'userAnonymous': content['userAnonymous'],
        'message': 'aa'
    }

    welcoming_available_id = set_welcoming_available(content['welcomingAvailable'], created_at)
    user_anonymous_id = set_user_anonymous(content['userAnonymous'], created_at)
    chat_history_id = set_chat_history(chat_history, created_at)

    chat_room = ChatRoom(
        welcoming_available_id=welcoming_available_id,
        user_anonymous_id=user_anonymous_id,
        chat_history_id=chat_history_id,
        created_at=created_at
    )

    try:
        db.session.add(chat_room)
        db.session.commit()

        # return 'Chat Room add. chat_room id={}'.format(chat_room.id)
        return jsonify(chat_room.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)


@chat_room_api.route("/chat-room/<id_>", methods=['PATCH'])
def patch(id_):
    chat_room = ChatRoom.query.filter_by(id=id_).first()
    chat_room.patch_model(request.get_json())

    try:
        db.session.add(chat_room)
        db.session.commit()

        return jsonify(chat_room.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)


@chat_room_api.route('/chats-rooms', methods=['GET'])
def fetch_all():
    try:
        chats_rooms = ChatRoom.query.filter(ChatRoom.deleted_at.is_(None))

        return jsonify([e.serialize() for e in chats_rooms])
    except Exception as e:
        db.session.rollback()
        return str(e)


@chat_room_api.route('/chat-room/<id_>', methods=['GET'])
def fetch(id_):
    try:
        chat_room = ChatRoom.query.filter_by(id=id_).first()

        return jsonify(chat_room.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)


@chat_room_api.route('/chat-room/<id_>', methods=['DELETE'])
def delete(id_):
    chat_room = ChatRoom.query.filter_by(id=id_).first()
    content = {
        'deletedAt': date.today()
    }
    chat_room.patch_model(content)

    try:
        # db.session.delete(chat_room)
        db.session.add(chat_room)
        db.session.commit()

        return jsonify(chat_room.serialize())
    except Exception as e:
        db.session.rollback()
        return str(e)
