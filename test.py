from graphix import Window, Point, Circle, Rectangle
import graphix_plus

def main():
    win = Window("Testing", 800, 734)

    group_1 = graphix_plus.Group(group_id = "Group 1")

    circ = Circle(Point(100,210), 50)
    graphix_plus.full_fill(circ, "green")
    circ.draw(win)
    group_1.add(circ)

    circ2 = Circle(graphix_plus.relative_point(circ, 50, 50), 20)
    graphix_plus.full_fill(circ2, "red")
    circ2.draw(win)
    group_1.add(circ2)

    debugger = graphix_plus.DebugOverlay(win)
    #debugger.enable()

    for i in range(2):
        win.get_mouse()
        group_1.move(100, 0)

    win.get_mouse()
    win.close()

if __name__ == "__main__":
    main()