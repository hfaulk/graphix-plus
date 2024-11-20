from graphix import Window, Point, Circle, Rectangle
import graphix_plus

def main():
    win = Window("Testing", 800, 734)

    group_1 = graphix_plus.Group(group_id = "Group 1")

    circ = Circle(Point(200,210), 50)
    graphix_plus.full_fill(circ, "green")
    circ.draw(win)
    group_1.add(circ)

    circ2 = Circle(graphix_plus.relative_point(circ, 50, 50), 20)
    graphix_plus.full_fill(circ2, "red")
    circ2.draw(win)
    group_1.add(circ2)

    for i in range(2):
        win.get_mouse()
        group_1.move(100, 0)

    graphix_plus.draw_rect(win, Point(100, 100), Point(200, 200), "red", "black", outline_width=10)

    win.get_mouse()
    mouse_coords = graphix_plus.queryMousePosition(win)
    print(mouse_coords, win.get_mouse())
    graphix_plus.draw_circ(win, Point(mouse_coords["x"], mouse_coords["y"]), 50, "blue", "black")

    win.get_mouse()
    win.close()

if __name__ == "__main__":
    main()