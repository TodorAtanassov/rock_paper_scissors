import random

# rock, paper, scissors = [Choices]
play = True
c_score = 0
u_score = 0
choices = ['r', 'p', 's']
c_choice = random.choice(choices)
while play:
    u_choice = input('''type "R" for Rock,
     "P" for Paper,
     "S" for scissors and
     "Stop" to end the game. \n''').lower()
    if c_choice == 'stop':
        break
    print('Game is terminated!')
if u_choice == 'r' and c_choice == 'r':
    print(f'''You:Rock -- AI: Rock
            DRAW
            You:{u_score} --- AI:{c_score}''')
elif u_choice == 's' and c_choice == 's':
    print('''You:Scissors -- AI: Scissors
                DRAW''')
elif u_choice == 'p' and c_choice == 'p':
    print('''You:Paper -- AI: Paper
             DRAW''')
elif u_choice == 'r' and c_choice == 'p':
    c_score += 1
    print('''You: Rock -- AI: Paper
             AI WINS''')
elif u_choice == 's' and c_choice == 'r':
    c_score += 1
    print('''You: Scissors -- AI: Rock
             AI WINS''')
elif u_choice == 'p' and c_choice == 's':
    c_score += 1
    print('''You: Paper -- AI: Scissors
             AI WINS''')
elif u_choice == 's' and c_choice == 'p':
    u_score += 1
    print('''You: Scissors -- AI: Paper
             YOU WIN''')
elif u_choice == 'p' and c_choice == 'r':
    u_score += 1
    print('''You: Paper -- AI: Rock
             YOU WIN''')
elif u_choice == 'r' and c_choice == 's':
    u_score += 1
    print('''You: Rock -- AI: Scissors
             YOU WIN''')
