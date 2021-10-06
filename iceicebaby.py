def snapUNiet():
    print("Sorry dat snap ik niet...")
def bonnetjeCheck(nummer,naam,prijs,aankopen):
    if aankopen[nummer] > 0:
        print(naam+str(aankopen[nummer])+" x "+str(prijs)+"   = €" + str(aankopen[nummer]*prijs))
        return aankopen[nummer]*prijs
    else:
        return 0
def inputSelectie(mode):
    loop = 1
    while loop == 1:
        stringInput = input("")
        if mode == 3:
            if stringInput.lower() == "a" or stringInput.lower()== "b"or stringInput.lower()== "c"or stringInput.lower()== "d":
                    loop = 0
            else:
                snapUNiet()
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
    if mode == 0 or mode == 3:
        return stringInput.lower()
    elif mode == 1:
        return aantalBolletjes  
    elif mode == 2:
        return again 
def smaakjes(aantalBolletjes):
    for x in range( 1, aantalBolletjes[3]+1):
        loop = 1
        while loop == 1:
            print(f"Welke smaak wilt u voor bolletje nummer {x}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            smaakKeuze = input().lower()
            if smaakKeuze != "a" and smaakKeuze != "c" and smaakKeuze != "m" and smaakKeuze != "v":
                print("Sorry dat snap ik niet...")
            else:
                loop = 0
def toppingsKeuzeNaarNummer(toppingsKeuze,bakjeOfHoorntje):
    if toppingsKeuze == "b":
        return 4
    elif toppingsKeuze == "c":
        return 5
    elif toppingsKeuze == "d":
        if bakjeOfHoorntje == "a":
            return 6   
        elif bakjeOfHoorntje == "b":
            return 7
    else:
        return "nee"
            
        
def bonnetjeCreatie(aankopen):
    kosten = 0
    print('--------["Papi Gelato"]--------\n')
    kosten += bonnetjeCheck(0,"Bolletjes    ",1.10,aankopen)
    kosten += bonnetjeCheck(1,"Horrentje    ",1.25,aankopen)
    kosten += bonnetjeCheck(2,"Horrentje    ",0.75,aankopen)
    print("                         -------+\nTotaal                   = €"+str(kosten))
    print(aankopen)

aankopen = [0,0,0,0,0,0,0,0]
again = 1   
while again == 1:
    print("Welkom bij Papi Gelato")
    print("hoe veel bolletjes wilt u?")
    aankopen[3] = inputSelectie(1)
    aankopen[0] += aankopen[3]
    smaakjes(aankopen)
    print(f"Wilt u deze {aankopen[3]} bolletje(s) in A) een hoorntje of B) een bakje?")
    bakjeOfHoorntje = inputSelectie(0)
    if bakjeOfHoorntje == "a":
        aankopen[1] += 1
        bestelling = "hoorntje"
    elif bakjeOfHoorntje == "b":
        aankopen[2] += 1
        bestelling = "bakje"
    print("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
    toppingKeuze = inputSelectie(2)
    nummer = toppingsKeuzeNaarNummer(toppingKeuze,bakjeOfHoorntje)
    if nummer != "nee":
        aankopen[nummer] +=1
    print(f"Hier is uw {bestelling} met {aankopen[0]} bolletje(s). Wilt u nog meer bestellen? (Y/N)")
    again = inputSelectie(2)
bonnetjeCreatie(aankopen)
