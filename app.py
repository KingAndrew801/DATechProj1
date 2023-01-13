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
                        try:
                            choosy = input("Do you want to play again?(Y/N)   ").upper()
                            if choosy == 'Y':
                                playing = True
                            elif choosy == 'N':
                                print("-------------------------------------")
                                print("Your games will be recorded.")
                                playing = False
                            else:
                                raise ValueError('That selection is invalid. Only Y or N is accepted.')
                        except ValueError as err:
                            print(err)
                if choice == 'B':
                    try:
                        if self.games:
                            print(f"""
Number of games played: {self.count}
Average of guesses: {statistics.mean(self.games)}                
Mean of guesses:{statistics.mean(self.games)}
Median of guesses:{statistics.median(self.games)}""")
                        else:
                            raise ValueError("Games must be played to make data for stats.")
                    except ValueError as err:
                        print(err)
                if choice =="C":
                    print("""You have chosen to TERMINATE yourself.
Your existence has ended.
-------------------------------------""")
                    self.existing = False
                else:
                    raise Exception('You must choose A, B, or C. Nothing else is valid.')
            except Exception as err:
                print(err)

def begin_life():
    name = input('What is your name?   ').title()
    print("-------------------------------------")
    print(f"{name} you have been spoken into existence!!!!")
    player = Player(name)
    return player.menu()
if __name__ == '__main__':
    begin_life()