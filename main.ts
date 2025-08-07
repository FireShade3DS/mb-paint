// This code was my attempt at learning 2d arrays. Use A+B to switch from display mode to draw mode, where you can press B to cycle the 4 colors and press A to move to the next cell.
function drawCursor () {
    if (mode) {
        led.plotBrightness(cursor_x, cursor_y, lookup(cursorColor))
        basic.pause(50)
        led.plotBrightness(cursor_x, cursor_y, 0)
        basic.pause(50)
    }
}
input.onButtonPressed(Button.A, function () {
    let row: number;
let col: number;
if (mode) {
        row = 0
        col = 0
        render = true
        finalizeEdit()
        cursorColor = 1
        moveCursor()
        render = false
    }
})
input.onButtonPressed(Button.AB, function () {
    if (!(render)) {
        render = true
        led.setBrightness(255)
        cursorColor = 1
        cursor_x = 0
        cursor_y = 0
        game.addScore(0)
        mode = 1 - mode
        render = false
        basic.pause(400)
    }
})
function lookup (input2: number) {
    if (input2 == 0) {
        return 0
    } else if (input2 == 1) {
        return 10
    } else if (input2 == 2) {
        return 70
    } else if (input2 == 3) {
        return 200
    } else {
        return 0
    }
}
input.onButtonPressed(Button.B, function () {
    if (mode) {
        render = true
        changeColor()
        render = false
    }
})
function finalizeEdit () {
    screen_array[cursor_y][cursor_x] = cursorColor
}
function moveCursor () {
    cursor_x += 1
    if (cursor_x > 4) {
        cursor_x = 0
        cursor_y += 1
        if (cursor_y > 4) {
            cursor_y = 0
        }
    }
}
function changeColor () {
    cursorColor = (cursorColor + 1) % 4
}
let pixel = 0
let render = false
let cursorColor = 0
let cursor_y = 0
let cursor_x = 0
let mode = 0
let screen_array: number[][] = []
game.addScore(0)
screen_array = [
[
0,
0,
0,
0,
0
],
[
0,
0,
0,
0,
0
],
[
0,
0,
0,
0,
0
],
[
0,
0,
0,
0,
0
],
[
0,
0,
0,
0,
0
]
]
basic.forever(function () {
    // the rendering code breaks on the simulator, but it does work IRL!
    if (!(render)) {
        for (let row2 = 0; row2 <= 4; row2++) {
            for (let col2 = 0; col2 <= 4; col2++) {
                pixel = screen_array[col2][row2]
                led.plotBrightness(row2, col2, lookup(pixel))
            }
        }
    }
    drawCursor()
})
