

# Oppgave 5
def hovedmeny():
    print("Velkommen! (skriv 1/2/3/4 eller vis/legg/søk/avslutt)")
    while True:
        print("1. Vis alle\n2. Legg til ny\n3. Søk\n4. Avslutt")
        valg = input("Ditt valg: ").strip().lower()

        if valg in ("1", "vis", "v"):
            vis_alle()
        elif valg in ("2", "legg", "l", "legg til", "leggtil"):
            legg_til()
        elif valg in ("3", "søk", "sok", "s"):
            sok()
        elif valg in ("4", "avslutt", "stopp", "a"):
            print("Programmet avsluttes.")
            break
        else:
            print("Ugyldig valg, prøv igjen.\n")



