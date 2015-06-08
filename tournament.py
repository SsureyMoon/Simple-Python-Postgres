#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """
    Connect to the PostgreSQL database.
    Returns a database connection and a cursor object.
    """
    try:
        db = psycopg2.connect("dbname=tournament")
        cursor = db.cursor()
        return db, cursor
    except:
        print "database(tournament) connection error"


def deleteMatches():
    """Remove all the match records from the database."""
    query = "truncate matches;"
    db, cursor = connect()
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    query = "truncate players CASCADE;"
    db, cursor = connect()
    cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    query = "select count(*) from players"
    db, cursor = connect()
    cursor.execute(query)
    count = cursor.fetchall()
    db.commit()
    db.close()
    return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    query = "insert into players (name) values (%s)"
    name = bleach.clean(name, strip=True)
    db, cursor = connect()
    cursor.execute(query, (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = "select * from player_standing;"
    db, cursor = connect()
    cursor.execute(query)
    result = cursor.fetchall()
    db.commit()
    db.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = """insert into matches (player1, player2, winner)
               values (%s, %s, %s)"""
    winner = bleach.clean(winner, strip=True)
    loser = bleach.clean(loser, strip=True)
    db, cursor = connect()
    cursor.execute(query, (winner, loser, winner,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    query = "select * from player_standing;"
    db, cursor = connect()
    cursor.execute(query)
    standings = cursor.fetchall()
    output_list = []
    while len(standings) > 0:
        player1 = standings.pop(0)
        player2 = standings.pop(0)
        tup = (player1[0], player1[1], player2[0], player2[1])
        output_list.append(tup)
    cursor.close()
    return output_list
