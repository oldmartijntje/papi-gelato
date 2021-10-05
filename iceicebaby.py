def bolletjesSelectie():
    loop = 1
    while loop == 1:
        aantalBolletjes = input("hoe veel bolletjes wilt u?")
        try:
            aantalBolletjes = int(aantalBolletjes)
            if aantalBolletjes >= 1 and aantalBolletjes <= 3:
                print("")
                loop = 0
            elif aantalBolletjes >= 4 and aantalBolletjes <=8:
                print(f"Dan krijgt u van mij {aantalBolletjes} bolletjes")
                loop = 0
            elif aantalBolletjes > 8:
                print("Sorry, zulke grote bakjes hebben we niet")
            else:
                print("Sorry dat snap ik niet...")
        except:
            print("Sorry dat snap ik niet...")
    return aantalBolletjes  
def bakjeOfHoorntje():
    print()
    

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
aantalBolletjes = bolletjesSelectie()


