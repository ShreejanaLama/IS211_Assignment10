 # this file loads the data into pets.db
import sqlite3

# connect to the pets.db
conn = sqlite3.connect('pets.db')
cur = conn.cursor()

# list of people (id, fname, lname, age)
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

# insert into person table
cur.executemany("INSERT INTO person VALUES (?, ?, ?, ?);", people)

# pets (id, name, breed, age, dead (1 = yes, 0 = no))
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

# insert into pet table
cur.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?);", pets)

# link table (person_id, pet_id)
person_pet = [
    (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)
]

# insert into person_pet
cur.executemany("INSERT INTO person_pet VALUES (?, ?);", person_pet)

# save and close
conn.commit()
conn.close()
print("data loaded into pets.db!, now run the query")
