from game import Game
import statistics

class Player:

    def __init__(self, name):
        self.name = None
        self.games = []
        self.count = 0
        self.existing = True

    def menu(self):
        while self.existing:
            print("""-------------------------------------
What would you like to do?
A. Play Game
B. View Stats
C. Terminate Self
-------------------------------------""")
            choice = input("Enter selection here:   ").upper()
            try:
                if choice == 'A':
                    playing = True
                    while playing:
                        self.count += 1
                        game = Game()
                        self.games.append(game.start_game())
                        decided = False
                        while decided == False:
                            try:
                                choosy = input("Do you want to play again?(Y/N)   ").upper()
                                if choosy == 'Y':
                                    decided = True
                                    playing = True
                                elif choosy == 'N':
                                    print("-------------------------------------")
                                    print("Your games will be recorded.")
                                    decided = True
                                    playing = False
                                else:
                                    raise ValueError('That selection is invalid. Only Y or N is accepted.')
                            except ValueError as err:
                                print(err)
                                continue
                if choice == 'B':
                    try:
                        if self.games:
                            print(f"""
Number of games played: {self.count}
Average of guesses: {statistics.mean(self.games)}                
Mean of guesses:{statistics.mean(self.games)}
Median of guesses:{statistics.median(self.games)}""")
                        elif self.count == 1:
                            raise Exception('You must play more than one game to make stats.')
                        else:
                            raise ValueError("Games must be played to make data for stats.")
                    except ValueError as err:
                        print(err)
                        continue
                    except Exception as err:
                        print(err)
                        continue
                if choice =="C":
                    print("""You have chosen to TERMINATE yourself.
Your existence has ended.
-------------------------------------""")
                    self.existing = False
                elif choice != 'A' or 'B' or 'C':
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