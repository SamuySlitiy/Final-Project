'''from flask import Flask, render_template, request, flash, redirect
import sqlite3
import hashlib

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/registry', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['Username']
        email = request.form['Email']
        password = request.form['Password']
        print(username, email, password)
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ? OR username = ?', (username, email))
        if c.fetchone():
            return render_template('signup_page_usernameOrEmailFail.html')
        c.execute('SELECT * FROM users WHERE password = ?', (password))
        if c.fetchall():
            return render_template('signup_page_passwordFail.html')
        c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password_hash))
        conn.commit()
        conn.close()
        return render_template('signup_page_success.html')
    return render_template('registry.html')

if __name__ == '__main__':
    app.run(port='10000', debug=True)'''

from flask import Flask, render_template, request, redirect, flash
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/registry', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['Username']
        email = request.form['Email']
        password = request.form['Password']

        # Проверяем если почта или имя уже использывается
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ? OR username = ?', (email, username))
        if c.fetchone():
            return render_template('signup_page_usernameOrEmailFail.html')
            conn.close()

        # Шифруем пароль
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Добавляем в базу данных
        c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password_hash))
        conn.commit()
        conn.close()
        return render_template('signup_page_success.html')
        

    return render_template('registry.html')

if __name__ == '__main__':
    app.run(port=10000, debug=True)
