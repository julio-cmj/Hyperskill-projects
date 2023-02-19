gride = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print("""---------
|       |
|       |
|       |
---------""")

win = 0
player = 'X'

while True:

    empty_space = True
    # x_count = 0
    # o_count = 0

    # Where to mark
    play = input()
    play = ([[n] for n in play.split()])

    # Mark checker
    try:
        c1 = int(play[0][0]) - 1
        c2 = int(play[1][0]) - 1
    except Exception():
        print('You should enter numbers!')
        continue
    if c1 > 2 or c2 > 2:
        print('Coordinates should be from 1 to 3!')
        continue
    if gride[c1][c2] != ' ':
        print('This cell is occupied! Choose another one!')
        continue

    # Put mark on the gride
    if player == 'X':
        gride[c1][c2] = 'X'
    elif player == 'O':
        gride[c1][c2] = 'O'

    # Diagonal win
    if gride[0][2] == gride[1][1] and gride[0][2] == gride[2][0] and gride[1][1] != ' ':
        winner = gride[0][2]
        win += 1
    if gride[0][0] == gride[1][1] and gride[0][0] == gride[2][2] and gride[0][0] != ' ':
        winner = gride[0][0]
        win += 1

    # horizontal win
    for n in range(0, 3):
        if gride[n][0] == gride[n][1] and gride[n][1] == gride[n][2] and gride[n][0] != ' ':
            winner = gride[n][0]
            win += 1

    # vertical win
    for n in range(0, 3):
        if gride[0][n] == gride[1][n] and gride[1][n] == gride[2][n] and gride[0][n] != ' ':
            winner = gride[0][n]
            win += 1

    # Check for empty space
    for line in gride:
        if ' ' in line:
            empty_space = False

    #   if 'X' in line:
    #       x_count += line.count('X')
    #   if 'O' in line:
    #       o_count += line.count('O')

    # New gride
    print('---------')
    for line in gride:
        print("|", ' '.join(line), "|")
    print('---------')

    # Change player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'

    # Check win,draw or next move
    if not empty_space and win == 0:
        continue
    elif win == 0:
        print('Draw')
        break
    else:
        print(f'{winner} wins')
        break

  # if win > 1:
  #     print("Impossible")
  #     break
  # elif (o_count - x_count >= 2) or (o_count - x_count <= -2):
  #     print('Impossible')
  #     break

    break
