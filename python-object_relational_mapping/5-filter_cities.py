#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """
    main function that runs the module
    """
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py mysql_username mysql_password mysql_database state_name")
        return
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        charset="utf8"
        )
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                FROM cities\
                LEFT JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))
    query_rows = cur.fetchall()
    if query_rows:
        print(", ".join([row[0] for row in query_rows]))
    else:
        print("")
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
