##############################################
#   Created By Omri Haviv                    #
#   For Vidazoo home hssignment              #
#                                            #
#   this is a roullete game                  #
#   by spining the wheel you insert one coin #
#   if you guess the right number            #
#   you get 36 coins                         #
##############################################

import sys
import time
import random
import os

class Credits:
    def __init__(self):
        self._credits = 100

    def getCredits(self):
        return self._credits

    def addCredits(self,amount):
        self._credits += amount

    def insertCredit(self):
        self._credits -= 1

class Wheel:

    def __init__(self):
        pass

    def spin(self):
        parts = ['\\', '|', '/', '-']
        for i in range(36):
            number = random.randrange(0,36)
            for part in parts:
                if (i < 15):
                    sys.stdout.write("SPINNING THE WHEEL \t%d\t%s \r" % (number,part))
                elif (i < 25):
                    sys.stdout.write("BALL IS BOUNCING \t%d\t%s \r" % (number,part))
                else:
                    sys.stdout.write("!? ARE YOU READY ?! \t%d\t%s \r" % (number,part))
                sys.stdout.flush()
                time.sleep(.01 * i)
        return number

class Game:

    def __init__(self):
        self._credits = Credits()
        self.spinWheel = Wheel()


    def Menu(self):
        self.clear_console()
        self.printLine("1.Spin The Wheel\n2.Quit\n")
        return raw_input(">> ")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def spinner(self):
        guess = -1
        self._credits.insertCredit()
        while (guess < 0 or guess > 36):
            self.clear_console()
            self.printLine("Guess a number between 0 - 36 [Enter] : ")
            guess = int(raw_input())
        num = self.spinWheel.spin()
        if (guess == num):
            self.clear_console()
            self.printLine("and the number is : " + str(num) + "#\n\nOMG YOU GOT IT!!!!\nYOU ARE A LUCKY PERSON\n+36 Credits\npress Enter to continue...")
            raw_input()
            self._credits.addCredits(36)
        else:
            self.clear_console()
            self.printLine("and the number is : " + str(num) + "\n\nWrong number guessed\nyou should try again :-)\npress Enter to continue...")
            raw_input()

    def printLine(self,line=""):
        sys.stdout.write("SCORE : %d \n" % self._credits.getCredits() + "\n\n"+str(line))
        sys.stdout.flush()


if (__name__ == "__main__"):
    game = Game()
    while (True):
        option = game.Menu()
        game.clear_console()
        if (option == '1'):
            game.spinner()
        elif (option == '2'):
            game.printLine("BYE BYE !!!...")
            break