#cetvrti zadatak

def izracunaj_prosjek(file_name):
    try:
        with open(file_name, 'r') as file:
            ukupno=0
            brojac=0

            for linija in file:
                if linija.startswith("X-DSPAM-Confidence:"):
                    try:
                        vrijednost = float(linija.split(":")[1].strip())
                        ukupno+=vrijednost
                        brojac+=1
                    except ValueError:
                        print("Greska", linija.strip())

                if brojac>0:
                    prosjek = ukupno / brojac
                    print(f"Average X-DSPAM-Confidence:  {prosjek}")
                else:
                    print("nema pronadjenih vrijednosti")

            
    except FileNotFoundError:
        print("Greska, datoteka ne postoji")
    except Exception as e:
        print("Dogodila se greska")


if __name__ == "__main__":
    ime_datoteke = input()
    izracunaj_prosjek(ime_datoteke)    
