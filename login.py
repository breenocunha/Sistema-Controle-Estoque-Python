import customtkinter as ctk
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os





class Login_System:
    def __init__(self, root):
        self.root = root
        self.width = 1100
        self.height = 700

        # Obter a largura e altura de tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular a posição x e y para centralizar a janela
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        blank_space = " "
        self.root.title(110 * blank_space + "Sistema de Gerenciamento e Faturamento | Desenvolvido por B1•INFORMÁTICA")
        self.root.config(bg="Teal")
        

        #Login Frame
        self.employeeid = StringVar()
        self.password = StringVar()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=600, y=100, width=400, height=512.5)

        title = Label(login_frame, text="Login", font=("Elephant", 30, "bold"), bg="white").place(x=0, y=40, relwidth=1)
        
        self.usuario_image = ImageTk.PhotoImage(file="images/do-utilizador.png")
        self.lbl_Usuario_image = Label(self.root, image=self.usuario_image, bd=0).place(x=100, y=100)

        lbl_employeeid = Label(login_frame, text="Usuário",  font=("Andalus", 15), bg="white", fg="#722F37").place(x=70, y=110)

        txt_username = Entry(login_frame, textvariable=self.employeeid, font=("times new roman", 15), bg="#ECECEC").place(x=70, y=140, width=250)

        lbl_pass = Label(login_frame, text="Senha", font=("Andales", 15), bg="white", fg="#722F37").place(x=70, y=190)
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bg="#ECECEC").place(x=70, y=220, width=250)

        #Supondo que o login_frame já esteja definido em algum lugar do seu código

        #Carregar a imagem do Ícone
        icon_path = "images/do-utilizador.png"
        icon_photo = ImageTk.PhotoImage(file=icon_path)

        #Definir o botão com o Ícone
        btn_submit = ctk.CTkButton(login_frame, text="Entrar".upper(), command=self.login,
        bg_color="#FFF", fg_color="#000", font=("Arial Roundend MT Bold", 10), compound=LEFT, hover_color="#131", width=250, height=35).place(x=70, y=420)     
        
    def login(self):
        con= sqlite3.connect(database=r'tbs.db')
        cur= con.cursor()
        try:
            if self.employeeid.get() == "" or self.password.get() == "":
                messagebox.showerror("Erro", "Todos os campos são obrigatórios", parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?", (self.employeeid.get(), self.password.get()))
                user= cur.fetchone()
                if user == None:
                    messagebox.showerror("Erro", "Nome de Usuário ou Senha Invalida", parent=self.root)
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro devido a: {str(ex)}", parent=self.root)

root=Tk()
obj=Login_System(root)
root.mainloop()