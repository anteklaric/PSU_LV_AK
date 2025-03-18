#treci zadatak
def main():
    brojevi = []

    while True:
        unos = input("Unos broja ili Done")
        if unos.lower == "done":
            break

        try:
            broj=float(unos)
            brojevi.append(broj)
        except ValueError:
            print("Greska")


    if brojevi: 
        print(f"Ukupno unesenih brojeva: {len(brojevi)}")
        print(f"Minimalna vrijednost: {min(brojevi)}")
        print(f"Maksimalna vrijednost:  {max(brojevi)}")
        brojevi.sort()
        print("Sortirana lista: ", brojevi)
    else:
        print("Nije unesen nijedan broj")

if __name__ == "__main__":
    main()                   
