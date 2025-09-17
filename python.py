

# Oppgave 4
def sok():
    navn = input("Hvem vil du søke etter? ").strip()
    for person in telefonbok:
        if person["navn"].lower() == navn.lower():
            print(f"Fant: {person['navn']} - {person['nummer']}\n")
            return
    print("Person ikke funnet.\n")


