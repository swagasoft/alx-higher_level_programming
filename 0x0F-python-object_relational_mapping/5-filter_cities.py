#!/usr/bin/python3
"""  lists all cities of a state in argument """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    c.close()
    db.close()
