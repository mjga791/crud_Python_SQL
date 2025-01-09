# INSPIRADO EN EL SIGUIENTE TUTORIAL: https://www.youtube.com/watch?v=Ro2m95m8QkI
# Sin Rueda Tecnología
# Cómo hacer un CRUD en Python con MySQL
# Pero corregido con Copilot


import tkinter as tk
from tkinter import LabelFrame, StringVar, Tk, ttk
from tkinter import messagebox
from tkinter import Entry, Label, Button
from tkinter import END

# Importamos las clases que necesitamos
from Clientes import CCliente

class FormularioClientes:
    def __init__(self):
        self.base = None
        self.texBoxID = None
        self.texBoxNombre = None
        self.texBoxApellidos = None
        self.seleccionNacionalidad = None
        self.combo = None
        self.groupboxDatos = None
        self.groupboxListado = None
        self.tree = None
        self.scrollbar = None

    def Formulario(self):
        try:
            self.base = Tk()
            self.base.title("Formulario de Clientes Python")
            self.base.geometry("800x400")
            self.base.config(bg="dark green")

            self.groupboxDatos = LabelFrame(self.base, text="DATOS PERSONALES", bg="light green", font=("Calibri", 14), padx=5, pady=5)
            self.groupboxDatos.grid(row=0, column=0, padx=10, pady=10)

            Label(self.groupboxDatos, text="ID del cliente: ", bg="dark green", fg="white", width=20, anchor=tk.W, font=("Calibri", 12)).grid(row=0, column=0, padx=5, pady=5)
            self.texBoxID = Entry(self.groupboxDatos, width=20, font=("Calibri", 12))
            self.texBoxID.grid(row=0, column=1, padx=5, pady=5)

            Label(self.groupboxDatos, text="Nombre del cliente: ", bg="dark green", fg="white", width=20, anchor=tk.W, font=("Calibri", 12)).grid(row=1, column=0, padx=5, pady=5)
            self.texBoxNombre = Entry(self.groupboxDatos, width=20, font=("Calibri", 12))
            self.texBoxNombre.grid(row=1, column=1, padx=5, pady=5)

            Label(self.groupboxDatos, text="Apellidos del cliente: ", bg="dark green", fg="white", width=20, anchor=tk.W, font=("Calibri", 12)).grid(row=2, column=0, padx=5, pady=5)
            self.texBoxApellidos = Entry(self.groupboxDatos, width=20, font=("Calibri", 12))
            self.texBoxApellidos.grid(row=2, column=1, padx=5, pady=5)

            Label(self.groupboxDatos, text="Nacionalidad: ", bg="dark green", fg="white", width=20, anchor=tk.W, font=("Calibri", 12)).grid(row=3, column=0, padx=5, pady=5)
            self.seleccionNacionalidad = StringVar()
            self.combo = ttk.Combobox(self.groupboxDatos, values=["EU", "No EU"], textvariable=self.seleccionNacionalidad, font=("Calibri", 12))
            self.combo.grid(row=3, column=1, padx=5, pady=5)
            self.seleccionNacionalidad.set("---")

            Button(self.groupboxDatos, text="Guardar", width=15, command=self.guardarRegistros, bg="dark green", fg="white", font=("Calibri", 12)).grid(row=4, column=0, padx=5, pady=15)
            Button(self.groupboxDatos, text="Modificar", width=15, command=self.modificarRegistros, bg="dark green", fg="white", font=("Calibri", 12)).grid(row=4, column=1, padx=5, pady=15)
            Button(self.groupboxDatos, text="Eliminar", width=15, command=self.eliminarRegistros, bg="dark green", fg="white", font=("Calibri", 12)).grid(row=4, column=2, padx=5, pady=15)

            self.groupboxListado = LabelFrame(self.base, text="LISTADO DE CLIENTES", bg="light blue", font=("Calibri", 14), padx=5, pady=5)
            self.groupboxListado.grid(row=0, column=1, padx=10, pady=10)

            self.tree = ttk.Treeview(self.groupboxListado, columns=("ID", "Nombre", "Apellidos", "Nacionalidad"), show="headings", height=10)
            self.tree.heading("ID", text="ID")
            self.tree.heading("Nombre", text="Nombre")
            self.tree.heading("Apellidos", text="Apellidos")
            self.tree.heading("Nacionalidad", text="Nacionalidad")
            self.tree.grid(row=0, column=0, padx=2, pady=2)

            # Añadir el scrollbar al treeview
            # Para que se pueda desplazar verticalmente
            self.scrollbar = ttk.Scrollbar(self.groupboxListado, orient="vertical", command=self.tree.yview)
            self.scrollbar.grid(row=0, column=1, sticky='ns')
            self.tree.configure(yscrollcommand=self.scrollbar.set)


            # Agregar los datos de los clientes
            clientes = CCliente.mostrarClientes()
            print("Clientes obtenidos:", clientes)  # Depuración
            for row in clientes:
                self.tree.insert("", "end", values=row)

            # Agregamos la función de selección de registros
            # self.tree.bind: Este método se usa para vincular un evento a un widget específico
            # "<<TreeviewSelect>>" es un evento especial de Treeview 
            # que se dispara cuando se selecciona un ítem en el Treeview.
            # seleccionarRegistro es un método de la clase que maneja lo que 
            # debe suceder cuando se selecciona un ítem en el Treeview.
            self.tree.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

            self.base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz, error : {}".format(error))

    def guardarRegistros(self):
        try:
            if self.texBoxNombre is None or self.texBoxApellidos is None or self.combo is None:
                messagebox.showerror("Error", "Los widgets no están inicializados")
                return

            nombre = self.texBoxNombre.get()
            apellidos = self.texBoxApellidos.get()
            nacionalidad = self.seleccionNacionalidad.get()

            CCliente.altaClientes(nombre, apellidos, nacionalidad)
            messagebox.showinfo("Información", "Registro guardado correctamente")

            self.actualizarTreeView()

            self.texBoxNombre.delete(0, END)
            self.texBoxApellidos.delete(0, END)
            self.seleccionNacionalidad.set("EU")

        except ValueError as error:
            print("Error al guardar los registros, error : {}".format(error))
    
    def actualizarTreeView(self):
        try:
            # Borrar todos los registros actuales del TreeView
            # children se refiere a los registros del TreeView
            # Es decir, dejará sólo las cabeceras   
            self.tree.delete(*self.tree.get_children())

            # Para obtener los datos actualizados de la base de datos
            datos = CCliente.mostrarClientes()
            
            # Insertar los datos en el TreeView
            for row in datos:
                self.tree.insert("", "end", values=row)        

        except ValueError as error:
            print("Error al actualizar la tabla, error : {}".format(error))

    def seleccionarRegistro(self, event):
        # Esta función servirá para traer al formulario los datos del registro seleccionado
        try:
            # Obtener el ID del elemento seleccionado
            itemSeleccionado = self.tree.focus()

            if itemSeleccionado:
                # Obtener los valores por cada columna
                values = self.tree.item(itemSeleccionado)['values']

                # Borra el contenido actual del formulario
                # Y va trayendo cada uno de los valores del registro seleccionado
                
                self.texBoxID.delete(0, END)
                self.texBoxID.insert(0, values[0])
                self.texBoxNombre.delete(0, END)
                self.texBoxNombre.insert(0, values[1])
                self.texBoxApellidos.delete(0, END)
                self.texBoxApellidos.insert(0, values[2])
                # En el caso de la Nacionalidad, se selecciona el valor del combo
                self.combo.set(values[3])
                
        except ValueError as error:
            print("Error al seleccionar el registro, error : {}".format(error))

    def modificarRegistros(self):
        try:
            if self.texBoxID is None or self.texBoxNombre is None or self.texBoxApellidos is None or self.combo is None:
                messagebox.showerror("Error", "Los widgets no están inicializados")
                return

            id = self.texBoxID.get()
            nombre = self.texBoxNombre.get()
            apellidos = self.texBoxApellidos.get()
            nacionalidad = self.seleccionNacionalidad.get()

            CCliente.modificarClientes(id, nombre, apellidos, nacionalidad)
            messagebox.showinfo("Información", "Registro modificado correctamente")

            self.actualizarTreeView()

            self.texBoxID.delete(0, END)
            self.texBoxNombre.delete(0, END)
            self.texBoxApellidos.delete(0, END)
            self.seleccionNacionalidad.set("EU")

        except ValueError as error:
            print("Error al modificar los registros, error : {}".format(error)) 

    def eliminarRegistros(self):
        try:
            if self.texBoxID is None:
                messagebox.showerror("Error", "Los widgets no están inicializados")
                return

            id = self.texBoxID.get()
            
            CCliente.eliminarClientes(id)
            messagebox.showinfo("Información", "Registro Eliminado correctamente")

            self.actualizarTreeView()

            self.texBoxID.delete(0, END)
            self.texBoxNombre.delete(0, END)
            self.texBoxApellidos.delete(0, END)
            self.seleccionNacionalidad.set("EU")

        except ValueError as error:
            print("Error al modificar los registros, error : {}".format(error))  

formulario_clientes = FormularioClientes()
formulario_clientes.Formulario()
