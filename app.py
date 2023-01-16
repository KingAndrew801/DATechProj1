from game import Game
import statistics

class Player:

    def __init__(self, name):
        self.name = None
        self.games = []
        self.allguesses = 0
        self.count = 0
        self.existing = True

    def game_stats(self):
        trying = True
        while trying == True:
            gameguesses = []
            for game in self.games:
                self.allguesses = self.allguesses + game.guesses
                for guesses2 in game.guesslist:
                    gameguesses.append(guesses2)
            try:
                if self.allguesses:
                    try:
                        print(f"""---------G-A-M-E---S-T-A-T-S---------
Total number of guesses made: {self.allguesses}
Average of guesses: {round(statistics.mean(gameguesses), 1)}                
Mean of guesses: {round(statistics.mean(gameguesses), 1)}
Median of guesses: {round(statistics.median(gameguesses), 1)}""")
                    except Exception:
                        print('''You must play more games with more
    guesses to calculate stats.''')
                        continue
                elif self.allguesses == 1:
                    raise Exception('You must play more than one game to make stats.')
                elif self.allguesses == 0:
                    raise ValueError("Games must be played to make data for stats.")
            except ValueError as err:
                print(err)
                trying = False
                continue
            except Exception as err:
                print(err)
                trying = False
                continue
            trying = False

    def menu(self):
        while self.existing:
            print("""-------------------------------------
What would you like to do?
A. Play Game
B. View Stats
C. Terminate Self
-------------------------------------""")
            choice = input("Enter selection here:   ").upper()
            print('-------------------------------------')
            try:
                if choice == 'A':
                    playing = True
                    while playing:
                        self.count += 1
                        gameiz = Game()
                        self.games.append(gameiz.start_game())
                        decided = False
                        while decided == False:
                            try:
                                choosy = input("Do you want to play again?(Y/N)   ").upper()
                                if choosy == 'Y':
                                    decided = True
                                    playing = True
                                    print(self.games)
                                elif choosy == 'N':
                                    print("-------------------------------------")
                                    print("Your games will be recorded.")
                                    decided = True
                                    playing = False
                                    continue
                                else:
                                    raise ValueError('That selection is invalid. Only Y or N is accepted.')
                            except ValueError as err:
                                print(err)
                                continue
                        continue
                if choice == 'B':
                    self.game_stats()
                    continue
                if choice == "C":
                    print("""You have chosen to TERMINATE yourself.
Your existence has ended.
-------------------------------------""")
                    self.existing = False
                    continue
                else:
                    raise Exception('You must choose A, B, or C. Nothing else is valid.')
            except Exception as err:
                print(err)
                continue

def begin_life():
    name = input('What is your name?   ').title()
    print("-------------------------------------")
    print(f"{name} you have been spoken into existence!!!!")
    player = Player(name)
    return player.menu()

if __name__ == '__main__':
    begin_life()
