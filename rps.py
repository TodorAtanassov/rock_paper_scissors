import random

# rock, paper, scissors = [Choices]
c_score = 0
h_score = 0
choices = ['R', 'P', 'S']
c_choice = random.choice(choices)
h_choice = input('''type "R for Rock",
     "P for Paper" and
     "S for scissors"\n''').lower()

if c_choice == 'R' and h_choice == 'r':
    print(f'''You:Rock -- AI: Rock
        DRAW
        You:{h_score} --- AI:{c_score}''')
if c_choice == 'S' and h_choice == 's':
    print('''You:Scissors -- AI: Scissors
            DRAW''')
if c_choice == 'P' and h_choice == 'p':
    print('''You:Paper -- AI: Paper
         DRAW''')
