from flask import Flask, render_template, redirect, url_for, request
from db import get_db

app = Flask(__name__)

# show all rolloffs
@app.route('/')
def index():
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM assets')
            rolloffs = cursor.fetchall()
    finally:
        conn.close()
    return render_template('home.html', rolloffs=rolloffs)

# show a single rolloff
@app.route('/rolloff/<int:id>', methods=["GET"])
def get_single_rolloff(id):
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM assets WHERE id=%s'
            cursor.execute(sql, (id))
            rolloff = cursor.fetchone()
    finally:
        conn.close()
    return render_template('rolloff.html', rolloff=rolloff)

# update a rolloff
@app.route('/update', methods=["POST"])
def update_rolloff():
    status = 1 if request.form['status'] == "rented" else 0
    location = request.form["location"]
    id = request.form["id"]

    conn = get_db()
    try:
        with conn.cursor() as cursor:
            sql = 'UPDATE assets SET status=%s, location=%s WHERE id=%s'
            cursor.execute(sql, (status, location, id))
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index'))


# create a rolloff
@app.route('/create')
def create_rolloff():
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO assets (status) VALUE (0)')
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index'))


# delete a rolloff
@app.route('/delete/<int:id>')
def delete_rolloff(id):
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            sql = 'DELETE FROM assets WHERE id=%s'
            cursor.execute(sql, (id))
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index'))