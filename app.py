from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config.global_paths import APP_SETTINGS

app = Flask(__name__)

app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from blueprints.contact_bp import contact_api
from blueprints.file_bp import file_api
from blueprints.person_bp import person_api
from blueprints.welcoming_bp import welcoming_api
from blueprints.aid_institution_bp import aid_institution_api
from blueprints.user_anonymous_bp import user_anonymous_api
from blueprints.welcoming_available_bp import welcoming_available_api
from blueprints.chat_history_bp import chat_history_api
from blueprints.chat_history_media_bp import chat_history_media_api
from blueprints.chat_room_bp import chat_room_api

app.register_blueprint(contact_api)
app.register_blueprint(file_api)
app.register_blueprint(person_api)
app.register_blueprint(welcoming_api)
app.register_blueprint(aid_institution_api)
app.register_blueprint(user_anonymous_api)
app.register_blueprint(welcoming_available_api)
app.register_blueprint(chat_history_api)
app.register_blueprint(chat_history_media_api)
app.register_blueprint(chat_room_api)


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
