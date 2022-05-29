import random

# rock, paper, scissors = [Choices]
play = True
c_score = 0
h_score = 0
choices = ['R', 'P', 'S']
c_choice = random.choice(choices)
while play:
    h_choice = input('''type "R" for Rock,
     "P" for Paper,
     "S" for scissors and
     "Stop" to end the game. \n''').lower()
    if c_choice == 'stop':
        play = False
        print('Game is terminated!')
    elif c_choice == 'R' and h_choice == 'r':
        print(f'''You:Rock -- AI: Rock
            DRAW
            You:{h_score} --- AI:{c_score}''')
    elif c_choice == 'S' and h_choice == 's':
        print('''You:Scissors -- AI: Scissors
                DRAW''')
    elif c_choice == 'P' and h_choice == 'p':
        print('''You:Paper -- AI: Paper
             DRAW''')
