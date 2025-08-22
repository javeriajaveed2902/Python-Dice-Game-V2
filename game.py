import numpy as np
import time
import sys

print('--- Welcome to Dice Rolling Game ---')
print('\n')
print('--- You have 3 chances to guess the correct number between 1 and 6 ---')


chances = 3
for i in range(chances):
    player_num = int(input(f"Chance {i + 1} Enter your number between 1 & 6 :"))

    print("--- Rolling the Dice ---")

    for _ in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(50)
    print()

    random_num = np.random.randint(1,7)

    print(f"Dice Shows: {random_num}")

    if player_num == random_num:
        print("Congratulations ! apsy barra koi juaari nhi hea !!")
        break
    else:
        print("Tumsei na ho payega...")
else:
    print('Sorry you lost your chances !')

