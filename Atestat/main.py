from turtle import *
from state import *
from check_win import is_win


def line(a, b, x, y):
    up()
    goto(a, b)
    down()
    goto(x, y)


def grid():
    Screen().bgcolor('light blue')
    for x in range(-150, 200, 50):
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()


turns = {'red': 'yellow', 'yellow': 'red'}
state = State()


def tap(x, y):
    player = state.player
    slots = state.slots
    grid = state.grid

    slot = int((x + 200) // 50)
    count = slots[slot]

    if count >= len(grid):
        print
        "No more space, try another slot"
        return

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()
    grid[len(grid) - count - 1][slot] = player
    last_played_cell = [len(grid) - count - 1, slot]
    if is_win(grid, player, last_played_cell, 4):
        print(str(player) + " wins")
        restart()
    slots[slot] = count + 1
    state.player = turns[player]


def restart():
    reset()
    hideturtle()
    grid()
    state.reset()
    Screen().onscreenclick(tap)
    done()


Screen().setup(420, 420, 370, 0)
hideturtle()
Screen().tracer(0, 0)
grid()
Screen().onscreenclick(tap)
done()