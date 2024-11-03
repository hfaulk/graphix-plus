"""
graphix_plus.py - An extension to graphix.py that adds general QoL features

This library extends the functionality of the graphix library to make it easier and more intuitive to use.

INSTALLATION:
Add to project directory along with main graphix.py library
"""

__version__ = "0.1"
__author__ = "Harry Faulkner"

#Imports
from graphix import GraphixObject, Window, Text, Point

#Classes
class Group:
    """
    A class that adds object grouping functionality to execute functions on multiple objects in one statement.

    Attributes
    -----
        group_id : str
            Identifier for instantiated group, blank by default

    Methods
    -----
        add(item):
            Adds parsed item/s to group. 'item' can be either single GraphixObject, or list of GraphixObjects.
        remove(item):
            Removes parsed item from group. 'item' can only be a singular GraphixObject.
        draw(window):
            Iterates over each item in group and draws to parsed window. 'window' must be graphix Window object.
        undraw():
            Iterates over each item in group and undraws from screen.
        move(dx, dy):
            Moves all objects in group by same vector.
        get_items():
            Returns list of every item in group.
        get_id():
            Returns string of 'group_id'.
    """
    def __init__(self, *, group_id:str=""):
        self.id = group_id
        self.items = []

    def add(self, item:GraphixObject or list) -> None:
        """
        Adds parsed item/s to group. 'item' can be either single GraphixObject, or list of GraphixObjects.

        Parameters
        -----
        item : GraphixObject or list
            Object or list of objects that is to be added to group

        Returns
        -----
        None

        See Also
        -----
        None
        """
        if isinstance(item, GraphixObject):
            self.items.append(item)
        elif isinstance(item, list):
            for given_item in item:
                if isinstance(given_item, GraphixObject):
                    self.items.append(given_item)
                else:
                    raise Exception(f"Provided item '{given_item}' is not of type {GraphixObject}")
        else:
            raise Exception(f"Provided item '{item}' is not one of type [{GraphixObject}, {list}]")

    def remove(self, item:GraphixObject) -> None:
        """
        Removes parsed item from group. 'item' can only be a singular GraphixObject.

        Parameters
        -----
        item : GraphixObject
            Object that is to be removed from group

        Returns
        -----
        None

        See Also
        -----
        None
        """
        self.items.remove(item)

    def draw(self, window:Window) -> None:
        """
        Iterates over each item in group and draws to parsed window. 'window' must be graphix Window object.

        Parameters
        -----
        window : Window
            Window object that the group is to be drawn onto

        Returns
        -----
        None

        See Also
        -----
        None
        """
        for item in self.items:
            item.draw(window)

    def undraw(self) -> None:
        """
        Iterates over each item in group and undraws from screen.

        Parameters
        -----
        None

        Returns
        -----
        None

        See Also
        -----
        None
        """
        for item in self.items:
            item.undraw()

    def move(self, dx:int, dy:int) -> None:
        """
        Moves all objects in group by same vector.

        Parameters
        -----
        dx : int
            Amount each object should be moved in x-direction
        dy : int
            Amount each object should be moved in y-direction

        Returns
        -----
        None

        See Also
        -----
        None
        """
        for item in self.items:
            item.move(dx, dy)

    def get_items(self) -> list:
        """
        Returns list of every item in group.

        Parameters
        -----
        None

        Returns
        -----
        List

        See Also
        -----
        None
        """
        return self.items

    def get_id(self) -> str:
        """
        Returns string of 'group_id'.

        Parameters
        -----
        None

        Returns
        -----
        String

        See Also
        -----
        None
        """
        return self.id

class DebugOverlay:
    """
    A class that freezes functionality of window and adds ability to click anywhere on screen
    and be shown the coordinates for that specific point.

    Attributes
    -----
        window : Window
            Window to add the overlay to.

    Methods
    -----
        enable():
            Draws overlay to window and stops functionality of window until removed.
    """
    def __init__(self, window):
        self.window = window
        self.win_height = self.window.height
        self.win_width = self.window.width

    def enable(self) -> None:
        """
        Draws overlay to window and stops functionality of window until removed.
        Can only be removed by removing in code.

        Parameters
        -----
        None

        Returns
        -----
        None

        See Also
        -----
        None
        """
        overlay_items = Group()
        debug_text = Text(Point(75, 20), "DEBUG ENABLED")
        coord_text = Text(Point(self.win_width - 45, 20), "()")

        overlay_items.add([debug_text, coord_text])
        overlay_items.draw(self.window)

        while True:
            mouse_coords = self.window.get_mouse()
            coord_text.text = f"({mouse_coords.x}, {mouse_coords.y})"

#General Functions
def full_fill(item: GraphixObject, colour:str) -> None:
    """
    Fills same colour for both inside and outline of given object.

    Parameters
    -----
    item : GraphixObject
        Item to colour fill

    Returns
    -----
    None

    See Also
    -----
    None
    """
    item.fill_colour = colour
    item.outline_colour = colour

def relative_point(ref_item:GraphixObject, dx:int, dy:int) -> Point:
    """
    Takes centre of parsed reference object as (0,0) and gives new point dx,dy away from that centre.

    Parameters
    -----
    ref_item : GraphixObject
        Object whose centre acts as 0,0 for the new point
    dx : int
        Difference in x-direction from centre of reference object
    dy: int
        Difference in y-direction from centre of reference object

    Returns
    -----
    Point

    See Also
    -----
    None
    """
    ref_centre = ref_item.get_centre()
    new_x = ref_centre.x + dx
    new_y = ref_centre.y + dy
    new_point = Point(new_x, new_y)

    return new_point