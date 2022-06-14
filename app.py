from flask import Flask, render_template

from controllers.index import index_blueprint
from controllers.reise import reise_blueprint
from controllers.reiseteilnehmer import reiseteilnehmer_blueprint
from controllers.reiseveranstalter import reiseveranstalter_blueprint
from model.models import db

from flask_wtf.csrf import CSRFProtect

import sqlalchemy

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Reise"

csrf = CSRFProtect(app)

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(index_blueprint)
app.register_blueprint(reise_blueprint)
app.register_blueprint(reiseteilnehmer_blueprint)
app.register_blueprint(reiseveranstalter_blueprint)

app.run(debug=True)
