import random
import time

def displayIntro():
    print('''Du bist in einer Welt gefangen als Ritter Kunibert.
Der einzige Weg zu überleben ist es, zwischen zwei Höhleneingängen zu wählen.
In einer wohnt ein hungriger Löwe in der anderen ein süßes Kätchen.
Der Löwe wird dich sofort verschlingen; die Katze will nur kuscheln.''')
    print()

def chooseCave():
    cave =  ''
    while cave != '1' and cave != '2':
        print('Welche Höhle möchtest du betreten? (1 oder 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('du betritts die Höhle')
    time.sleep(2)
    print('Es ist furchtbar dunkel....')
    time.sleep(2)
    print('''Etwas wuscheliges springt aus dem dunkeln auf dich zu.
Du kannst auf den ersten Blick nicht erkennen was es ist doch dann stehst du vor...''')
    print()
    time.sleep (2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('''Es kuschelt und schnurrt! Das kann nur das Kätchen sein.
Welch ein Glück!''')
    else:
        print('''Du kannst noch die Zähne im dunkeln aufblitzen sehen... dann ist alles dunkel.
Es war der Löwe''')

playAgain = 'Ja'
while playAgain == 'Ja' or playAgain == 'j':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Möchtest du es nochmal versuchen?(Ja oder Nein)' )
    playAgain = input()
