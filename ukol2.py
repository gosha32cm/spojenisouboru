
from funkce import pozdrav, dnesni_den, vypis_cisla, obdelnik, nalada_dne

def main():
    while True:
        print("--- MENU ---")
        print("1. Pozdrav")
        print("2. Dnešní den")
        print("3. Čísla 1 až 5")
        print("4. Obdélník z hvězdiček")
        print("5. Nálada dne")
        print("6. Konec")
        volba = input("Zadej číslo: ")

        if volba == "1":
            pozdrav()
        elif volba == "2":
            dnesni_den()
        elif volba == "3":
            vypis_cisla()
        elif volba == "4":
            obdelnik()
        elif volba == "5":
            nalada_dne()
        elif volba == "6":
            print("Program končí.")
            break
        else:
            print("Neplatná volba, zkus to znovu.")

if __name__ == "__main__":
    main()
