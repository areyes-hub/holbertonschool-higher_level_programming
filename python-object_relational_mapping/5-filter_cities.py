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
    count = 0
    for row in query_rows:
        print(row[0], end="")
        count += 1
        if count == len(query_rows):
            break
        print(", ", end="")
    print("")
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
