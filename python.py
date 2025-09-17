

# Oppgave 2
def vis_alle():
    if not telefonbok:
        print("Telefonboka er tom.")
    else:
        print("\n--- Telefonbok ---")
        for person in telefonbok:
            print(f"{person['navn']}: {person['nummer']}")
        print("------------------\n")

