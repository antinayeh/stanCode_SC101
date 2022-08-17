"""
File: bouncing ball
Name: Antina Yeh
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)


def bounce(event):
    global count

    vy = GRAVITY

    if ball.x == START_X and ball.y == START_Y:
        count += 1
        if count > 3:
            return

        while ball.x <= window.width:
            vy += GRAVITY
            ball.move(VX, vy)

            if ball.y >= window.height:
                vy = vy * REDUCE
                while vy > 1:
                    ball.move(VX, -vy)
                    vy -= GRAVITY
                    pause(DELAY)
            pause(DELAY)

        ball.x = START_X
        ball.y = START_Y




if __name__ == "__main__":
    main()
