from global_paths import APP_SETTINGS
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Contact


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/add-contact")
def add_contact():
    telephone = request.args.get('telephone')
    email = request.args.get('email')
    created_at = date.today()

    try:
        contact = Contact(
            telephone=telephone,
            email=email,
            created_at=created_at
        )

        db.session.add(contact)
        db.session.commit()

        return "Contact added. contact id={}".format(contact.id)
    except Exception as e:
        return str(e)


@app.route("/get-all-contacts")
def get_all_contacts():
    try:
        contacts = Contact.query.all()

        return jsonify([e.serialize() for e in contacts])
    except Exception as e:
        return str(e)


@app.route("/get-contact/<id_>")
def get_contact(id_):
    try:
        contact = Contact.query.filter_by(id=id_).first()

        return jsonify(contact.serialize())
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
