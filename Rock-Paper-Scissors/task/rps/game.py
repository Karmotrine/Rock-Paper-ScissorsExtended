# Rock-Paper-Scissors (Extended)
# 05.03.2021 - Yuan Ureña
# Jetbrains Academy
import random


class GameEngine:
    def __init__(self):
        self.default_options = ["rock", "paper", "scissors"]
        self.options = list()

    def mode_select(self):
        options = input("Enter your custom options: (Press [ENTER] to select RPS Classic)\n")
        if options == '':
            self.options.extend(self.default_options)
        else:
            self.options.extend(options.split(','))

    def win_algo(self, user):
        comp = random.choice(self.options)
        detect_winner = self.options[self.options.index(user) + 1:] + self.options[:self.options.index(user)]
        if user == comp:
            print(f'There is a draw ({comp})')
            return 0
        elif comp in detect_winner[:int(len(detect_winner) / 2)]:
            print(f'Sorry, but the computer chose {comp}')
            return -1
        else:
            print(f'Well done. The computer chose {comp} and failed')
            return 1


class ScoreBoard:
    def __init__(self):
        self.scorelist = []
        self.scorelist_dict = {}

    def display_rating(self):
        f = open("rating.txt", 'w', )
        for key, value in self.scorelist_dict.items():
            print(f'{key} {value}', file=f, flush=True)
        f.close()

    def update_ratingfile(self,u_name):
        with open("rating.txt","r") as rating_line:
            lines = rating_line.readlines()
        with open("rating.txt","w") as rating_line:
            for line in lines:
                if line.startswith(u_name):
                    print(u_name, self.scorelist_dict[u_name], sep=" ", end='\n', file=rating_line)
                else:
                    print(line, end='',file=rating_line)
        rating_line.close()

    def read_ratingfile(self):
        with open("rating.txt", "r+") as f:
            self.scorelist = f.readlines()
        f.close()
        self.scorelist = [i.strip("\n") for i in self.scorelist]
        for i in self.scorelist:
            self.scorelist_dict[i.split(' ')[0]] = int(i.split(' ')[1])

    def login_fetch_rating(self, u_name):
        if u_name not in self.scorelist_dict.keys():
            self.scorelist_dict[u_name] = 0


score_board = ScoreBoard()
game_engine = GameEngine()

user_name = input()
print(f'Hello, {user_name}!')

game_engine.mode_select()

print("Okay, let's start")
score_board.read_ratingfile()
score_board.login_fetch_rating(user_name)

while True:
    command = input()
    if command == "!exit":
        score_board.update_ratingfile(user_name)
        print("Bye!")
        break
    elif command == "!rating":
        print(f"Your rating: {score_board.scorelist_dict[user_name]}")
    elif command not in game_engine.options:
        print("Invalid Output")
    else:
        verdict = game_engine.win_algo(command)
        if verdict == 0:
            score_board.scorelist_dict[user_name] += 50
        elif verdict == 1:
            score_board.scorelist_dict[user_name] += 100

