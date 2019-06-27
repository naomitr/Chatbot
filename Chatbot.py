# --- Define your functions below! ---

from random import *

def intro():
    for i in range(1):
        answer = input("Say 'Hi' to active ChatBot!")
        answer = answer.lower()
        if answer == "hi":
            answer = input("Would you like to learn my name?")
            if answer == "yes":
                print("Hi!")
                print("My name is")
                print("______         ____        _         ____   ___   ___   ___  ")
                print("|  ____|       |  _ \      | |       |___ \ / _ \ / _ \ / _ \ ")
                print("| |____   _____| |_) | ___ | |_ ______ __) | | | | | | | | | |")
                print("|  __\ \ / / _ \  _ < / _ \| __|______|__ <| | | | | | | | | |")
                print("| |___\ V /  __/ |_) | (_) | |_       ___) | |_| | |_| | |_| |")
                print("|______\_/ \___|____/ \___/ \__|     |____/ \___/ \___/ \___/ ")
                answer = input("What's your name?")
                if answer == answer:
                    print("Cool name!")
            else:
                print("Okay, but I'll tell you anyways!")
                print("My name is EveBot-3000!")
                answer = input("What's your name?")
                if answer == answer:
                    print("Cool name!")

def choices():
    for i in range (1):
        print("You're at the")
        print("  _____ _           _                 __  __                  ")
        print(" / ____| |         (_)               |  \/  |                 ")
        print("| |    | |__   ___  _  ___ ___  ___  | \  / | ___ _ __  _   _ ")
        print("| |    | '_ \ / _ \| |/ __/ _ \/ __| | |\/| |/ _ \ '_ \| | | |")
        print("| |____| | | | (_) | | (_|  __/\__ \ | |  | |  __/ | | | |_| |")
        print(" \_____|_| |_|\___/|_|\___\___||___/ |_|  |_|\___|_| |_|\__,_|")
        print("Would you like to know about what I can do?")
        answer = input("Just type 'Yes'!")
        if answer == "yes":
            print("I can show you art!")
            print("Type 'Art' to see art!")
            print("I can tell you poems!")
            print("Type 'Poem' to see a poem!")
            print("I can play a game with you!")
            print("Type 'Game' to play a game with me!")

    # input from the user about which path to take
    choice = input()
    choice = choice.lower()
    if choice == "art":
        art()
    elif choice == "game":
        game()
        # game()
    elif choice == "poem":
        poem()
        # poem()


def art():
    for i in range(1):
        print(".----------------.  .----------------.  .----------------. ")
        print("| .--------------. || .--------------. || .--------------. |")
        print("| |      __      | || |  _______     | || |  _________   | |")
        print("| |     /  \     | || | |_   __ \    | || | |  _   _  |  | |")
        print("| |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | |")
        print("| |   / ____ \   | || |   |  __ /    | || |     | |      | |")
        print("| | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | |")
        print("| ||____|  |____|| || | |____| |___| | || |   |_____|    | |")
        print("| |              | || |              | || |              | |")
        print("| '--------------' || '--------------' || '--------------' |")
        print("'----------------'  '----------------'  '----------------'  ")
        print("I have three artworks!")
        print("Would you like to see 1, 2 or 3?")
        answer = input("Just type '1', '2', or '3' to see the options!")
        if answer == "1":
            art1()
        if answer == "2":
            art2()
        if answer == "3":
            art3()

def art1():
    print("   ______________________________")
    print(" / \                             \.")
    print("|   |                            |.")
    print("    |                            |.")
    print("    |           /\_/\            |.")
    print("    |          ( o.o )           |.")
    print("    |           > ^ <            |.")
    print("    |                            |.")
    print("    |                            |.")
    print("    |   _________________________|___")
    print("    |  /                            /.")
    print("    \_/____________________________/.")
    answer = input("Did you like my art?")
    print("Awesome!")
    print("You're going back to the choices menu now!")
    choices()


def art2():
    print(" ____________________________")
    print("|  ________________________  |")
    print("| |                        | |")
    print("| |                        | |")
    print("| |                        | |")
    print("| |                        | |")
    print("| |      ^..^      /       | |")
    print("| |      /_/\_____/        | |")
    print("| |         /\   /\        | |")
    print("| |        /  \ /  \       | |")
    print("| |                        | |")
    print("| |                        | |")
    print("| |________________________| |")
    print("|____________________________|")
    answer = input("Did you like my art?")
    print("Awesome!")
    print("You're going back to the choices menu now!")
    choices()

