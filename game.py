import random
import statistics

class Game:
    def __init__(self):
        self.answer = random.randint(1,100)
        self.guesses = 0
        self.solved = False
        self.guesslist = []

    def __repr__(self):
        return f"{self.guesses}"

    def start_game(self):
        print("""
A random number has been selected between 1 and 100
you will type your guesses below until you guess the number""")
        while self.solved == False:
            try:
                print(self.answer)
                choice = int(input("""-------------------------------
What is your guess?  """))
                self.guesses += 1
                self.guesslist.append(choice)
                if choice < 1 or choice > 100:
                    raise ValueError("You need to guess using numbers between 1 and 100.")
                elif bool(isinstance(choice, int)) == False:
                    raise ValueError("You have to guess using numbers.")
                elif isinstance(choice, int):
                    if choice == self.answer:
                        self.solved = True
                        print("That is correct!")
                        return self.guesses
                    else:
                        print("That answer is incorrect.")
                        if choice < self.answer:
                            print("You need to go higher")
                        if choice > self.answer:
                            print("You need to go lower.")
                else:
                    raise ValueError("You need to guess using numbers.")
            except ValueError as err:
                print(err)
            print(f"""-------------------------------
You have made {self.guesses} guesses.
The mean of your guesses is: {statistics.mean(self.guesslist)}
The median of your guesses is: {statistics.median(self.guesslist)}
The mode of your guesses is: {statistics.mode(self.guesslist)}""")

if __name__ == '__main__':
    game = Game()
    game.start_game()