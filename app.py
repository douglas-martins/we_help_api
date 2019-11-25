from config.global_paths import APP_SETTINGS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from blueprints.contact_bp import contact_api
from blueprints.file_bp import file_api

app.register_blueprint(contact_api)
app.register_blueprint(file_api)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
