
# Oppgave 3
def legg_til():
    navn = input("Skriv inn et navn: ").strip()
    nummer = input("Skriv inn et nummer: ").strip()
    ny_person = {"navn": navn, "nummer": nummer}
    telefonbok.append(ny_person)
    print(f"{navn} ble lagt til i telefonboka.\n")

