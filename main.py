import psycopg2

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

    script = "INSERT INTO menu VALUES (%s, %s, %s)"
    insert_injection = ('Unagi_nigiri', 15, 'Unagi with sushi rice')

    cur.execute(script, insert_injection)

    conn.commit()

except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()