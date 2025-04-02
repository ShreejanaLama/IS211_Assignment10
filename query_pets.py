 # lets user look up people and their pets by id
import sqlite3

def get_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    # get person
    cur.execute("SELECT first_name, last_name, age FROM person WHERE id=?", (person_id,))
    person = cur.fetchone()

    if not person:
        print("sorry, that person does not exist!")
        return

    print(f"{person[0]} {person[1]}, {person[2]} years old")

    # get their pets
    cur.execute("""
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    """, (person_id,))
    pets = cur.fetchall()

    for pet in pets:
        status = "dead" if pet[3] else "alive"
        print(f"{person[0]} {person[1]} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old and is {status}.")

    conn.close()

# loop until user exits
while True:
    try:
        user_input = input("Enter person ID (-1 to exit): ")
        person_id = int(user_input)
        if person_id == -1:
            print("bye!")
            break
        get_person_and_pets(person_id)
    except ValueError:
        print("invalid input. plz enter a number")
