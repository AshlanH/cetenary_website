import psycopg2
import pandas as pd

hostname = 'localhost'
database = 'cetenary_project'
username = 'postgres'
pwd = '472112'
port_id = 5432
conn, cur = None, None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor()

    script = "SELECT * FROM vinyl"

    cur.execute(script)
    output = cur.fetchall()
    for a in output:
        print(a)

except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()
