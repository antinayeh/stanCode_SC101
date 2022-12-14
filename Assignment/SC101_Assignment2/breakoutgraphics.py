"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10         # Number of rows of bricks
BRICK_COLS = 10       # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

BRICK_COLOR_LIST = ['Red', 'Orange', 'Yellow', 'Green', 'Blue']  # List of colors for the bricks


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a score label
        self.__score = 0
        self.label = GLabel(label='Score: ' + str(self.__score))
        self.label.font = '-20'
        self.window.add(self.label, x=0, y=window_height - self.label.height)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width)/2, y=self.window.height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.mouse_clicked)
        onmousemoved(self.mouse_moved)

        # Draw bricks
        brick_x = 0
        brick_y = brick_offset
        for c in range(brick_rows):
            for r in range(brick_cols):
                while brick_x + brick_width <= self.window.width:
                    brick = GRect(brick_width, brick_height)
                    color = self.brick_color(c)
                    brick.filled = True
                    brick.fill_color = color
                    brick.color = color

                    self.window.add(brick, x=brick_x, y=brick_y)
                    brick_x += brick_width + brick_spacing
            brick_x = 0
            brick_y += brick_height + brick_spacing

    def mouse_clicked(self, event):
        if self.__dx == self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def mouse_moved(self, event):
        x = event.x - PADDLE_WIDTH
        if 0 <= x <= self.window.width - PADDLE_WIDTH:
            self.paddle.x = x
        elif x < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - PADDLE_WIDTH

    # Getter
    def get_dx(self):
        return self.__dx

    # Getter
    def get_dy(self):
        return self.__dy

    # Setter
    def set_dx(self, dx):
        self.__dx = dx

    # Setter
    def set_dy(self, dy):
        self.__dy = dy

    # Getter
    def get_num_bricks(self):
        return BRICK_ROWS * BRICK_COLS

    def get_score(self):
        return self.__score

    def get_object(self, x, y):
        """
        :param x: x coordinate of ball
        :param y: y coordinate of ball
        :return:  true if the ball hit paddle or brick
        """
        ob = self.window.get_object_at(x, y)
        collision = False

        if ob == self.label or ob is None:
            return collision
        else:
            self.__dy = - self.__dy
            collision = True
            if ob != self.paddle:
                self.window.remove(ob)
                self.__score += 1
                self.label.text = 'Score: ' + str(self.__score)
        return collision


    def brick_color(self, row):
        """
        :param row: the current row for building bricks
        :return: the color for the bricks
        """
        num_colors = len(BRICK_COLOR_LIST)  # number of colors in the color list
        row_color_counter = BRICK_ROWS // num_colors  # number of rows for each color, keep track of what color to use
        color_code = 0  # index to get the right color in the list

        while True:
            if row < row_color_counter:
                return BRICK_COLOR_LIST[color_code]
            color_code += 1  # move to next color
            row_color_counter = BRICK_ROWS // num_colors * (color_code + 1)















