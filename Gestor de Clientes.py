from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import conexion


class Ventana():

    def __init__(self):
        self.opcion = "True"
        self.cliente1 = conexion.Cliente()

        self.root = Tk()
        self.root.title("Gestor de Clientes")
        self.root.resizable(0,0) 
        self.ancho = 647
        self.largo = 450
        self.pantalla_ancho = self.root.winfo_screenwidth()
        self.pantalla_largo = self.root.winfo_screenheight()
        self.x = (self.pantalla_ancho / 2) - (self.ancho / 2)#Para que se ajuste al medio de la pantalla
        self.y = (self.pantalla_largo / 4) - (self.largo / 4)
        self.root.geometry("%dx%d+%d+%d" % (self.ancho,self.largo, self.x, self.y))
        self.root.iconbitmap("C:/Users/niko_/Desktop/Python/Gestor de Clientes/Libreta.ico")
        self.cargar_objetos()
        self.cargar_datos()
        self.root.mainloop()
        
          
    def cargar_objetos(self):

        self.frame = LabelFrame(self.root, padx=20)
        self.frame.grid(row=0, column=0, columnspan=3, sticky="nswe")

        self.btn_nuevo = Button(self.frame, text="Nuevo Cliente", bg="#ddd", font=('Calibri', 12,'bold'), command=self.cargar_objetos_top)
        self.btn_nuevo.grid(row = 0 , column=0, padx=20, pady=20, ipadx=30, sticky="nswe")

        self.btn_editar = Button(self.frame, text="Editar", bg="#ddd", font=('Calibri', 12,'bold'), command=self.cargar_datos_top)
        self.btn_editar.grid(row=0, column=1, padx=20, pady=20, ipadx=50, ipady=20, sticky="nswe")

        self.btn_eliminar = Button(self.frame, text="Eliminar Cliente", bg="#ddd", font=('Calibri', 12,'bold'), command=self.eliminar_cliente)
        self.btn_eliminar.grid(row=0, column=2, padx=20, pady=20, ipadx=20, ipady=20, sticky="nswe")

        self.frame_tree = LabelFrame(self.root, padx=20, pady=20)
        self.frame_tree.grid(row=1, column=0, sticky="nswe")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold'))
        self.tree = ttk.Treeview(self.frame_tree, style="mystyle.Treeview")
        self.tree['columns'] = ('Nombre', 'Telefono','Email', 'Empresa')

        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('Nombre', width=150)
        self.tree.column('Telefono', width=150)
        self.tree.column('Email', width=150)
        self.tree.column('Empresa', width=150)

        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Telefono", text="Telefono")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Empresa", text="Empresa")
        self.tree.grid(row=1, column=0, columnspan=4)

        self.scrollVert = Scrollbar(self.frame_tree,command=self.tree.yview)
        self.scrollVert.grid(row=1, column=4, sticky = "nsew")
        self.tree.config(yscrollcommand = self.scrollVert.set)


    def cargar_objetos_top(self):#Ventana emergente 
        
        self.top = Toplevel()
        self.top.title("Nuevo Cliente")
        self.ancho = 400
        self.largo = 180
        self.pantalla_ancho = self.root.winfo_screenwidth()
        self.pantalla_largo = self.root.winfo_screenheight()
        self.x = (self.pantalla_ancho / 2) - (self.ancho / 2)
        self.y = (self.pantalla_largo / 4) - (self.largo / 4)
        self.top.geometry("%dx%d+%d+%d" % (self.ancho,self.largo, self.x, self.y))
        self.top.iconbitmap("C:/Users/niko_/Desktop/Python/Gestor de Clientes/Libreta.ico")

        self.lb_nombre = Label(self.top, text="Nombre", font=('Calibri', 12,'bold'))
        self.caja_nombre = Entry(self.top, width=40, font=('Calibri', 12))
        self.lb_nombre.grid(row=0, column=0, pady=2, sticky='w')
        self.caja_nombre.grid(row=0, column=1)

        self.lb_telefono = Label(self.top, text="Telefono", font=('Calibri', 12,'bold'))
        self.caja_telefono = Entry(self.top, width=40, font=('Calibri', 12))
        self.lb_telefono.grid(row=1, column=0, pady=2, sticky='w')
        self.caja_telefono.grid(row=1, column=1)

        self.lb_email = Label(self.top, text="Email", font=('Calibri', 12,'bold'))
        self.caja_email = Entry(self.top, width=40, font=('Calibri', 12))
        self.lb_email.grid(row=2, column=0, pady=2, sticky='w')
        self.caja_email.grid(row=2, column=1)

        self.lb_empresa = Label(self.top, text="Empresa", font=('Calibri', 12,'bold'))
        self.caja_empresa = Entry(self.top, width=40, font=('Calibri', 12))
        self.lb_empresa.grid(row=3, column=0, pady=2, sticky='w')
        self.caja_empresa.grid(row=3, column=1)

        self.frame_top = Frame(self.top, padx=40)
        self.frame_top.grid(row=5, column=0, columnspan=3, sticky="nswe")

        self.btn_cancelar = Button(self.frame_top, text="Cancelar",bg="#ddd", font=('Calibri', 10,'bold'), command=self.top.destroy)
        self.btn_cancelar.grid(row=0, column=1, padx=60, pady=10, ipadx=15, ipady=10)

        self.btn_guardar = Button(self.frame_top, text="Guardar",bg="#ddd", font=('Calibri', 10,'bold'), command=self.nuevo_cliente)
        self.btn_guardar.grid(row=0, column=2, padx=10, ipadx=15, ipady=10)

        self.caja_nombre.focus()
        self.top.bind("<Return>", lambda x : self.nuevo_cliente())


    def cargar_datos(self):#Cargar la lista de los clientes en la grilla

        rows = self.cliente1.cargar_datos()
        self.tree.delete(*self.tree.get_children())

        for row in rows:
            self.tree.insert('', END, row[0], values=(row[1], row[2], row[3], row[4]))

    def cargar_datos_top(self):#Cargar datos en la ventana emergente

        self.opcion = "False"#Variable que cambia segun si se quiere modificar o ingresar
        
        if len(self.tree.selection()) == 0:
            messagebox.showerror("Error","Seleccione un cliente que desee editar")
        else:
            id = self.tree.selection()[0]#Selecionar dato
            rows = self.cliente1.cargar_datos_top(id)
             
            self.cargar_objetos_top()
            self.top.title("Editar Cliente")
            self.caja_nombre.insert(0, rows[1])
            self.caja_telefono.insert(0, rows[2])
            self.caja_email.insert(0, rows[3])
            self.caja_empresa.insert(0, rows[4])
                  
        
    def insertar(self, cliente):#Ingresar nuevo cliente

        self.cliente1.insertar_datos(cliente)
    

    def modificar(self, cliente):#Modificar nuevo cliente

        id = self.tree.selection()[0]
        self.cliente1.modificar_datos(cliente, id)


    def nuevo_cliente(self):#Agregar nuevo cliente

        if not self.caja_nombre.get():
            messagebox.showerror("Error","El nombre es obligatorio") 
            self.top.lift()
            return
        if not self.caja_telefono.get():
            messagebox.showerror("Error","El telefono es obligatorio")
            self.top.lift()
            return
        if not self.caja_empresa.get():
            messagebox.showerror("Error","La empresa es obligatorio")
            self.top.lift()
            return

        cliente = {
                
            'nombre': self.caja_nombre.get(),
            'telefono': self.caja_telefono.get(),
            'email': self.caja_email.get(),
            'empresa': self.caja_empresa.get()
        }
            
        if self.opcion == "True":
            self.insertar(cliente)
            
        if self.opcion == "False":    
            self.modificar(cliente)
            self.opcion = "True"

        self.top.destroy()#Cierra la ventana
        self.cargar_datos()
        
            
    def eliminar_cliente(self):#Eliminar cliente seleccionado

        if len(self.tree.selection()) == 0  :#Selecionar dato
            messagebox.showerror("Error","Seleccione a un cliente")
        else:
            id = self.tree.selection()[0]
            cliente = self.cliente1.buscar_cliente(id)
            respuesta = messagebox.askokcancel("Seguro?", f"Estas seguro de querer eliminar a cliente {cliente[1]}?")
            if respuesta:
                self.cliente1.eliminar(id)
                self.cargar_datos()
            else:
                pass


ventana = Ventana()


