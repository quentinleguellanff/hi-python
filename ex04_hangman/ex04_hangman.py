import random
from words import english_words

tentative = 10
indexList = []
letterList = []
letter = ''
strGuessing = ''
index = random.randint(0,len(english_words)-1)
wordToGuess = english_words[index]
listWordToGuess = list(wordToGuess)


print("\nBienvenue dans le jeu du Pendu, vous devez devez deviner un mot en anglais !")
print(f'le mot que vous devez deviner contient { len(wordToGuess) } mots, vous avez '+ str(tentative) +' tentatives pour le trouver ! ')

for i in range(len(wordToGuess)):
    strGuessing += '_'
print(strGuessing + '\n')
StrGuessingList  = list(strGuessing)



while strGuessing != wordToGuess and tentative != 0:
    indexList.clear()
    letter = input('entrez une lettre pour tenter de deviner le mot :\n')
    while len(letter) != 1 or not letter.isalpha():
        letter = input('Erreur : entrez une lettre pour tenter de deviner le mot :\n')
    cpt = 0
    if letter not in letterList :
        letterList.append(letter)
        strLetterList = "".join(letterList)
        if letter in wordToGuess:
            for i in range(len(wordToGuess)):
                if letter == wordToGuess[i]:
                    indexList.append(i)
                    cpt += 1
            for y in range(len(indexList)):
                StrGuessingList[indexList[y]] = letter
            strGuessing = "".join(StrGuessingList)
            print('\nBien joué ! Vous avez entré la lettre '+ letter + ' présente '+ str(cpt) + ' fois dans le mot')
            print('liste des lettres deja utilisées : '+ strLetterList)
            print('le mot à deviner : ' + strGuessing)
        else :
            tentative -= 1
            if tentative != 0: 
                print('\nla lettre '+ letter + " n'est pas présente dans le mot, il vous reste "+ str(tentative) + ' tentatives')
                print('liste des lettres deja utilisées : '+ strLetterList)
                print('le mot à deviner : ' + strGuessing)
    else:
        print("Vous avez déjà entré cette lettre, essayez en une autre !")
        print('liste des lettres deja utilisées : '+ strLetterList)

if tentative == 0:
    print('Dommage, vous avez perdu !, le mot à deviner était ' + wordToGuess)
else:
    print('Bravo ! Vous avez trouvez le mot qui était '+wordToGuess + " vous l'avez trouvé en "+ str(10-tentative) + ' tentatives !')