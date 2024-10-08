from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Mazesolver") 
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill="both", expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wati_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        
    def close(self):
        self.__running = False   

    def draw_line(self, line, fill_color):
        line.draw(self.canvas ,fill_color)

class Point:
    def __init__(self, xcord, ycord):
        self.x = xcord
        self.y = ycord

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)