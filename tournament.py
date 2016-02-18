#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
    
import psycopg2
import sys

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        conn = psycopg2.connect("dbname=tournament")
        return conn
    except:
        print "		I am unable to connect to the database"

def deleteMatches():
    """Remove all the match records from the database."""
    cur3=conn.cursor()
    query = "DELETE from MATCHES;"
    cur3.execute(query)
    #When the "Matches" table is deleted, the "players" table is modified accordingly.
    cur3.execute("UPDATE players SET MATCHES = 0,WINS = 0;")
    cur3.execute("commit;") 
    print "\t\t\tMatches Table DELETED\n"

def deletePlayers():
    """Remove all the player records from the database."""
    cur3=conn.cursor()
    query = "DELETE from players;"
    cur3.execute(query)
    cur3.execute("commit;") 
    print "\n"
    print "\t\t\tPlayers Table DELETED\n"
    cur3.execute("""SELECT * from players""")
    rows = cur3.fetchall()
    print "\t\t\tSELECT * from players after deleting all players:\n\n\n"
    #print (rows)
    for row in rows:
        print "               ",row
        count=count+1
    

def countPlayers():
    """Returns the number of players currently registered."""
    cur1 = conn.cursor()
    cur1.execute("""SELECT * from players""")
    rows = cur1.fetchall()
    print "\t\t\tCount players; SELECT * from players:\n"
    #print (rows)
    count=0
    for row in rows:
        print "\t\t\t",row
        count=count+1
    print "\t\t\tCount:",count
    print "\n"
    return count
    


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    print "\n"
    print "\t\t\tRegistering....\t",name
    cur2=conn.cursor()

    #Below are 2 different failed attempts at passing variables to sqlcommand.
    #attempt1 =====>
    #query = """INSERT INTO players(NAME,MATCHES,WINS) VALUES ( '%s', 0, 0 );""" %name
    #cur2.execute(query)
    #attempt2 =====>
    #cur2.execute("""INSERT INTO players (NAME,MATCHES,WINS) VALUES (%(str)s, 0, 0);""") %name

    #New player is registered into the table using "name" parameter. "matches" and "wins" in "players" table is set to "0" by default.
    SQL = "INSERT INTO players(NAME,MATCHES,WINS) VALUES ( %s, 0, 0 );" # Note: no quotes
    data = (name, )
    cur2.execute(SQL, data) # Note: no % operator
    cur2.execute("commit;") 
    cur2.execute("\t\t\tSELECT * from players;")
    
    print "\t\t\tRegistered!!\n"

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
    print "\n"
    print "\t\t\tReporting match.....","winner:",winner,"\tloser:",loser

    cur1 = conn.cursor()
    cur1.execute("""SELECT * from players""")
    rows = cur1.fetchall()
    
    winner_wins_updated,winner_matches_updated,loser_matches_updated = 0, 0, 0
    
    #Update the win counts and match counts for the winner.
    #And update only match counts for the loser.
    for row in rows:
        if row[0] == winner:
            winner_matches_updated=row[2]+1
            winner_wins_updated = row[3]+1
        if row[0] == loser:
            loser_matches_updated=row[2]+1


    #Updating the "players" and "matches" tables based on the latest match reported.
    query1="UPDATE players SET MATCHES = %d,WINS = %d where id  = %d;" %(winner_matches_updated,winner_wins_updated,winner)
    query2="UPDATE players SET MATCHES = %d where id  = %d;" %(loser_matches_updated,loser)
        
    cur1.execute(query1)
    cur1.execute(query2)
    cur1.execute("COMMIT;")

    print "\n"
    print "\t\t\tMatch reported\n"

    rows1=playerStandings()

    print "\t\t\tUpdated Standings after reporting match:\n"
        #print (rows)
    for row1 in rows1:
        print "\t\t\t",row1
    print "\n"

 
 
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
        eg : [(1,john,2,billy), (3,peter,4,will) , .....]
    """
    #LOGIC used in pairing :
    #   Latest standings are extracted using "players" table. 
    #   From the standings, 2 players sets/tuples are chosen wherein the players have similar "wins".(Adjacent)
    #   
    cur4=conn.cursor()
    query= "SELECT * from players order by WINS desc,MATCHES asc;"
    cur4.execute(query)
    rows = cur4.fetchall()
    
    #Below are the temporary variables used in processing.
    count=1
    temp_pid = ()
    temp_name = ()
    pid = ()
    name = ()

    #For executing the test cases successfully, the returned datastructure should be a list of tuples.
    outer_list = []
    inner_tuple = ()

    #Instantiating and returning the datastructure.
    for row in rows:
        pid = (row[0],)
        name=(row[1],)
        if count in {1,3,5,7}:
            temp_pid = pid
            temp_name = name
        else:
            inner_tuple = temp_pid+temp_name+pid+name
            outer_list.append(inner_tuple)
        count=count+1
    return outer_list

#In each function, a cursor is attached to the connection and then the respective queries are executed.
conn = psycopg2.connect("dbname=tournament")


