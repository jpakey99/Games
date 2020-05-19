import random


def choose_amount(nim, stack):
    max = nim[stack]
    if max == 1:
        return 1
    else:
        return random.randint(1, max)


def choose_stack(nim):
    length = len(nim) -1
    while True:
        rand = random.randint(0, length)
        if nim[rand] != 0:
            return rand


def game_over(nim):
    for stack in range(0,len(nim)):
        if nim[stack] != 0:
            return False
    return True


def play_game(nim):
    player1 = True
    game_playing = True

    while game_playing:
        print(nim)
        stack = choose_stack(nim)
        remove = choose_amount(nim, stack)
        nim[stack] = nim[stack] - remove
        if player1:
            print("player 2 turn")
            player1 = False
        else:
            print("player 1 turn")
            player1 = True
        game_playing = not game_over(nim)


def main():
    nim = []
    play_game(nim)


main()