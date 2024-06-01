import random
class Guess():
    def __init__(self, number):
        self.number = number

    def guess(self, number):
        if number == self.number:
            print("You guessed it!")
            return 0
        elif number > self.number:
            print("Too high!")
            
        else:
            print("Too low!")


number = random.randint(1,10)
while True:
    guess_number = int(input("Guess a number between 1 and 10: "))
    guess=Guess(number)
    if guess.guess(guess_number) == 0:
        break