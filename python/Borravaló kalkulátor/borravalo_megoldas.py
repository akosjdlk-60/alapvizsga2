print("1. feladat: Borravaló kalkulátor")

osszes_ar: int = 0

emberek_szama: int = int(input("Hány fős a baráti társaság? Válasz: "))  # 1 pont
for i in range(emberek_szama):
    szemelyes_fogyasztas: int = int(input(f"Mennyit fogyasztott az {i+1}. ember (Ft)? Válasz: "))  # 1 pont, ha helyesen printeli az emberek sor számát (i+1)
    osszes_ar += szemelyes_fogyasztas

borravalo_szazalek = float(input("Hány százalék borravalót szeretne adni? Válasz: ").replace("%", ""))  # 1 pont (+1 pont ha %-lel is működik)

if borravalo_szazalek < 0:                                                          # -------- #
    print("A borravaló mértéke nem lehet negatív! 0% borravaló lesz számolva.")     #  1 pont  #
    borravalo_szazalek = 0                                                          # -------- #
    
print("\nAz összes fogyaszás: ", osszes_ar)  # 1 pont a helyes végeredményért
print("A borravaló mértéke: ", int(osszes_ar*borravalo_szazalek/100)) # 1 pont a helyes végeredményért
print("----------")
print("A végleges összeg: ", int(osszes_ar*borravalo_szazalek/100 + osszes_ar)) # 1 pont a helyes végeredményért