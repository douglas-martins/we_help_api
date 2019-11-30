from app import db
from models.chat_history_model import ChatHistory
from models.contact_model import Contact
from models.file_model import File
from models.person_model import Person
from models.user_anonymous_model import UserAnonymous
from models.welcoming_available_model import WelcomingAvailable
from models.welcoming_model import Welcoming


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
