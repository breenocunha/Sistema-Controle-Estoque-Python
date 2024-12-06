from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import tkinter.ttk as ttk
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        blank_space = " "
        self.root.title(110 * blank_space + "Sistema de Gerenciamento e Faturamento | Desenvolvido por B1•INFORMÁTICA")
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.config(bg = "Teal")

        #Todas Variavéis
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()

        #Buscar Frame
        SearchFrame = LabelFrame(self.root, text="Pesquisar Funcionários", font=("goudy old style", 15), bg="Teal", fg="White")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        #Opções
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER, font=("goudy old style", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="White", bd=3).place(x=200, y=10, width=230)
        btn_search = Button(SearchFrame, text="Pesquisar", font=("goudy old style", 15, "bold"), bg="Green", fg="White", cursor="hand2").place(x=440, y=10, width=150, height=30)

        #Titulo
        title = Label(self.root, text="Detalhes do Funcionário", font=("goudy old style", 15, "bold"), bg="peru", fg="White", bd=3).place(x=50, y=100, width=1000)

        #Content
        #Linha 1
        lbl_empid = Label(self.root, text="Emp ID", font=("goudy old style", 14), bg="Teal", fg="White").place(x=50, y=150)
        lbl_gender = Label(self.root, text="Sexo", font=("goudy old style", 14), bg="Teal", fg="White").place(x=370, y=150)
        lbl_contact = Label(self.root, text="Contato", font=("goudy old style", 14), bg="Teal", fg="White").place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("ARIEL", 14)).place(x=150, y=150, width=180)

        #Alterando os Valores no ComboBox
        cmb_search = ttk.Combobox(
            SearchFrame,
            textvariable=self.var_searchby,
            values=("Selecione", "Email", "Nome", "Contato"),
            state='readonly',
            justify=CENTER,
            font=("goudy old style", 12)
        )
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        #Mapeando valores do ComboBox para nomes das colunas do banco de dados
        self.search_map = {
            "Email": "Email",
            "Nome": "Name",
            "Contato": "Contact"
        }

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("ARIEL", 14), bg="White").place(x=850, y=150, width=180)

        #Linha 2
        lbl_name = Label(self.root, text="Nome", font=("goudy old style", 14), bg="Teal", fg="White").place(x=50, y=190)
        lbl_dob = Label(self.root, text="D. Nasc", font=("goudy old style", 14), bg="Teal", fg="White").place(x=370, y=190)
        lbl_doj = Label(self.root, text="D. Emp", font=("goudy old style", 14), bg="Teal", fg="White").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("ARIEL", 14), bg="White").place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("ARIEL", 14), bg="White").place(x=450, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("ARIEL", 14), bg="White").place(x=850, y=190, width=180)
        txt_gender = Entry(self.root, textvariable=self.var_gender, font=("ARIEL", 14), bg="White").place(x=450, y=150, width=180)

        #Linha3
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 14), bg="Teal", fg="White").place(x=50, y=230)
        lbl_pass = Label(self.root, text="Senha", font=("goudy old style", 14), bg="Teal", fg="White").place(x=370, y=230)
        lbl_utype = Label(self.root, text="Usuário", font=("goudy old style", 14), bg="Teal", fg="White").place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("ARIEL", 14), bg="White").place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("ARIEL", 14), bg="White").place(x=450, y=230, width=180)

        cmb_utype = ttk.Combobox(
            self.root, textvariable=self.var_utype,
            values=("Admin", "Funcionário"),
            state='readonly',
            justify=CENTER,
            font=("goudy old style", 12)
        )
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        self.cmb_utype = {
            "Admin": "Admin",
            "Funcionário": "Employee"
        }

        #Linha 4
        lbl_address = Label(self.root, text="Endereço", font=("goudy old style", 14), bg="Teal", fg="White").place(x=50, y=270)

        self.txt_address = Text(self.root, font=("ARIEL", 14), bg="White")
        self.txt_address.place(x=150, y=280, width=300, height=60)

        #Botão
        btn_add = Button(self.root, text="Salvar", command=self.add, font=("goudy old style", 15), bg="#722F37", fg="White", bd=0, cursor="hand2").place(x=490, y=320, width=120, height=30)
        btn_add = Button(self.root, text="Atualizar", font=("goudy old style", 15), bg="#722F37", fg="White", bd=0, cursor="hand2").place(x=635, y=320, width=120, height=30)
        btn_add = Button(self.root, text="Deletar", font=("goudy old style", 15), bg="#722F37", fg="White", bd=0, cursor="hand2").place(x=780, y=320, width=120, height=30)
        btn_add = Button(self.root, text="Limpar", font=("goudy old style", 15), bg="#722F37", fg="White", bd=0, cursor="hand2").place(x=925, y=320, width=120, height=30)

        #Employee Detalhes
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=380, relwidth=1, width=120)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview) #Horizontal ScrollBar
        scrolly.config(command=self.EmployeeTable.yview) #Vertical ScrollBar

        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Nome")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Sexo")
        self.EmployeeTable.heading("contact", text="Contato")
        self.EmployeeTable.heading("dob", text="Data Nasc")
        self.EmployeeTable.heading("doj", text="Data Contrato")
        self.EmployeeTable.heading("pass", text="Senha")
        self.EmployeeTable.heading("utype", text="Tipo User")
        self.EmployeeTable.heading("address", text="Endereço")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r'tbs.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Erro","ID do Funcionário necessária", parent=self.root)
            else:
                cur.execute("Select * from employee id where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Erro", "Este ID de Funcionário já foi atribuído, tente um ID diferente", parent=self.root)
                else:
                    cur.execute("Insert into employee (eid, name, email, gender, contact, dob, doj, pass, utype, address) values(?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),

                                        self.var_dob.get(),
                                        self.var_doj.get(),

                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro devido a : {str(ex)} ", parent=self.root)
    def show(self):
        con = sqlite3.connect(database=r'tbs.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Erro",f"Erro devido a: {str(ex)} ", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['Values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, row[9])



if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()