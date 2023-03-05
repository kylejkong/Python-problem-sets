from pyfiglet import Figlet
import sys
import random
def main():
    figlet()


def figlet():

    figlet = Figlet()

    #get list of fonts
    fontList = figlet.getFonts()

    if len(sys.argv) == 1:

        figlet.setFont(font=random.choice(fontList))


    elif len(sys.argv) == 3:
        if sys.argv[1]=="-f" or sys.argv[1]=="--font":
            if sys.argv[2] in fontList:
                figlet.setFont(font=sys.argv[2])
            else:
                sys.exit("Invalid usage")
        else:
                sys.exit("Invalid usage")


    else:
        sys.exit("Invalid usage")




    userInput = input("Input: ")

    print(figlet.renderText(userInput))

main()

