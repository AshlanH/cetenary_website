from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            dbname='cetenary_project',
                            user='postgres',
                            password='472112',
                            port=5432
    )
    return conn

temp=[['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5'],
       ['Input1', 'Input2', 'Input3', 'Input4', 'Input5']]

@app.route('/')
def home():
   return render_template('base.html')

@app.route('/store', methods=['POST', 'GET'])
def store():
    if request.method == 'POST':
        if request.form.get('submit_button') == '1':
            return redirect(url_for('buffer', buffer_input = request.form.get('submit_button')))
        elif request.form.get('submit_button') == '2':
            return redirect(url_for('buffer', buffer_input = request.form.get('submit_button')))
        else:   
            return render_template('base.html')
    elif request.method == 'GET':
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM vinyl")
        return render_template('store.html', menu = cur.fetchall())

@app.route('/buffer/<buffer_input>')
def buffer(buffer_input):
    return f"<h1>Passde value: {buffer_input} </h1>"


if __name__ == "__main__":
      app.run(debug=True)