
class Ital:
    def __init__(self, sor: str) -> None:
        self.nev: str = ...
        self.ar: int = ...
        self.egyseg: int = ...
        self.alkohol_szazalek: float = ...

    @property # Ezzel a property dekorátorral lehet egy függvényt úgy használni, mintha egy változó lenne:   self.tisza_alkohol_tartalom()   -->   self.tisza_alkohol_tartalom
    def tisza_alkohol_tartalom(self) -> float:
        return ... # Hány ml tiszta alkohol van egy egyseg(cl) italban, 1cl = 10ml


    # Ezt a stringet fogja kiírni a print függvény
    def __str__(self) -> str:
        return f"Ital: {self.nev} ({self.ar} Ft, {self.alkohol_szazalek}%)"

    def __repr__(self) -> str:
        return f"Ital: {self.nev} ({self.ar} Ft, {self.alkohol_szazalek}%)"
    
class Embed:
    def __init__(self, nev: str, ferfi: bool, tomeg: float) -> None:
        self.nev: str = ...
        self.ferfi: bool = ...
        self.tomeg: float = ...
        self.fogyasztott_italok: list[Ital] = ...
        self.nemi_szorzo = self.nemi_szorzo_calc(ferfi)

    def elivott_vagyon(self) -> int:
        pass

    def nemi_szorzo_calc(self, ferfi: bool) -> float:
        # 0.68 a nők, 0.55 a férfiak átlagos szorzója
        pass

    def ver_alkohol_szazalek(self) -> float:
        # Vér alkohol % = Összes alkohol (grammban) * tömeg (kg) * nemi szorzó
        # 1 gramm alkohol = 0.78506 ml
        pass

    # Ezt a stringet fogja kiírni a print függvény
    def __str__(self) -> str:
        return f"{self.nev}, {self.tomeg} kg"

    def __repr__(self) -> str:
        return f"{self.nev}, {self.tomeg} kg"