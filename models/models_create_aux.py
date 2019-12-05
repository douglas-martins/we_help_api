from app import db
import abc
import models.chat_history_model
import models.chat_history_media_model
import models.chat_room_model
import models.contact_model
import models.file_model
import models.person_model
import models.user_anonymous_model
import models.welcoming_available_model
import models.welcoming_model
from datetime import date


@abc.abstractmethod
def set_welcoming_available(content, created_at):
    welcoming_id = set_welcoming(content['welcoming'], created_at)

    welcoming_available = WelcomingAvailable(
        welcoming_id=welcoming_id,
        on_chat=content['onChat'],
        created_at=created_at
    )

    try:
        db.session.add(welcoming_available)
        db.session.commit()

        return welcoming_available.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_welcoming_available_id(content, id):
    welcoming_available = WelcomingAvailable.query.filter_by(id=id).first()
    set_welcoming_id(content['welcoming'], welcoming_available.welcoming_id)
    welcoming_available.updated_at = date.today()
    welcoming_available.patch_model(content)

    try:
        db.session.add(welcoming_available)
        db.session.commit()

        return welcoming_available.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_chat_room(content, created_at):
    welcoming_available_id = set_welcoming_available(content['welcomingAvailable'], created_at)
    user_anonymous_id = set_user_anonymous(content['userAnonymous'], created_at)
    chat_history_id = set_chat_history(content['chatHistory'], created_at)

    chat_room = ChatRoom(
        welcoming_available_id=welcoming_available_id,
        user_anonymous_id=user_anonymous_id,
        chat_history_id=chat_history_id,
        created_at=created_at
    )

    try:
        db.session.add(chat_room)
        db.session.commit()

        return chat_room.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_chat_room_id(content, id):
    chat_room = ChatRoom.query.filter_by(id=id).first()
    set_welcoming_available_id(content['welcomingAvailable'], chat_room.welcoming_available_id)
    set_chat_history_id(content['chatHistory'], chat_room.chat_history_id)
    set_file_id(content['file'], chat_room.file_id)
    chat_room.updated_at = date.today()
    chat_room.patch_model(content)

    try:
        db.session.add(chat_room)
        db.session.commit()

        return chat_room.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_chat_history_media(content, created_at):
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

        return chat_history_media.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_chat_history_media_id(content, id):
    chat_history_media = ChatHistoryMedia.query.filter_by(id=id).first()
    set_chat_history_id(content['chatHistory'], chat_history_media.chat_history_id)
    set_file_id(content['file'], chat_history_media.file_id)
    chat_history_media.updated_at = date.today()
    chat_history_media.patch_model(content)

    try:
        db.session.add(chat_history_media)
        db.session.commit()

        return chat_history_media.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_chat_history(content, created_at):
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

        return chat_history.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_chat_history_id(content, id):
    chat_history = ChatHistory.query.filter_by(id=id).first()
    set_welcoming_id(content['welcoming'], chat_history.welcoming_id)
    set_user_anonymous_id(content['userAnonymous'], chat_history.user_anonymous_id)
    chat_history.updated_at = date.today()
    chat_history.patch_model(content)

    try:
        db.session.add(chat_history)
        db.session.commit()

        return chat_history.id
    except Exception as e:
        return str(e)


@abc.abstractmethod
def set_user_anonymous(content, created_at):
    user_anonymous = UserAnonymous(
        name=content['name'],
        created_at=created_at
    )

    try:
        db.session.add(user_anonymous)
        db.session.commit()

        return user_anonymous.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_user_anonymous_id(content, id):
    user_anonymous = UserAnonymous.query.filter_by(id=id).first()
    user_anonymous.updated_at = date.today()
    user_anonymous.path_model(content)

    try:
        db.session.add(user_anonymous)
        db.session.commit()

        return user_anonymous.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_welcoming(content, created_at):
    person_id = set_person(content['person'], created_at)

    welcoming = Welcoming(
        password=content['password'],
        person_id=person_id,
        created_at=created_at
    )

    try:
        db.session.add(welcoming)
        db.session.commit()

        return welcoming.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_welcoming_id(content, id):
    welcoming = File.query.filter_by(id=id).first()
    set_person_id(content['person'], welcoming.person_id)
    welcoming.updated_at = date.today()
    welcoming.patch_model(content)

    try:
        db.session.add(welcoming)
        db.session.commit()

        return welcoming.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_person(content, created_at):
    contact_id = set_contact(content['contact'], created_at)
    file_id = set_file(content['file'], created_at)

    person = Person(
        contact_id=contact_id,
        file_id=file_id,
        name=content['name'],
        created_at=created_at
    )

    try:
        db.session.add(person)
        db.session.commit()

        return person.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_person_id(content, id):
    person = Person.query.filter_by(id=id).first()
    set_contact_id(content['contact'], person.contact_id)
    set_file_id(content['file'], person.file_id)
    # contact = Contact.query.filter_by(id=person.contact_id).first()
    # file = File.query.filter_by(id=person.file_id).first()

    person.updated_at = date.today()
    # contact.updated_at = date.today()
    # file.updated_at = date.today()

    person.patch_model(content)
    # contact.patch_model(content)
    # file.patch_model(content)

    try:
        db.session.add(person)
        # db.session.add(contact)
        # db.session.add(file)
        db.session.commit()

        return person.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_contact(content, created_at):
    contact = Contact(
        telephone=content['telephone'] if content.get('telephone') else None,
        email=content['email'] if content.get('email') else None,
        created_at=created_at
    )

    try:
        db.session.add(contact)
        db.session.commit()

        return contact.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_contact_id(content, id):
    contact = Contact.query.filter_by(id=id).first()
    contact.updated_at = date.today()
    contact.patch_model(content)

    try:
        db.session.add(contact)
        db.session.commit()

        return contact.id
    except Exception as e:
        db.session.rollback()
        return str(e)


def set_file(content, created_at):
    file = File(
        url=content['url'],
        created_at=created_at
    )

    try:
        db.session.add(file)
        db.session.commit()

        return file.id
    except Exception as e:
        db.session.rollback()
        return str(e)


@abc.abstractmethod
def set_file_id(content, id):
    file = File.query.filter_by(id=id).first()
    file.updated_at = date.today()
    file.patch_model(content)

    try:
        db.session.add(file)
        db.session.commit()

        return file.id
    except Exception as e:
        db.session.rollback()
        return str(e)
