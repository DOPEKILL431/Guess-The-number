from random import randint
from colorama import Back,Fore,Style,deinit,init



hp=5
number=randint(0,10)
response_user=int

while hp>0 and number!=response_user:

    response_user=int(input("Entrez votre chiffre :"))
    print()

    if response_user ==number :
        print(Fore.GREEN+Style.NORMAL + "Vous avez trouvé le bon nombre , vous avez gagner le jeu ! ")
    
    if response_user > number :
        print(Fore.RED+Style.NORMAL + "Too high")
        hp=hp-1
        print(Fore.RED+Style.NORMAL + "On vous retire 1 hp sur votre vie , il vous reste alors ",hp," hp ")
        print()
        
    if response_user < number :
        print(Fore.RED+Style.NORMAL + "Too low")
        hp=hp-1
        print(Fore.RED+Style.NORMAL + "On vous retire 1 hp sur votre vie , il vous reste alors ",hp," hp ")
        print()
        


