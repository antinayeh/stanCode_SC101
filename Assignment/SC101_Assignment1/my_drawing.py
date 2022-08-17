"""
File: my_drawing.py
Name: Antina Yeh
----------------------
TODO: We use pycharm to code, so I thought I would draw the pycharm logo for the project.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine, GArc
from campy.graphics.gwindow import GWindow

LENGTH = 100

def main():
    """
    Title: pycharm logo
    We use pycharm to code, so I thought I would draw the pycharm logo for the project.
    """
    window = GWindow(width=500, height=500)

    green = GPolygon()
    green.add_vertex((230, 0))
    green.add_vertex((30, 80))
    green.add_vertex((0, 390))
    green.add_vertex((160, window.height))
    green.add_vertex((450, 150))
    green.filled = True
    green.color = 'mediumspringgreen'
    green.fill_color = 'mediumspringgreen'
    window.add(green)

    light_green = GPolygon()
    light_green.add_vertex((0, 390))
    light_green.add_vertex((380, 0))
    light_green.add_vertex((400, 210))
    light_green.add_vertex((160, window.height))
    light_green.filled = True
    light_green.color = 'palegreen'
    light_green.fill_color = 'palegreen'
    window.add(light_green)

    blue = GPolygon()
    blue.add_vertex((window.width, 180))
    blue.add_vertex((400, 110))
    blue.add_vertex((400, 450))
    blue.filled = True
    blue.color = 'turquoise'
    blue.fill_color = 'deepskyblue'
    window.add(blue)

    yellow = GPolygon()
    yellow.add_vertex((360, window.height))
    yellow.add_vertex((150, 450))
    yellow.add_vertex((180, 310))
    yellow.add_vertex((440, 205))
    yellow.add_vertex((window.width, 440))
    yellow.filled = True
    yellow.color = 'yellow'
    yellow.fill_color = 'yellow'
    window.add(yellow)





    box = GRect(window.width/1.6, window.height/1.6)
    box.filled = True
    window.add(box, x=(window.width-box.width)/2, y=(window.height-box.height)/2)

    line = GRect((box.width/2)*0.75, box.height/18)
    line.filled = True
    line.color = 'white'
    line.fill_color = 'white'
    window.add(line, x=box.x + box.width*0.1, y=box.y + box.height*0.80)

    pc = GLabel('PC')
    pc.color = 'white'
    pc.font = '-180-bold'
    pc_y = box.y + box.y + box.width - line.y - line.height + pc.height

    window.add(pc, x=line.x, y=pc_y)








if __name__ == '__main__':
    main()
