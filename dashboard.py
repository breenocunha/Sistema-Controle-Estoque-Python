from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
# from employee import employeeClass
# from supplier import supplierClass
# from stock import stockClass
# from sales import salesClass
import sqlite3
import time
import os
from billing import billClass

class billClass:
    def __init__(self, root):
        self.root = root
        self.width = 1310
        self.height = 720

        #Obter a largura e altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #Calcular a posição x e y para centralizar a jaela
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height// 2) - (self.height// 2)
        blank_space = " "
        self.root.title(150 * blank_space + "Sistema de Gerenciamento e Faturamento | Desenvolvido por B1•INFORMÁTICA")
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.config(bg="Teal")


        self.icon_title = PhotoImage(file="images/mercearias.png")
        title = Label(self.root, text="MERCADINHO DA B1", image=self.icon_title, compound=LEFT, font=("ARIEL", 40, "bold"), bg="Teal", fg="White")
        title.place(x=50, y=18)

        btn_logout = Button(self.root, text="Sair", font=("ARIEL", 15, "bold"), bg="White", cursor="hand2").place(x=1200, y=40, width=100)

        self.lbl_clock = Label(self.root, text="Mercadinho da B1...!!\t\t Data: DD-MM-YYYY\t\t Time: HH:MM:SS")
        self.lbl_clock.place(x=0, y=120, relwidth=1, height=30)

        self.MenuLogo = PhotoImage(file="images/supermercado.png")

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="White")
        LeftMenu.place(x=0, y=150, width=230, height=570)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=Y)

        self.icon_side = PhotoImage(file="images/avanco.png")

        lbl_menu = Label(LeftMenu, text="Menu", font=("ARIEL", 15, "bold"), bg="#722F37", fg="White")
        lbl_menu.pack(side=TOP, fill=X)

        btn_employee = Button(LeftMenu, text="USUÁRIO", image=self.icon_side, compound=LEFT, padx=20, anchor="w", font=("ARIEL", 15)).place(x=12, y=20, width=200, height=50)
        btn_supplier = Button(LeftMenu, text="FORNECEDOR", image=self.icon_side, compound=LEFT, padx=20, anchor="w", font=("ARIEL", 12, "bold")).place(x=12, y=90, width=200, height=50)
        btn_stock = Button(LeftMenu, text="ESTOQUE", image=self.icon_side, compound=LEFT, padx=20, anchor="w", font=("ARIEL", 15)).place(x=12, y=320, width=200, height=50)
        btn_sales = Button(LeftMenu, text="VENDAS", image=self.icon_side, compound=LEFT, padx=20, anchor="w",font=("ARIEL", 15)).place(x=12, y=390, width=200, height=50)
        btn_billing = Button(LeftMenu, text="COBRANÇA", image=self.icon_side, compound=LEFT, padx=20, anchor="w", font=("ARIEL", 15)).place(x=12, y=460, width=200, height=50)

        self.lbl_employee = Label(self.root, text="FUNCIONÁRIOS\n[ 0 ]", relief=RIDGE, bg="Gray", fg="White", font=("goudy old style", 15, "bold"))
        self.lbl_employee.place(x=250, y=170, width=200, height=100)

        self.lbl_employee = Label(self.root, text="FORNECEDORES\n[ 0 ]", relief=RIDGE, bg="Gray", fg="White", font=("goudy old style", 15, "bold"))
        self.lbl_employee.place(x=600, y=170, width=200, height=100)

        self.lbl_employee = Label(self.root, text="VENDAS\n[ 0 ]", relief=RIDGE, bg="Gray", fg="White", font=("goudy old style", 15, "bold"))
        self.lbl_employee.place(x=250, y=350, width=200, height=100)

        self.lbl_employee = Label(self.root, text="ESTOQUE\n[ 0 ]", relief=RIDGE, bg="Gray", fg="White", font=("goudy old style", 15, "bold"))
        self.lbl_employee.place(x=600, y=350, width=200, height=100)


        lbl_footer = Label(self.root, text="Sistema de Gerenciamento e Faturamento de Supermercado | Desenvolvido por B1•INFORMÁTICA")
        lbl_footer.place(x=0, y=670, relwidth=1, height=50)

if __name__ == "__main__":
    root = Tk()
    obj = billClass(root)
    root.mainloop()