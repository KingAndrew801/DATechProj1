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
        print("""You have created a number between 1 and 100.
Now try to guess the number by typing it below.""")
        while self.solved == False:
            try:
                # print(self.answer)
                choice = int(input("""-------------------------------------
What is your guess?  """))
            except ValueError:
                print('That guess is invalid. You have to guess using numbers.')
                continue
            self.guesses += 1
            self.guesslist.append(choice)
            try:
                if choice < 1 or choice > 100:
                    raise Exception("You need to guess using numbers between 1 and 100.")
                elif isinstance(choice, int):
                    if choice == self.answer:
                        self.solved = True
                        print("That is correct!")
                        return self
                    else:
                        print("That answer is incorrect.")
                        if choice < self.answer:
                            print("You need to go higher")
                        if choice > self.answer:
                            print("You need to go lower.")
            except Exception as err:
                print(err)
                continue
            except TypeError as err:
                print(err)
                continue
            print(f"""-------------------------------------
You have made {self.guesses} guesses this game.
The mean of these guesses is: {statistics.mean(self.guesslist)}
The median of these guesses is: {statistics.median(self.guesslist)}
The mode of these guesses is: {statistics.mode(self.guesslist)}""")

if __name__ == '__main__':
    game = Game()
    game.start_game()