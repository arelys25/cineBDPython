import tkinter as tk 
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import messagebox

class Funciones:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Funciones del cine')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='gray', cursor='boat')
        self.ventana.resizable(width=0, height=0)
        scrollbar = Scrollbar(self.ventana,orient='vertical',command=Text.yview)
        scrollbar.grid(row=0,column=1,sticky=tk.NS)

        self.ventana.iconbitmap('./images/iconCine.ico')

        try:
            # Guardar la referencia de la imagen
            logo = utl.read_image('./images/cine_logo.png', (75, 75))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        
        lblLogo = tk.Label(self.ventana, image=logo, bg='gray')
        lblLogo.place(x=0, y=0)
        
        # Otros elementos de la interfaz...
        
        datosLabel = tk.Label(self.ventana, text='Funciones en Luxor:', font=('Tahoma', 40,BOLD), bg='gray',fg='#8b0000')
        datosLabel.place(x=130, y=10)
        
        opcion = IntVar()
        peli1 = tk.Label(self.ventana, text='Sleep', font=('Arial', 25,BOLD), bg='gray')
        peli1.place(x=370, y=100)
        try:
            # Guardar la referencia de la imagen como atributo de la clase
            self.sleep = utl.read_image('./images/sleep.png', (200, 260))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        sleeplbl = tk.Label(self.ventana, image=self.sleep, bg='gray')
        sleeplbl.place(x=130, y=100)
        sleepFun = tk.Label(self.ventana,text='Funciones del 28/10/2024:', font=('Arial', 15), bg='gray')
        sleepFun.place(x=375, y=150)
        fun1 = Radiobutton(self.ventana,text= '11:30 am',font=('Arial', 13), bg='gray',value=1,variable=opcion)
        fun1.place(x=380,y=200)
        fun2 = Radiobutton(self.ventana,text= '14:10 pm',font=('Arial', 13), bg='gray',value=2,variable=opcion)
        fun2.place(x=380,y=230)
        fun3 = Radiobutton(self.ventana,text= '18:00 pm',font=('Arial', 13), bg='gray',value=3,variable=opcion)
        fun3.place(x=380,y=260)
        fun4 = Radiobutton(self.ventana,text= '21:50 pm',font=('Arial', 13), bg='gray',value=4,variable=opcion)
        fun4.place(x=380,y=290)
        
        
        peli2 = tk.Label(self.ventana, text='La Morgue', font=('Arial', 25,BOLD), bg='gray')
        peli2.place(x=370, y=400)
        try:
            # Guardar la referencia de la imagen como atributo de la clase
            self.morgue = utl.read_image('./images/morgue.png', (200, 260))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        morguelbl = tk.Label(self.ventana, image=self.morgue, bg='gray')
        morguelbl.place(x=130, y=400)
        morgueFun = tk.Label(self.ventana,text='Funciones del 28/10/2024:', font=('Arial', 15), bg='gray')
        morgueFun.place(x=375, y=450)
        fun5 = Radiobutton(self.ventana,text= '10:30 am',font=('Arial', 13), bg='gray',value=5,variable=opcion)
        fun5.place(x=380,y=500)
        fun6 = Radiobutton(self.ventana,text= '13:10 pm',font=('Arial', 13), bg='gray',value=6,variable=opcion)
        fun6.place(x=380,y=530)
        fun7 = Radiobutton(self.ventana,text= '17:00 pm',font=('Arial', 13), bg='gray',value=7,variable=opcion)
        fun7.place(x=380,y=560)
        fun8 = Radiobutton(self.ventana,text= '20:50 pm',font=('Arial', 13), bg='gray',value=8,variable=opcion)
        fun8.place(x=380,y=590)
        
        
        peli3 = tk.Label(self.ventana, text='Ouija, el origen del mal', font=('Arial', 25,BOLD), bg='gray')
        peli3.place(x=370, y=700)
        try:
            # Guardar la referencia de la imagen como atributo de la clase
            self.ouija = utl.read_image('./images/ouija.png', (200, 260))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        ouijalbl = tk.Label(self.ventana, image=self.ouija, bg='gray')
        ouijalbl.place(x=130, y=700)
        ouijaFun = tk.Label(self.ventana,text='Funciones del 28/10/2024:', font=('Arial', 15), bg='gray')
        ouijaFun.place(x=375, y=750)
        fun9 = Radiobutton(self.ventana,text= '9:30 am',font=('Arial', 13), bg='gray',value=9,variable=opcion)
        fun9.place(x=380,y=800)
        fun10 = Radiobutton(self.ventana,text= '15:10 pm',font=('Arial', 13), bg='gray',value=10,variable=opcion)
        fun10.place(x=380,y=830)
        fun11 = Radiobutton(self.ventana,text= '19:00 pm',font=('Arial', 13), bg='gray',value=11,variable=opcion)
        fun11.place(x=380,y=860)
        fun12 = Radiobutton(self.ventana,text= '22:50 pm',font=('Arial', 13), bg='gray',value=12,variable=opcion)
        fun12.place(x=380,y=890)
        
        self.bolets = IntVar()
        
        def boletos():
            try:    
                boletos = self.bolets.get()
                
                if boletos <=0:
                    messagebox.showerror("Error", "Todos los campos son obligatorios")
                    return  # Evitar continuar si hay campos vacíos
                
                if opcion.get() == 1 or opcion.get()== 2 or opcion.get()==3 or opcion.get() == 4:
                    if opcion.get() == 1:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'Sleep' en el horario de 11:30 am.")
                    elif opcion.get()== 2:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'Sleep' en el horario de 14:10 pm.")
                    elif opcion.get()== 3:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'Sleep' en el horario de 18:00 pm.")
                    elif opcion.get()== 4:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'Sleep' en el horario de 21:50 pm.")
                elif opcion.get() == 5 or opcion.get()== 6 or opcion.get()==7 or opcion.get() == 8:
                    if opcion.get() == 5:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Morgue' en el horario de 10:30 am.")
                    elif opcion.get()== 6:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Morgue' en el horario de 13:10 pm.")
                    elif opcion.get()== 7:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Morgue' en el horario de 17:00 pm.")
                    elif opcion.get()== 8:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Morgue' en el horario de 20:50 pm.")
                elif opcion.get() == 9 or opcion.get()== 10 or opcion.get()==11 or opcion.get() == 12:
                    if opcion.get() == 9:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Ouija' en el horario de 9:30 am.")
                    elif opcion.get()== 10:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Ouija' en el horario de 15:10 pm.")
                    elif opcion.get()== 11:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Ouija' en el horario de 19:00 pm.")
                    elif opcion.get()== 12:
                        info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'La Ouija' en el horario de 22:50 pm.")
                else:
                    info = (f"Hola! Usted ha comprado {boletos} boletos para la \nfuncion 'SIN DEFINIR en el horario de SIN DEFINIR.")
                
            
                # Widget Text para mostrar la información
                textDatos = tk.Text(self.ventana, font=('Arial', 11), width=50, height=5, bd=2, state='disabled')
                textDatos.place(x=1000, y=200)

                # Mostrar información en el widget Text
                textDatos.config(state='normal')  # Habilitar edición temporal
                textDatos.delete(1.0, 'end')  # Limpiar contenido previo
                textDatos.insert('end', info)  # Insertar la información
                textDatos.config(state='disabled')  # Volver a deshabilitar
            except Exception as e:
                messagebox.showerror("Error", "Numero de boletos invalido",e)
            
            
        
        boletoslbl = tk.Label(self.ventana, text='Cantidad de boletos:', font=('Arial', 25,BOLD), bg='gray')
        boletoslbl.place(x=1000, y=100)
        boletosEnt = tk.Entry(self.ventana,font=('Arial', 22),textvariable=self.bolets,bd=2)
        boletosEnt.place(x=1330,y=103)
        boletosbtn = tk.Button(self.ventana,text='TERMINAR COMPRA',command=boletos,bd=5,bg='pink')
        boletosbtn.place(x=1150,y=150)
        
        # MENU Y CHECKBUTTON
        def orden():
            lista = ''
            if(queso.get()):
                lista += ' con queso'
            else :
                lista += ' sin queso'
                
            if(lechuga.get()):
                lista += ' y con lechuga'
            else:
                lista += ' y sin legucha'
                
            imprimirOrden.config(text= lista)
        
        queso = IntVar()
        lechuga = IntVar()
        self.hamburguesa = utl.read_image('./images/hamburguesa.png',(145,145))
        Label(self.ventana,image=self.hamburguesa).place(x=1300,y=465)
        
        frame = Frame(self.ventana)
        frame.pack(side=RIGHT)
        frame.config(bg='goldenrod3')
        
        Label(frame,text='¿Cómo desea su hamburguesa?',bg='goldenrod3',font=('Arial', 25)).pack(anchor='w')
        Checkbutton(frame,text='con queso', variable=queso, onvalue=1,offvalue=0,bg='goldenrod3',font=('Arial', 20),command=orden).pack(anchor='w')
        Checkbutton(frame,text='con lechuga', variable=lechuga, onvalue=1,offvalue=0,bg='goldenrod3',font=('Arial', 20),command=orden).pack(anchor='w')
        
        imprimirOrden = Label(frame,bg='goldenrod3')
        imprimirOrden.pack(anchor='w')
        imprimirOrden.config(font=('Arial', 15))
        
        # MENUS DE OPCIONES 
        
            # VENTANAS EMERGENTES
        
        def nuevo():
            messagebox.askquestion('Abrir nuevo documento',message='¿Estas seguro?')
            
        def licencia():
            messagebox.showinfo('Version',message='Version 1.0')
            
        def error():
            messagebox.showerror('ERROR',message='¡BORRASTE LA BASE DE DATOS!')
            
        def precaucion():
            messagebox.showwarning('Atencion',message='Se copiará todo')
        
        menuBar = Menu(self.ventana)
        self.ventana.config(menu= menuBar)
        
        archivoMenu = Menu(menuBar,tearoff=0) #,tearoff=0 hace que las lineas punteadas por default se quiten 
        archivoMenu.add_command(label='Nuevo',command=nuevo)
        archivoMenu.add_command(label='Abrir')
        archivoMenu.add_command(label='Guardar')
        archivoMenu.add_command(label='Cerrar',command=error)
        archivoMenu.add_separator() # separar el menu de la opcion de salir 
        archivoMenu.add_command(label='Salir',command=self.ventana.quit) # añadirle un comando para que se slaga de la ventana al oprimirlo 
        
        editMenu = Menu(menuBar,tearoff=0)
        editMenu.add_command(label='Cortar')
        editMenu.add_command(label='Copiar',command=precaucion)
        editMenu.add_command(label='Pegar')
        
        ayudaMenu = Menu(menuBar,tearoff=0)
        ayudaMenu.add_command(label='Licencia',command=licencia)
        ayudaMenu.add_separator()
        
        menuBar.add_cascade(label='Archivo',menu=archivoMenu) # colocar el menu para que lo podamos ver
        menuBar.add_cascade(label='Editar',menu=editMenu)
        menuBar.add_cascade(label='Ayuda',menu=ayudaMenu)
        
        # SPINBOX
        w = Spinbox(self.ventana,values=('Sala VIP','Sala 3D','Sala 4D','Sala IMAX','Sala Kids'),font=('Arial', 20))
        w.place(x=1500,y=260)
        
        e = Spinbox(self.ventana,values=('Asientos altos','Asientos medios','Asientos bajos'),font=('Arial', 20))
        e.place(x=1500,y=310)
        
        # LISTAS 
        def agregar():
            listaProductos.insert(END, entrada.get())
        
        productos = Label(self.ventana,text='Productos',font=('Arial', 15,BOLD),bg='gray')
        productos.place(x=900,y=560)
        
        listaProductos = Listbox(self.ventana, width=30,font=('Arial', 12))
        listaProductos.insert(0,'Vasos') # indice del lugar en la lista | nombre del elemento a añadir
        listaProductos.insert(1,'Bote de palomitas')
        listaProductos.insert(2,'Nachos')
        listaProductos.insert(3,'Cubiertos')
        listaProductos.place(x=900,y=600)
        
        # eliminar productos de la lista 
        listaProductos.delete(2) # posicion del elemento
        
        # para que el usuario pueda añadir un producto
        entrada = Entry(self.ventana,bd=3)
        entrada.place(x=900,y=800)
        
        agregarProductobtn = Button(self.ventana,text='Agergar producto',bd=3,bg='blue',command=agregar)
        agregarProductobtn.place(x=900,y=830)
        
        
        self.ventana.mainloop()  # Mantener la ventana abierta
        
