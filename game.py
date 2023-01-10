import random

class Game:
    def __init__(self):
        self.answer = random.randint(1,100)
        self.guesses = 0
        self.solved = False

    def start_game(self):
        print("""
A random number has been selected between 1 and 100
you will type your guesses below until you guess the number""")
        while self.solved == False:
            try:
                choice = int(input("What is your guess?  "))
                self.guesses += 1
                if choice < 1 or choice > 100:
                    print("You must guess between 1 and 100")
                    pass
                if choice == int:
                    if choice == self.answer:
                        self.solved == True
                    else:
                        print("That answer is incorrect.")
                        if choice > self.answer:
                            print("You need to go higher")
                        if choice < self.answer:
                            print("You need to go lower.")
                else:
                    raise ValueError("You need to guess using numbers.")
            except ValueError as err:
                print(err)


if __name__ == '__main__':
    game = Game()
    game.start_game()