import random
import time

def output(text) :
    print(text)

def add(val1, val2) :
    calculated = val1 + val2
    return(calculated)

def subtract(val1, val2) :
    calculated = val1 - val2
    return(calculated)

def multiply(val1, val2) :
    calculated = val1 * val2
    return(calculated)

def share(val1, val2) :
    calculated = val1 / val2
    return(calculated)

def ask(ask) :
    output = input(ask)
    return(output)

def yipee() :
    print("Thanks for using earthworm")
def randomint(min,max) :
    return(random.randint(min,max))

def throwup() :
    options = ["   ||", "  |  | |", " ||  | ||", " |  || | ||", " |  | || || ", "|| | | || || |"]
    print("  ________  \n /        \\ \n |   > <  | \n |    ^   | \n | _____  | \n \\_|   |__/")

    while True :
        print("   |   | \n" * 2)
        print(random.choice(options))
        time.sleep(0.06)
