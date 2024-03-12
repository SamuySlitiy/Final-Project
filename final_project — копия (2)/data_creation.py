import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_db_table():
    c.execute('''
              CREATE TABLE IF NOT EXISTS users
              (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT,
                password TEXT
              )
              ''')
def add_data():
    data = [('samuy_SliTiY', 'saniasava0107@gmail.com', '1234')]
    c.executemany('''INSERT INTO users(username, email, password) VALUES (?,?,?)''', data)
    print(data)
    
data2 = c.fetchall()
conn.commit()