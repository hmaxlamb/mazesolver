from window import Window, Line, Point

def main():
    win = Window(800, 600)

    p1 = Point(43, 87)
    p2 = Point(641, 450)

    l1 = Line(p1, p2)

    win.draw_line(l1, "red")

    win.wati_for_close()


main()