def art3():
    print("........................................................................")
    print(":      ,~~.          ,~~.          ,~~.          ,~~.          ,~~.    :")
    print(":     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,:")
    print(":(\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  :")
    print(": \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )    :")
    print(":  \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /     :")
    print(": ~'`~'`~'`~`~'`~'`~'`~'`~`~'`~'`~'`~'`~`~'`~'`~'`~'`~'`~`~'`~'`~'`~'` :")
    print(":      ,~~.    ..........................................      ,~~.    :")
    print(":     (  9 )-_,:                                        :     (  9 )-_,:")
    print(":(\___ )=='-'  :                                        :(\___ )=='-'  :")
    print(": \ .   ) )    :                            |           : \ .   ) )    :")
    print(":  \ `-' /     :     \,/                _  _|_  _       :  \ `-' /     :")
    print(":   `~j-'      :                       |;|_|;|_|;|      :   `~j-'      :")
    print(":     '=:      :                       \\.     .  /      :     '=:      :")
    print(":      ,~~.    :                        \\:   .  /       :      ,~~.    :")
    print(":     (  9 )-_,:              \,/        ||:   |        :     (  9 )-_,:")
    print(":(\___ )=='-'  :   \,/                   ||:.  |        :(\___ )=='-'  :")
    print(": \ .   ) )    :                         ||:  .|        : \ .   ) )    :")
    print(":   `~j-'      :                         ||: , |        :      ,~~.    :")
    print(":  \ `-' /     :                 /`\     ||:   |        :  \ `-' /     :")
    print(":     (  9 )-_,:        /`\              ||:   |        :     (  9 )-_,:")
    print(":(\___ )=='-'  :                         ||: . |        :(\___ )=='-'  :")
    print(": \ .   ) )    :                        _||_   |        : \ .   ) )    :")
    print(":  \ `-' /     :--~~__            __ ----~    ~`---,    :  \ `-' /     :")
    print(":   `~j-'      :   ~---__ ,--~'                  ~~----_:   `~j-'      :")
    print(":     '=:      :........................................:     '=:      :")
    print(":      ,~~.          ,~~.          ,~~.          ,~~.          ,~~.    :")
    print(":     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,:")
    print(":(\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  :")
    print(": \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )    :")
    print(":  \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /     :")
    print(": ~'`~'`~'`~`~'`~'`~'`~'`~`~'`~'`~'`~'`~`~'`~'`~'`~'`~`~'`~'`~'`~'`~'` :")
    print(":......................................................................:")
    answer = input("Did you like my art?")
    print("Awesome!")
    print("You're going back to the choices menu now!")
    choices()

def game():
    print(".------..------..------..------.")
    print("|G.--. ||A.--. ||M.--. ||E.--. |")
    print("| :/\: || (\/) || (\/) || (\/) |")
    print("| :\/: || :\/: || :\/: || :\/: |")
    print("| '--'G|| '--'A|| '--'M|| '--'E|")
    print("`------'`------'`------'`------'")
    print("Now we'll play a number guessing game!")
    print("I'm thinking of a number from one to twenty...")
    print("You have four chances to guess!")
    aRandomNumber = randint(1, 20)
    for i in range(4):
        guess = input("Guess a number between 1 and 20 (inclusive): ")

        if not guess.isnumeric():
        	print("That's not a positive whole number, try again!")
        else:
        	guess = int(guess)
        if guess > aRandomNumber:
            print("Guess lower!")
        elif guess < aRandomNumber:
            print("Guess higher!")
    choices()
def poem():
    print(" /$$$$$$$                                  ")
    print("| $$__  $$                                 ")
    print("| $$  \ $$ /$$$$$$   /$$$$$$  /$$$$$$/$$$$ ")
    print("| $$$$$$$//$$__  $$ /$$__  $$| $$_  $$_  $$")
    print("| $$____/| $$  \ $$| $$$$$$$$| $$ \ $$ \ $$")
    print("| $$     | $$  | $$| $$_____/| $$ | $$ | $$")
    print("| $$     |  $$$$$$/|  $$$$$$$| $$ | $$ | $$")
    print("|__/      \______/  \_______/|__/ |__/ |__/")
    print("You may shoot me with your words,")
    print("You may cut me with your eyes,")
    print("You may kill me with your hatefulness,")
    print("But still, like air, I’ll rise.")
    print("By: Maya Angelou")
    choices()
# --- Put your main program below! ---


def main():
    intro()
    choices()



# DON'T TOUCH! Setup code that runs your main() function.
main()
