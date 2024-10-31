"""
graphix_plus.py - An extension to graphix.py that adds general QoL features

This library extends the functionality of the graphix library to make it easier and more intuitive to use.

INSTALLATION:
Add to project directory along with main graphix.py library
"""

__version__ = "0.1"
__author__ = "Harry Faulkner"

#Imports
import graphix

#Classes
class Group:
    def __init__(self, *, group_id:str=""):
        self.id = group_id
        self.items = []

    def add(self, item:graphix.GraphixObject or list) -> None:
        if isinstance(item, graphix.GraphixObject):
            self.items.append(item)
        elif isinstance(item, list):
            for given_item in item:
                if isinstance(given_item, graphix.GraphixObject):
                    self.items.append(given_item)
                else:
                    raise Exception(f"Provided item '{given_item}' is not of type {graphix.GraphixObject}")
        else:
            raise Exception(f"Provided item '{item}' is not one of type [{graphix.GraphixObject}, {list}]")

    def remove(self, item:graphix.GraphixObject) -> None:
        self.items.remove(item)

    def draw(self, window:graphix.Window) -> None:
        for item in self.items:
            item.draw(window)

    def undraw(self):
        for item in self.items:
            item.undraw()

    def move(self, dx:int, dy:int) -> None:
        for item in self.items:
            item.move(dx, dy)

    def get_items(self) -> list:
        return self.items

    def get_id(self) -> str:
        return self.id

class DebugOverlay:
    def __init__(self, window):
        self.window = window
        self.win_height = self.window.height
        self.win_width = self.window.width

    def enable(self) -> None:
        overlay_items = Group()
        debug_text = graphix.Text(graphix.Point(75, 20), "DEBUG ENABLED")
        coord_text = graphix.Text(graphix.Point(self.win_width - 45, 20), "()")

        overlay_items.add([debug_text, coord_text])
        overlay_items.draw(self.window)

        while True:
            mouse_coords = self.window.get_mouse()
            coord_text.text = f"({mouse_coords.x}, {mouse_coords.y})"

#General Functions
def full_fill(item: graphix.GraphixObject, colour:str) -> None:
    item.fill_colour = colour
    item.outline_colour = colour

def relative_point(ref_item:graphix.GraphixObject, dx:int, dy:int) -> graphix.Point:
    ref_centre = ref_item.get_centre()
    new_x = ref_centre.x + dx
    new_y = ref_centre.y + dy
    new_point = graphix.Point(new_x, new_y)

    return new_point