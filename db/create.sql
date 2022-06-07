CREATE DATABASE IF NOT EXISTS Reise;
USE Reise;

CREATE TABLE IF NOT EXISTS Reiseveranstalter (
	bueroId INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
	bundesland VARCHAR(120),
	description TEXT,
	telefonnummer INT,
	postleitzahl INT,
    Adresse VARCHAR(120),
    Bueroname TEXT,
    Stadt TEXT);


CREATE TABLE IF NOT EXISTS Reise (
	ReiseId INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    Kosten FLOAT,
    Zielort TEXT,
    Land TEXT,
    Dauer TIME,
    Hotel TEXT,
    bueroId INT,
    FOREIGN KEY (bueroId) REFERENCES Reiseveranstalter (bueroId));
 

CREATE TABLE IF NOT EXISTS Reiseteilnehmer (
	ReisendeId INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    Vorname TEXT,
    Nachname TEXT,
    Adresse VARCHAR(120),
    Bundesland TEXT,
    Telefonnummer TEXT);
    
CREATE TABLE IF NOT EXISTS Reiseteilnehmer_Reise (
	bueroId INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    ReisendeId INT,
    ReiseId INT,
    FOREIGN KEY (ReisendeId) REFERENCES Reiseteilnehmer(ReisendeId),
    FOREIGN KEY (ReiseId) REFERENCES Reise(ReiseId));

