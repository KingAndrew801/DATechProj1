import random

class Game:
     def __init__(self):
        self.answer = random.randint(1,100)
        self.guesses = 0
        self.solved = False

    def start_game(self):
        print("""A random number has been selected between 1 and 100
        you will type your guesses below until you guess the number""")
        while self.solved == False:
            try:
                choice = input("What is your guess?  ")
                self.guesses += 1
                if choice == self.answer:
                    self.solved == True

if __name__ == '__main__':
    game = Game()
    game.start_game()