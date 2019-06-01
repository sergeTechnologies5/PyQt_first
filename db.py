import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/hr.db')

db.execute('''CREATE TABLE IF NOT EXISTS  expirydate (date DATE NOT NULL);''')
db.execute('''CREATE TABLE IF NOT EXISTS  ip (ip TEXT NOT NULL);''')
db.execute('''CREATE TABLE IF NOT EXISTS  url (url TEXT NOT NULL);''')
db.execute('''CREATE TABLE IF NOT EXISTS  users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,password	TEXT NOT NULL,date	TEXT)''')
db.execute('''CREATE TABLE IF NOT EXISTS  databasecredentials (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,url TEXT NOT NULL,usernname TEXT NOT NULL,password	TEXT NOT NULL,date	TEXT)''')