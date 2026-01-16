import random

grid = []

num = 1

print('')

try:

    amount = int(input('Grid size: '))

    print('')

    xCoords = []

    num = 0

    for each in range(amount):

        xCoords.append(num)

        num += 1

    for each in range(amount):

        gridRow = []

        for each in range(amount):

            gridRow.append('')

            num += 1

        grid.append(gridRow)

    randomCoordY = random.randint(0,amount-1)

    randomCoordX = random.randint(0,amount-1)

    while not grid[randomCoordY][randomCoordX] == 'X':

        try:

            num = 0

            for each in range(amount):

                print(amount-num-1,grid[num])

                num += 1

            print(' ',xCoords)

            print('')

            guessX = int(input('Coordinate X: '))

            print('')

            guessY = int(input('Coordinate Y: '))

            grid[amount-guessY-1][guessX] = 'X'

        except:

            print('')

            print('Error.')

            print('')

    print('')

    print('Hit! You win!')

    print('')

except:

    print('')

    print('Error. Please Try again, and make sure to use numbers.')

    print('')