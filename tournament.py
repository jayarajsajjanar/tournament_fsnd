#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import sys

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    #return psycopg2.connect("dbname=tournament")
    try:
        conn = psycopg2.connect("dbname=tournament")
        return conn
    except:
        print "I am unable to connect to the database"

def deleteMatches():
    """Remove all the match records from the database."""
    cur3=conn.cursor()
    query = "DELETE from MATCHES;"
    cur3.execute(query)
    cur3.execute("UPDATE players SET MATCHES = 0,WINS = 0;")
    cur3.execute("commit;") 
    print "\nTable DELETED\n"

def deletePlayers():
    """Remove all the player records from the database."""
    cur3=conn.cursor()
    query = "DELETE from players;"
    cur3.execute(query)
    cur3.execute("commit;") 
    print "\nTable DELETED\n"
    cur3.execute("""SELECT * from players""")
    rows = cur3.fetchall()
    print "\nSELECT * from players:\n"
    #print (rows)
    for row in rows:
        print row
        count=count+1
    

def countPlayers():
    """Returns the number of players currently registered."""
    cur1 = conn.cursor()
    cur1.execute("""SELECT * from players""")
    rows = cur1.fetchall()
    print "\nSELECT * from players:\n"
    #print (rows)
    count=0
    for row in rows:
        print row
        count=count+1
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    print ("registering....\t",name)
    cur2=conn.cursor()
    query = """INSERT INTO players(NAME,MATCHES,WINS) VALUES ( '%s', 0, 0 );""" %name
    cur2.execute(query)
    cur2.execute("commit;") 
    cur2.execute("SELECT * from players;")
    print "\nregistered\n"

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    cur4=conn.cursor()
    query= "SELECT * from players order by WINS desc,MATCHES asc;"
    cur4.execute(query)
    rows = cur4.fetchall()
    return rows
    
    

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    print ("\n reporting match.....",winner,loser)
    cur1 = conn.cursor()
    cur1.execute("""SELECT * from players""")
    rows = cur1.fetchall()
    
    winner_wins_updated,winner_matches_updated,loser_matches_updated = 0, 0, 0
    #print (rows)
    for row in rows:
        if row[0] == winner:
            winner_matches_updated=row[2]+1
            winner_wins_updated = row[3]+1
        if row[0] == loser:
            loser_matches_updated=row[2]+1



    query1="UPDATE players SET MATCHES = %d,WINS = %d where id  = %d;" %(winner_matches_updated,winner_wins_updated,winner)
    query2="UPDATE players SET MATCHES = %d where id  = %d;" %(loser_matches_updated,loser)
        
    cur1.execute(query1)
    cur1.execute(query2)
    cur1.execute("COMMIT;")
    print "\n match reported\n"

    rows1=playerStandings()

    print "Updated Standings:\n"
        #print (rows)
    for row1 in rows1:
        print (row1)

 
 
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


conn = psycopg2.connect("dbname=tournament")


#ret=connect()
#cur=ret.cursor
# registerPlayer('xyz')

# print "Counting...."
# count_players = countPlayers()
# print "\n counted results: %s \n" %count_players



# rows=playerStandings()

# print "\nStandings:\n"
#     #print (rows)
# for row in rows:
#     print (row)

# # reportMatch('Allen','Teddy')

# rows=playerStandings()

# print "\nNEW Standings:\n"
#     #print (rows)
# for row in rows:
#     print (row)

# deletePlayers()
        


"""print "Welcome!! \n Choose an option : \n"
#Welcome_string = 
        #1) DeleteMatches
        #2) Delete
        #3) Count() 
        #4) Register()
        #5) RegisterCountDelete()
        #6) StandingsBeforeMatches()
        #7) ReportMatches()
        #8) Pairings

print Welcome_string
choice = input("")

if choice == 1:
    print "DeleteMatches"
elif choice == 2:
    print "Delete"
elif choice == 3:
    print "Counting"
    count_players = countPlayers(ret)
elif choice == 4:
    print "Registering"
elif choice == 5:
    print "Registering Count deliting"
elif choice == 6:
    print "Standings before matches"
elif choice == 7:
    print "Matches"
elif choice == 8:
    print "Pairings"
else:
    print "Choose again!!"
"""