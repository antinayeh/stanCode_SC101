"""
File: babygraphics.py
Name: Antina Yeh
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width = width - GRAPH_MARGIN_SIZE*2  # get the real width of the canvas
    year_width = width / len(YEARS)  # width between each year
    # year_index += 1  # modify year index
    x = int(year_width * year_index + GRAPH_MARGIN_SIZE)  # get x coordinate
    return x



def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    x1 = GRAPH_MARGIN_SIZE
    x2 = CANVAS_WIDTH - GRAPH_MARGIN_SIZE
    y_top = GRAPH_MARGIN_SIZE
    y_bottom = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    canvas.create_line(x1, y_top, x2,  y_top, width=LINE_WIDTH)  # top horizontal line
    canvas.create_line(x1, y_bottom, x2, y_bottom, width=LINE_WIDTH)  # bottom horizontal line

    y1 = 0
    y2 = CANVAS_HEIGHT
    for i in range(len(YEARS)):  # create vertical lines
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, y1, x, y2, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, y_bottom, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for n in range(len(lookup_names)):
        name = lookup_names[n]
        # loop over colors if more than 4 names
        if n > len(COLORS) - 1:
            n = n % len(COLORS)
        color = COLORS[n]
        # get list of ranking and its x,y coordinates
        data = get_data_points(name, name_data)
        # loop over the data list to get the rank, the current point, and the next point
        for i in range(len(data) - 1):
            rank = data[i][0]
            x = data[i][1]
            y = data[i][2]
            # next point, used to create line
            x2 = data[i+1][1]
            y2 = data[i+1][2]
            # check if no ranking ( > 1000)
            if y == CANVAS_HEIGHT-GRAPH_MARGIN_SIZE:
                label = name + " *"
            else:
                label = name + " " + str(rank)
            canvas.create_line(x, y, x2, y2, width=LINE_WIDTH, fill=color)
            canvas.create_text(x + TEXT_DX, y, text=label, anchor=tkinter.SW, fill=color)


def get_data_points(name, name_data):
    """
    Input:
        name (str): The name you want to get data for
        name_data (dict): Dictionary holding baby name data
    Returns:
        data (list): returns a list of lists that contain the ranking and its x, y coordinates
    """
    data = []
    height = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2  # true height of graph

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        year = str(YEARS[i])
        # check if this name has data for the year
        if year in name_data[name]:
            rank = name_data[name][year]
            y = int((height / MAX_RANK) * int(rank)) + GRAPH_MARGIN_SIZE
        # if no data for the year, set the rank to 0 and y coordinate to the bottom line
        else:
            rank = 0
            y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
        # append data for this year to the list
        data.append([rank, x, y])
    return data





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
