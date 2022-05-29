import random

# rock, paper, scissors = [Choices]
play = True
c_score = 0
u_score = 0
choices = ['R', 'P', 'S']
c_choice = random.choice(choices)
while play:
    u_choice = input('''type "R" for Rock,
     "P" for Paper,
     "S" for scissors and
     "Stop" to end the game. \n''').lower()
    if u_choice == 'stop':
        break
print('Game is terminated!')
if c_choice == 'R' and u_choice == 'r':
    print(f'''You:Rock -- AI: Rock
            DRAW
            You:{u_score} --- AI:{c_score}''')
elif c_choice == 'S' and u_choice == 's':
    print('''You:Scissors -- AI: Scissors
                DRAW''')
elif c_choice == 'P' and u_choice == 'p':
    print('''You:Paper -- AI: Paper
             DRAW''')
