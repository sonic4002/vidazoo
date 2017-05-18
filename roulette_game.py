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
        return number.__str__()

class Game:

    def __init__(self):
        self._credits = Credits()
        self.spinWheel = Wheel()


    def Menu(self):
        os.system('cls')
        self.printLine()
        print "1.Spin The Wheel"
        print "2.Quit"
        return raw_input(">> ")

    def spinner(self):
        self._credits.insertCredit()
        self.printLine("Guess a number between 0 - 36 [Enter] : ")
        guess = raw_input()
        num = self.spinWheel.spin()
        if (guess == num):
            os.system('cls')
            self.printLine("and the number is : " + num + "#\n\nOMG YOU GOT IT!!!!\nYOU ARE A LUCKY PERSON\n+36 Credits\npress Enter to continue...")
            raw_input()
            self._credits.addCredits(36)
        else:
            os.system('cls')
            self.printLine("and the number is : " + num + "\n\nWrong number guessed\nyou should try again :-)\npress Enter to continue...")
            raw_input()

    def printLine(self,line=""):
        sys.stdout.write("SCORE : %d \n" % self._credits.getCredits() + "\n\n"+line)
        sys.stdout.flush()


if (__name__ == "__main__"):
    game = Game()
    while (True):
        option = game.Menu()
        os.system('cls')
        if (option == '1'):
            game.spinner()
        elif (option == '2'):
            game.printLine("BYE BYE !!!...")
            break