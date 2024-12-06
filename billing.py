from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile

class billClass:
    def __init__(self, root):
        self.root = root
        self.width = 1510
        self.height = 710

        #Obter a largura e altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #Calcular a posição x e y para centralizar a jaela
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height// 2) - (self.height// 2)
        blank_space = " "
        self.root.title(110 * blank_space + "Sistema de Gerenciamento e Faturamento | Desenvolvido por B1•INFORMÁTICA")
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.config(bg="Teal")
        self.cart_list = []
        self.chk_print = 0


if __name__ == "__main__":
    root = Tk()
    obj = billClass(root)
    root.mainloop()