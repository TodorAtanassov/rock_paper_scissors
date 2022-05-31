import random

# rock, paper, scissors = [Choices]
play = True
c_score = 0
u_score = 0
choices = ['r', 'p', 's']


u_choice = input('''type "R" for Rock,
     "P" for Paper,
     "S" for scissors and
     "Stop" to end the game. \n''').lower()
while play:
    c_choice = random.choice(choices)
    u_choice = input('>')
    if u_choice == 'r' and c_choice == 'r':
        print(f'''You:Rock -- AI: Rock
                DRAW
                You:{u_score} --- AI:{c_score}''')
    elif u_choice == 's' and c_choice == 's':
        print(f'''You:Scissors -- AI: Scissors
                    DRAW
                     You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'p' and c_choice == 'p':
        print(f'''You:Paper -- AI: Paper
                 DRAW
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'r' and c_choice == 'p':
        c_score += 1
        print(f'''You: Rock -- AI: Paper
                 AI WINS
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 's' and c_choice == 'r':
        c_score += 1
        print(f'''You: Scissors -- AI: Rock
                 AI WINS
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'p' and c_choice == 's':
        c_score += 1
        print(f'''You: Paper -- AI: Scissors
                 AI WINS
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 's' and c_choice == 'p':
        u_score += 1
        print(f'''You: Scissors -- AI: Paper
                 YOU WIN
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'p' and c_choice == 'r':
        u_score += 1
        print(f'''You: Paper -- AI: Rock
                 YOU WIN
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'r' and c_choice == 's':
        u_score += 1
        print(f'''You: Rock -- AI: Scissors
                 YOU WIN
                  You:{u_score} --- AI:{c_score}''')
    if u_choice == 'stop':
        break
        print('Game is terminated!')
    if c_score == 3 or u_score == 3:
        break
print(f'Result: YOU({u_score}) -- ({c_score})')
