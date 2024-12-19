# program 1: Comma Code

spam = ['apples', 'bananas', 'tofu', 'cats']


def list_to_string(lst: list):
    string = ''
    for item in lst:
        string = string + item + ', '
    return string


print(list_to_string(spam))

# program 2: Coin Flip Streaks
import random


def coin_flip():
    number_of_streaks = 0
    list_of_all_flips = []

    for experiment_number in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        flips = ''
        for _ in range(0, 100):
            random_flip = random.randint(0, 1)
            if random_flip == 1:
                flips = flips + "H"
            else:
                flips = flips + "T"

        # print(len(list_of_flips))
        list_of_all_flips.append(flips)
        print(f"Experiment {experiment_number} completed.")

    print(len(list_of_all_flips))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for item in list_of_all_flips:
        if "HHHHHH" in item or "TTTTTT" in item:
            number_of_streaks += 1
    print('Chance of streak: %s%%' % (number_of_streaks / 100))


coin_flip()

# program 3: Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = len(grid)
y = len(grid[0])


def character_picture_grid():
    for j in range(y):
        for i in range(x):
            print(grid[i][j], end="")
        print()


character_picture_grid()
