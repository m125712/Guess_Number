import random
class GuessingGame():
    def __init__(self,attempts=5,min_num=0,max_num=10):
        self.number = random.randint(min_num, max_num)
        self.attempts = attempts
        self.min_num = min_num
        self.max_num = max_num

    def play(self):

        print(f"Think number between {self.min_num} and {self.max_num}. You have {self.attempts} guesses.")
        while self.attempts > 0:
            try:
                guess = int(input("Guess a number: "))
                if self.validate_guess(guess):
                    self.attempts -= 1
                    if guess == self.number:
                        print("You guessed it!")
                        break
                    elif guess > self.number:
                        print("Too high! Try again.")
                    else:
                        print("Too low! Try again.")
                else:
                    print(f"Invalid guess. Please enter a number between {self.min_num} and {self.max_num}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if self.attempts == 0:
            print(f"You ran out of guesses. The number was {self.number}.")

    def validate_guess(self, guess):
        return self.min_num <= guess <= self.max_num

if __name__ == "__main__":
    game = GuessingGame()
    game.play()