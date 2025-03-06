#!/usr/bin/python3
"""
This module lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """
    main function that runs the module
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        charset="utf8"
        )
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
