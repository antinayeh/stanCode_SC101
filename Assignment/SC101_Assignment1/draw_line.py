"""
File: draw_line
Name: Antina Yeh
-------------------------
TODO:
"""
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5

window = GWindow()
num_clicks = 0
first_point_x = 0
first_point_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    global num_clicks
    global first_point_x
    global first_point_y

    num_clicks += 1
    if num_clicks % 2 != 0:
        first_point_x = event.x
        first_point_y = event.y
        circle = GOval(SIZE, SIZE, x=event.x - SIZE/2, y=event.y - SIZE/2)
        window.add(circle)

    else:
        ob = window.get_object_at(first_point_x, first_point_y)
        window.remove(ob)

        second_point_x = event.x
        second_point_y = event.y
        line = GLine(first_point_x, first_point_y, second_point_x, second_point_y)
        window.add(line)


if __name__ == "__main__":
    main()
