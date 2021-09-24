import random

print("Bienvenue dans le jeu 'guess the number', vous devez deviner un nombre sur l'étendu sélectionnée\n")
range = input("Entrez un nombre entier strictement positif qui définit les limites du nombre à deviner :\n")

while not range.isdigit() or int(range) < 0:
    range = input("Erreur : entrez un nombre entier strictement positif qui définit les limites du nombre à deviner :\n")    

randNumber = random.randint(0,int(range))
print(randNumber)

print("Vous devez deviner un nombre compris entre 0 et "+range+" inclus")
inputNumber = input("entrez un nombre compris entre 0 et "+range+" inclus :\n")

intRange = int(range)

while not inputNumber.isdigit() or int(inputNumber) > int(range):
    inputNumber = input("Erreur : entrez un nombre compris entre 0 et "+range+" inclus\n")

number = int(inputNumber)
cpt = 1

while number != randNumber:
    if number > randNumber:
        while not inputNumber.isdigit() or int(inputNumber) > int(range):
            inputNumber = input("Erreur : entrez un nombre compris entre 0 et "+range+" inclus\n")
        inputNumber = input("le nombre entré est supérieur au nombre à deviné ! essayer un nombre inférieur :\n")
        number = int(inputNumber)
        cpt += 1
    else:
        while not inputNumber.isdigit() or int(inputNumber) > int(range):
            inputNumber = input("Erreur : entrez un nombre compris entre 0 et "+range+" inclus\n")
        inputNumber = input("le nombre entré est inférieur au nombre à deviné ! essayer un nombre supérieur :\n")
        number = int(inputNumber)
        cpt += 1

print("Bravo, vous avez trouvé en "+str(cpt)+" tentative(s) !")