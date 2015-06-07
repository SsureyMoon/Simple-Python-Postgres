-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament

CREATE TABLE players (
    id serial PRIMARY KEY,
    name text
);

CREATE TABLE matches (
    id serial PRIMARY KEY,
    player1 int REFERENCES players,
    player2 int REFERENCES players,
    winner int REFERENCES players
);

-- Finding the number of matches each player has played.
CREATE VIEW matches_per_player AS
  select P.id, P.name, count(M.id) as num
  from players as P left join matches as M
  on P.id = M.player1 or P.id = M.player2
  group by P.id
  order by num DESC;

-- Finding the number of wins for each player.
CREATE VIEW wins_each_player AS
  select P.id, P.name, count(M.id) as num
  from players as P left join matches as M
  on P.id = M.winner
  group by P.id
  order by num DESC;

-- Finding the player standings.
CREATE VIEW player_standing AS
  select M.id, M.name, W.num as wins, M.num as matches
  from matches_per_player as M left join wins_each_player as W
  on M.id = W.id
  order by wins DESC;