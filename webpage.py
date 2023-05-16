from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            dbname='exercises',
                            user='postgres',
                            password='472112',
                            port=5432
    )
    return conn

books=[['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5']]

@app.route('/')
def home():
   conn = get_db_connection()
   cur = conn.cursor()
   return render_template('store.html', book = books)

if __name__ == "__main__":
      app.run(debug=True)