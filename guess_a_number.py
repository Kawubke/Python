# Dieses Programm hat eine geheime Zahl
import random

guessesTaken = 0

print("Hi wie ist dein Name?")
player = input()

number = random.randint(1, 20)
print("Also, ich denke an eine Zahl zwischen 1 und 20 ausgedacht. Kannst du sie erraten?")

while guessesTaken < 6:
    print("Probiere dein Glück")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Meine Zahl ist höher!")

    if guess > number:
        print("Meine Zahl ist niedriger")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Super gemacht, " + player + "! Du hast meine Nummer mit " + guessesTaken + " Versuchen erraten!")

if guess != number:
    number = str(number)
    print("Schade. Die Zahl an die ich gedacht habe war " + number)
