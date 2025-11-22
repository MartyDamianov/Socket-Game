from os import path
import pygame
pygame.init()

class label:
    def __init__(self, x, y, color, text, size):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.size = size
        self.font = pygame.font.Font(path.realpath("Pixelated font.ttf"), self.size)
       
    def draw(self, window):
        self.rendered = self.font.render(str(self.text), True, self.color)
        window.blit(self.rendered, (self.x, self.y))

    def get_size(self):
        return self.font.render(str(self.text), True, self.color).get_rect().size        

def error():
    import tkinter as tk
    
    window = tk.Tk()
    window.title("Networking demo")
    window.geometry("400x400")
    window.configure(background = "#0000ff")
    
    label = tk.Label(window, text = "Something went wrong with the\nnewtworking\n\n\n\n\n\n\n\n\n\n\nIf you want help troubleshooting please\ncall me at 425-370-5531\nor contact me at\nmartindamianov@gmail.com", foreground = "#ffffff", background = "#0000ff", font=('Comic Sans', 15, 'bold'))
    label.pack()
    
    tk.mainloop()
