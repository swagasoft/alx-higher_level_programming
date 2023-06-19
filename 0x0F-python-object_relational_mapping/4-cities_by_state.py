#!/usr/bin/python3
"""  lists all citie cities from database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
