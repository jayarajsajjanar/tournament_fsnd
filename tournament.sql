-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

--AUTO increments ID column.
CREATE TABLE players(ID SERIAL PRIMARY KEY NOT NULL, NAME VARCHAR(50), WINS INT, MATCHES INT);
--DEFAULT VALUES
--\COPY players(NAME,MATCHES,WINS) FROM 'players_data.csv' DELIMITER ',' CSV;

CREATE TABLE matches(ID INT PRIMARY KEY NOT NULL, WINNER INT,LOSER INT);

--CREATE TABLE standings(ID INT PRIMARY KEY NOT NULL, )