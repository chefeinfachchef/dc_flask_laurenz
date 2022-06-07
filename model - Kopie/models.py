# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Reise(db.Model):
    __tablename__ = 'reise'

    ReiseId = db.Column(db.Integer, primary_key=True, unique=True)
    Kosten = db.Column(db.Integer)
    Zielort = db.Column(db.Text)
    Land = db.Column(db.Text)
    Dauer = db.Column(db.Time)
    Hotel = db.Column(db.Integer)
    bueroId = db.Column(db.ForeignKey('reiseveranstalter.bueroId'), index=True)

    reiseveranstalter = db.relationship('Reiseveranstalter', primaryjoin='Reise.bueroId == Reiseveranstalter.bueroId', backref='reises')



class Reiseteilnehmer(db.Model):
    __tablename__ = 'reiseteilnehmer'

    ReisendeId = db.Column(db.Integer, primary_key=True, unique=True)
    Vorname = db.Column(db.Text)
    Nachname = db.Column(db.Text)
    Adresse = db.Column(db.String(120))
    Bundesland = db.Column(db.Text)
    Telefonnummer = db.Column(db.Text)



class ReiseteilnehmerReise(db.Model):
    __tablename__ = 'reiseteilnehmer_reise'

    bueroId = db.Column(db.Integer, primary_key=True, unique=True)
    ReisendeId = db.Column(db.ForeignKey('reiseteilnehmer.ReisendeId'), index=True)
    ReiseId = db.Column(db.ForeignKey('reise.ReiseId'), index=True)

    reise = db.relationship('Reise', primaryjoin='ReiseteilnehmerReise.ReiseId == Reise.ReiseId', backref='reiseteilnehmer_reises')
    reiseteilnehmer = db.relationship('Reiseteilnehmer', primaryjoin='ReiseteilnehmerReise.ReisendeId == Reiseteilnehmer.ReisendeId', backref='reiseteilnehmer_reises')



class Reiseveranstalter(db.Model):
    __tablename__ = 'reiseveranstalter'

    bueroId = db.Column(db.Integer, primary_key=True, unique=True)
    bundesland = db.Column(db.String(120))
    description = db.Column(db.Text)
    telefonnummer = db.Column(db.Integer)
    postleitzahl = db.Column(db.Integer)
    Adresse = db.Column(db.String(120))
    Bueroname = db.Column(db.Text)
    Stadt = db.Column(db.Text)
