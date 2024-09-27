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