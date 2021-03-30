#!/usr/bin/python3
import os
import random
import sys
import time


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def correctNumberGuessed(correctNumber: int):
    clearConsole()
    print(f"Du hast es geschafft!\n
          Die gesuchte Nummer war tatsächlich {correctNumber}!")
    time.sleep(5)
    sys.exit()


def checkInput(randomNumber: int):
    userNumber = None
    while userNumber != randomNumber:
        try:
            userNumber = int(input("Rate die gesuchte Nummer: "))
            if userNumber > randomNumber:
                clearConsole()
                print(f"Die gesuchte Zahl ist kleiner als {userNumber}")
            elif userNumber < randomNumber:
                clearConsole()
                print(f"Die gesuchte Zahl ist größer als {userNumber}")
        except ValueError:
            clearConsole()
            pass


if __name__ == "__main__":
    randomNumber = random.choice(range(101))
    checkInput(randomNumber)
    correctNumberGuessed(randomNumber)
