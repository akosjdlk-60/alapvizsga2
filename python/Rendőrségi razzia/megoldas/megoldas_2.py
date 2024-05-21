
def main() -> None:
    
    resztvevok = int(input("A házibuliban résztvevők száma: "))  # 1 p
    rendorok = int(input("A rendőrök száma: ")) # 1 p
    elso_elkap = int(input("Első rendőr által elkapott emberek: "))
    
    elszokott = rendori_elfogas(resztvevok, rendorok, elso_elkap)

    if elszokott == resztvevok: # 1p
        print("A rendőrök nem tudtak senkit sem elfogni a házibuliban.") # 1p
        
    elif 0 > elszokott: # 1p
        print("A rendőrök mindenkit el tudtak fogni a házibuliban.") # 1p
        
    else:
        print(f"A rendőrök {resztvevok-elszokott} embert fogtak el a házibuliban és {elszokott} el tudott menekülni.") # 2 p


# Gyakorlatilag recursive substraction
def rendori_elfogas(resztvevok, rendorok, kivonas_erteke): # 3. paraméter: 2p

    if rendorok == 0: # 1p
        return resztvevok

    return rendori_elfogas(resztvevok - kivonas_erteke, rendorok - 1, kivonas_erteke * 2) # 4 p

if __name__ == "__main__":
    main()
