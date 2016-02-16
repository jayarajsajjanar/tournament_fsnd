-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.



--On each execution of the project, the database is dropped and repopulated.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

--Connects to the database "tournament"
\c tournament;

--AUTO increments ID column.
CREATE TABLE players(ID SERIAL PRIMARY KEY NOT NULL, NAME VARCHAR(50), WINS INT, MATCHES INT);

--DEFAULT VALUES for only code testing - Does not add any functionality!!
--\COPY players(NAME,MATCHES,WINS) FROM 'players_data.csv' DELIMITER ',' CSV;

CREATE TABLE matches(ID INT PRIMARY KEY NOT NULL, WINNER INT,LOSER INT);
