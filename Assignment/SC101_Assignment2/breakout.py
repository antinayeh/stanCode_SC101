"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        ball = graphics.ball

        if ball.x <= 0 or ball.x + ball.width > graphics.window.width:
            graphics.set_dx(-dx)
        if ball.y <= 0:
            graphics.set_dy(-dy)
        if ball.y + ball.height > graphics.window.height:
            ball.x = (graphics.window.width - ball.width)/2
            ball.y = (graphics.window.height - ball.height)/2
            graphics.set_dx(0)
            graphics.set_dy(0)
            lives -= 1

        if not graphics.get_object(ball.x, ball.y):
            if not graphics.get_object(ball.x + ball.width, ball.y):
                if not graphics.get_object(ball.x, ball.y + ball.width):
                    graphics.get_object(ball.x + ball.width, ball.y + ball.width)

        if graphics.get_score() == graphics.get_num_bricks() or lives == 0:
            graphics.window.remove(ball)
            graphics.window.remove(graphics.paddle)
            if graphics.get_score() == graphics.get_num_bricks():
                graphics.label.text = "You Win! Your score is: " + str(graphics.get_score())
            else:
                graphics.label.text = "You Lose! Your score is: " + str(graphics.get_score())
            graphics.label.x = (graphics.window.width - graphics.label.width) / 2
            graphics.label.y = (graphics.window.height - graphics.label.height) / 2
            break





if __name__ == "__main__" :
    main()