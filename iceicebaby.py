def bolletjesSelectie():
    loop = 1
    while loop == 1:
        aantalBolletjes = input("hoe veel bolletjes wilt u?")
        try:
            aantalBolletjes = int(aantalBolletjes)
            if aantalBolletjes > 8:
                print("Sorry, zulke grote bakjes hebben we niet")
            loop = 0
        except:
            print("Sorry dat snap ik niet...")
    return aantalBolletjes  


print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
aantalBolletjes = bolletjesSelectie()
if aantalBolletjes >= 1 and aantalBolletjes <= 3:
    print("")
elif aantalBolletjes >= 4 and aantalBolletjes <=8:
    print(f"Dan krijgt u van mij {aantalBolletjes} bolletjes")

