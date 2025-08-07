"""

This code was my attempt at learning 2d arrays. Use A+B to switch from display mode to draw mode, where you can press B to cycle the 4 colors and press A to move to the next cell.

"""
def drawCursor():
    if mode:
        led.plot_brightness(cursor_x, cursor_y, lookup(cursorColor))
        basic.pause(50)
        led.plot_brightness(cursor_x, cursor_y, 0)
        basic.pause(50)

def on_button_pressed_a():
    global render, cursorColor
    if mode:
        row = 0
        col = 0
        render = True
        finalizeEdit()
        cursorColor = screen_array[col][row]
        moveCursor()
        render = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global render, cursorColor, cursor_x, cursor_y, mode
    if not (render):
        render = True
        led.set_brightness(255)
        cursorColor = 1
        cursor_x = 0
        cursor_y = 0
        game.add_score(0)
        mode = 1 - mode
        render = False
        basic.pause(400)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def lookup(input2: number):
    if input2 == 0:
        return 0
    elif input2 == 1:
        return 10
    elif input2 == 2:
        return 70
    elif input2 == 3:
        return 200
    else:
        return 0

def on_button_pressed_b():
    global render
    if mode:
        render = True
        changeColor()
        render = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def finalizeEdit():
    screen_array[cursor_y][cursor_x] = cursorColor
def moveCursor():
    global cursor_x, cursor_y
    cursor_x += 1
    if cursor_x > 4:
        cursor_x = 0
        cursor_y += 1
        if cursor_y > 4:
            cursor_y = 0
def changeColor():
    global cursorColor
    cursorColor = (cursorColor + 1) % 4
pixel = 0
render = False
mode = 0
cursorColor = 0
screen_array: List[List[number]] = []
cursor_x = 0
cursor_y = 0
temp = 0
cursor_y = 0
cursor_x = 0
screen_array = [[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
cursorColor = 3

def on_forever():
    global pixel
    # the rendering code breaks on the simulator, but it does work IRL!
    if not (render):
        for row2 in range(5):
            for col2 in range(5):
                pixel = screen_array[col2][row2]
                led.plot_brightness(row2, col2, lookup(pixel))
    drawCursor()
basic.forever(on_forever)
