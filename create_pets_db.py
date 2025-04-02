 import sqlite3

# create and connect to a new SQLite database
conn = sqlite3.connect('pets.db')
cur = conn.cursor()

# create tables just like the assignment says
cur.execute('''
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);
''')

cur.execute('''
CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);
''')

cur.execute('''
CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
);
''')

conn.commit()
conn.close()

print("pets.db was created now load the pet.db!")
