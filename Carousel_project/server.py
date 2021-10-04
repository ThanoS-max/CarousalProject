from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("users.db")
    q1 = "select * from users"
    rows = conn.execute(q1)
    rows = rows.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/add_entry' , methods=['POST'])
def add_entry():
    email = request.form['email']
    phone = request.form['phone']
    name = request.form['name']
    conn = sqlite3.connect("users.db")
    q2 = "insert into users (email, phone, name) values('{em}','{ph}','{nm}')".format(em=email, ph=phone, nm=name)
    conn.execute(q2)
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)