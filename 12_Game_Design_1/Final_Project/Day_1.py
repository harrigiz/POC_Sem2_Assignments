import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        lives = 3
        self.width = 600
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, bg="AAAAFF", width = self.width, height = self.height)
        self.canvas.pack()
        self.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("BREAKOUT")
    game = Game(root)
    root.mainloop()