import random as r
import os
import time

os.system('CLS')

options = {
    1: 'kamien',
    2: 'papier',
    3: 'nozyce',
    4: 'test',
    5: 'test2'
}
your_score = 0
comp_score = 0
while 0 == 0:
    print(f'Your score is {your_score}')
    print(f'Computer score is {comp_score}\n')

    comp_choice = options.get(r.randint(1, 3))
    your_choice = input("Kamien/papier/nozyce? : ").lower()

    print(f'Your choice: {your_choice}')
    time.sleep(1.5)
    print(f'Computer choice: {comp_choice}')
    time.sleep(1.5)

    if your_choice == 'kamien' and comp_choice == "nozyce":
        print("You won")
        time.sleep(1)
        os.system('CLS')
        your_score += 1
    elif your_choice == 'papier' and comp_choice == "kamien":
        print("You won")
        time.sleep(1)
        os.system('CLS')
        your_score += 1
    elif your_choice == 'nozyce' and comp_choice == "papier":
        print("You won")
        time.sleep(1)
        os.system('CLS')
        your_score += 1
    elif your_choice == comp_choice:
        print("Draw")
        time.sleep(1)
        os.system('CLS')
    else:
        print("You lost")
        time.sleep(1)
        os.system('CLS')
        comp_score += 1

