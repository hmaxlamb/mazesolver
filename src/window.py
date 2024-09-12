import tkinter import TK, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = tkinter.TK()
        self.__root.title("Mazesolver") 
        self.__root.Canvas(self.__root, bg="white", height=height, width=width)
        self.__root.pack(fill="both", expand=True)
        self.__running = False
        




