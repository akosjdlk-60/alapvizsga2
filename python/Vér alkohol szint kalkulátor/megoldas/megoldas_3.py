import os

class Ital: # 1p split, 1p tisza_alkohol_tartalom, 1p többi __init__ => 3p
    #sor = nev;ar;egyseg;alkohol_szazalek%
    def __init__(self, sor: str) -> None:
        _split = sor.split(",")
        self.nev = _split[0]
        self.ar = int(_split[1])
        self.egyseg = int(_split[2])
        self.alkohol_szazalek = float(_split[3])

    @property
    def tisza_alkohol_tartalom(self) -> float: # 1p
        return float(self.egyseg*self.alkohol_szazalek/10) # ml /egyseg(cl)

    def __str__(self) -> str:
        return f"Ital: {self.nev} ({self.ar} Ft, {self.alkohol_szazalek}%)"

    def __repr__(self) -> str:
        return f"Ital: {self.nev} ({self.ar} Ft, {self.alkohol_szazalek}%)"


class Ember: # 1p/saját függvény + 2p ver_alkohol_szazalek => 3p
    def __init__(self, nev: str, ferfi: bool, tomeg: float) -> None:
        self.nev: str = nev
        self.nemi_szorzo: float = self.nemi_szorzo_calc(ferfi)
        self.tomeg: float = tomeg
        self.fogyasztott_italok: list[Ital] = []

    def nemi_szorzo_calc(self, ferfi: bool) -> float: # 1p
        if ferfi:
            return 0.68
        else:
            return 0.55

    def elivott_vagyon(self) -> int: # 1p
        osszeg = 0
        for ital in self.fogyasztott_italok:
            osszeg += ital.ar
        
        return osszeg

    def ver_alkohol_szazalek(self) -> float: # 2p
        osszes_alkohol_ml = 0

        for ital in self.fogyasztott_italok:
            osszes_alkohol_ml += ital.tisza_alkohol_tartalom
            
        return osszes_alkohol_ml * 0.78506 / self.tomeg * self.nemi_szorzo

    def __str__(self) -> str:
        return f"{self.nev}, {self.tomeg} kg"

    def __repr__(self) -> str:
        return f"{self.nev}, {self.tomeg} kg"


def italok_beolvasasa(file_path: str) -> list[Ital]: # 1p
    italok = []
    with open(file_path, "r", encoding="utf-8") as f:
        f.readline()
        for sor in f:
            italok.append(Ital(sor))
    return italok


CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), "../italok.csv")

def main() -> None:
    italok: list[Ital] = italok_beolvasasa(CSV_FILE_PATH)
    emberek_szama = int(input("Emberek száma: ")) # 0,5p
    emberek: list[Ember] = []

    for i in range(emberek_szama):
        tomeg = kor = ferfi = 0
        
        nev = input(f"\n{i+1}. Ember:\nNév: ") # 0,5p
        
        # Az összes while loopos inputnál 1p
        while kor < 18:
            try:
                kor = int(input("Kor: "))
                if kor < 18:
                    print("\n18 évnél fiatalabb nem fogyaszthat alkoholt!\n") # 1p
            except ValueError:
                print("\nNem megfelelő kor!\n")

        while ferfi != "igen" and ferfi != "nem":
            ferfi = input("Férfi? (igen/nem): ").strip().lower()
            if ferfi != "igen" and ferfi != "nem":
                print("\nNem megfelelő érték!\n")
        
        while tomeg == 0:
            try:
                tomeg = float(input("Tömeg (kg): ").replace(",", ".")) # 1p, a replace miatt
            except ValueError:
                print("\nNem megfelelő tömeg!\n")
            
        emberek.append(Ember(nev, ferfi == "igen", tomeg))

    ################# 13 #################

    for ember in emberek:
        print(f"\n{ember.nev} által fogyasztott italok:")
        while True:
            for i, ital in enumerate(italok):
                print(f"{i+1}. {ital.nev}")
                
            try: # 1p
                valasztas = int(input("Választott ital sorszáma: "))
                if valasztas < 1 or valasztas > len(italok):
                    print("\nNem megfelelő sorszám!\n")
                    continue
            except ValueError:
                print("\nNem megfelelő sorszám!\n")
                continue

            while True:
                try: # 2p
                    mennyiseg = int(input("Mennyiség: "))
                except ValueError:
                    print("\nNem megfelelő mennyiség!\n")
                    continue

                if mennyiseg >= 1:
                    break
                else:
                    print("\nNem megfelelő mennyiség!\n")

            ember.fogyasztott_italok.extend([italok[valasztas-1]]*mennyiseg)

            match input("\nMég egy ital? (igen/nem): ").strip().lower(): # ha az egész match blokk helyes 1p
                case "igen":
                    continue

                case "nem":
                    break

                case _:
                    print("\nNem megfelelő érték!\n")
                    continue

    for ember in emberek:
        print(f"\n{ember.nev} véralkohol szintje: {round(ember.ver_alkohol_szazalek(), 3)}%") # 0,5p
        print(f"{ember.nev} fogyasztott italokra költött összeg: {ember.elivott_vagyon()} Ft") # 0,5p
    

if __name__ == "__main__":
    main()