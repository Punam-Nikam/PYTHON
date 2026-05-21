import sqlite3

conn=sqlite3.connect('database.db')

c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY , title TEXT,done BOOLEAN)''')
c.execute('''INSERT INTO tasks (title,done) VALUES ('learn python',False)''')
conn.commit()

c.execute("SELECT * FROM tasks")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()