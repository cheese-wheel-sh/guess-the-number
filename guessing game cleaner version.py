#!/usr/bin/python3
import os
import random
import sys
import time


class globalVars():
    randomNumber = None
    userNumber = None


globalVar = globalVars()


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def numberGuessedCorrectly():
    clearConsole()
    print(
        f"Du hast es geschafft!\n
        Die gesuchte Nummer war tatsächlich {globalVar.userNumber}!")
    time.sleep(5)
    sys.exit()


def checkInput():
    clearConsole()
    num = globalVar.userNumber
    if num > globalVar.randomNumber:
        print(f"Die gesuchte Zahl ist kleiner als {num}")
    elif num < globalVar.randomNumber:
        print(f"Die gesuchte Zahl ist größer als {num}")


def whileNotGuessed():
    while globalVar.userNumber != globalVar.randomNumber:
        try:
            globalVar.userNumber = int(input("Rate die gesuchte Nummer: "))
            checkInput()
        except ValueError:
            clearConsole()
            pass


if __name__ == "__main__":
    globalVar.randomNumber = random.choice(range(101))
    clearConsole()
    whileNotGuessed()
    numberGuessedCorrectly()
