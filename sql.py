import psycopg2
import pandas as pd

hostname = 'localhost'
database = 'exercises'
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

    # script portion 

    script = "SELECT * FROM menu"

    cur.execute(script)
    output = cur.fetchall()

    df = pd.DataFrame(data = output, columns = ['Item', 'Price', 'Description', 'ID'])
    print(df)

except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()