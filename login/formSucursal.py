import tkinter as tk 
import util.generic as utl
from tkinter import *
from tkinter import messagebox




class Sucursal:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.config(bg='#fcfcfc',cursor='boat') # cursor da forma al cursor del mouse
        self.ventana.resizable(width=0,height=0) # que el usuario no pueda ampliar o hacer mas chica la imagen (0=false,1=true) (x (a lo ancho),y (a lo largo))
        utl.central_window(self.ventana,700,700)
        self.ventana.iconbitmap('./images/iconCine.ico')

        try:
            # Guardar la referencia de la imagen
            logo = utl.read_image('./images/cine_logo.png', (75, 75))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        
        lblLogo = tk.Label(self.ventana, image=logo, bg='#fcfcfc')
        lblLogo.place(x=0, y=0)

        datosLabel = tk.Label(self.ventana, text='Ingresa los datos para ubicar tu cine más cercano:', font=('Tahoma', 15), bg='#fcfcfc')
        datosLabel.place(x=130, y=10)
        
        estado = StringVar()
        ciudad = StringVar()
        cp = StringVar()
        datos = StringVar()
        
        def mostrarInfo():
            if not (estado.get() or ciudad.get() or cp.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  # Evitar continuar si hay campos vacíos

            info = (f"Hola, usted vive en el estado de {estado.get()},\n"
                    f"ciudad {ciudad.get()} y su código postal es {cp.get()}")
            
            # Widget Text para mostrar la información
            textDatos = tk.Text(self.ventana, font=('Arial', 11), width=40, height=5, bd=2, state='disabled')
            textDatos.place(x=130, y=500)

            # Mostrar información en el widget Text
            textDatos.config(state='normal')  # Habilitar edición temporal
            textDatos.delete(1.0, 'end')  # Limpiar contenido previo
            textDatos.insert('end', info)  # Insertar la información
            textDatos.config(state='disabled')  # Volver a deshabilitar
        

        paisLabel = tk.Label(self.ventana, text='Estado:', font=('Arial', 12), bg='#fcfcfc')
        paisLabel.place(x=130, y=50)
        paisEnt = tk.Entry(self.ventana,font=('Arial', 11),textvariable=estado,bd=2)
        paisEnt.place(x=200,y=50)

        ciudadLabel = tk.Label(self.ventana, text='Ciudad:', font=('Arial', 12), bg='#fcfcfc')
        ciudadLabel.place(x=130, y=100)
        ciudadEnt = tk.Entry(self.ventana,font=('Arial', 11),textvariable=ciudad,bd=2)
        ciudadEnt.place(x=200,y=100)
        
        cpLabel = tk.Label(self.ventana, text='CP:', font=('Arial', 12), bg='#fcfcfc')
        cpLabel.place(x=130, y=150)
        cpEnt = tk.Entry(self.ventana,font=('Arial', 11),textvariable=cp,bd=2)
        cpEnt.place(x=200,y=150)
        
        
        buscarbtn = tk.Button(self.ventana,text='BUSCAR CINE',command=self.buscarCine,bd=5,bg='pink')
        buscarbtn.place(x=170,y=200)
        
        mostrarDatosbtn = tk.Button(self.ventana,text='MOSTRAR INFO',command=mostrarInfo,bd=5,bg='pink')
        mostrarDatosbtn.place(x=300,y=200)
        
                
        self.ventana.mainloop()  # Mantener la ventana abierta
        
    def buscarCine(self):
            buscandolbl = tk.Label(self.ventana,text='Cine mas cercano:',font=('Arial', 12), bg='#fcfcfc')
            buscandolbl.place(x=150,y=250)
            encontradolbl = Label(self.ventana,text='Luxe Plaza Forum. Av. Vallarta, \nCol. Rosas #425',font=('Arial', 12), bg='#fcfcfc')
            encontradolbl.place(x=150,y=290)
            
            try:
                # Guardar la referencia de la imagen como atributo de la clase
                self.luxe = utl.read_image('./images/luxe.png', (150, 150))
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

            luxelbl = tk.Label(self.ventana, image=self.luxe, bg='#fcfcfc')
            luxelbl.place(x=190, y=330)
               