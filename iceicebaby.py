def snapUNiet():
    print("Sorry dat snap ik niet...")
def inputSelectie(mode):
    loop = 1
    while loop == 1:
        stringInput = input("")
        if mode == 0:
            if stringInput.lower() == "a" or stringInput.lower()== "b":
                    loop = 0
            else:
                snapUNiet()
        if mode == 1:
            try:
                aantalBolletjes = int(stringInput)
                if aantalBolletjes >= 1 and aantalBolletjes <= 3:
                    print("")
                    loop = 0
                elif aantalBolletjes >= 4 and aantalBolletjes <=8:
                    print(f"Dan krijgt u van mij {aantalBolletjes} bolletjes")
                    loop = 0
                elif aantalBolletjes > 8:
                    print("Sorry, zulke grote bakjes hebben we niet")
                else:
                    snapUNiet()
            except:
                snapUNiet()
        if mode == 2:
            if stringInput.lower() == "y":
                again = 1
                loop = 0
            elif stringInput.lower() == "n":
                again = 0
                loop = 0
                print("Bedankt en tot ziens!")
            else:
                snapUNiet()
    if mode == 0:
        return stringInput.lower()
    elif mode == 1:
        return aantalBolletjes  
    elif mode == 2:
        return again 
def smaakjes(aantalBolletjes):
    for x in range( 1, aantalBolletjes+1):
        loop = 1
        while loop == 1:
            print(f"Welke smaak wilt u voor bolletje nummer {x}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            smaakKeuze = input().lower()
            if smaakKeuze != "a" and smaakKeuze != "c" and smaakKeuze != "m" and smaakKeuze != "v":
                print("Sorry dat snap ik niet...")
            else:
                loop = 0
def bonnetjeCreatie():
    print()

aankopen = [0,0,0]
again = 1   
while again == 1:
    print("Welkom bij Papi Gelato")
    print("hoe veel bolletjes wilt u?")
    aankopen[0] += inputSelectie(1)
    smaakjes(aankopen[0])
    print(f"Wilt u deze {aankopen[0]} bolletje(s) in A) een hoorntje of B) een bakje?")
    bakjeOfHoorntje = inputSelectie(0)
    if bakjeOfHoorntje == "a":
        aankopen[1] += 1
        bestelling = "hoorntje"
    elif bakjeOfHoorntje == "b":
        aankopen[2] += 1
        bestelling = "bakje"
    print(f"Hier is uw {bestelling} met {aankopen[0]} bolletje(s). Wilt u nog meer bestellen? (Y/N)")
    again = inputSelectie(2)

