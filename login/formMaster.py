import tkinter as tk 
#from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from login.formFunciones import Funciones
from login.formSucursal import Sucursal



# LA HACEMOS CLASE PORQUE NECESITAMOS UN CONSTRUCTOR QUE GENERE LA VENTANA
class MasterPanel:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master panel')
        w,h = self.ventana.winfo_screenwidth(),self.ventana.winfo_screenheight() # que la ventana se adapte ala pantalla 
        self.ventana.geometry("%dx%d+0+0" % (w,h)) # asignar tamaño de la ventana
        self.ventana.config(bg='#fcfcfc',cursor='boat') # fondo de LA VENTANA | cursor da forma al cursor del mouse
        self.ventana.resizable(width=0, height=0)
        
        self.ventana.iconbitmap('./images/iconCine.ico') # icono de la ventana (.ico)
        
        self.ventana.resizable(0,1) # que el usuario no pueda ampliar o hacer mas chica la imagen (0=false,1=true) (x (a lo ancho),y (a lo largo))
        
        logo = utl.read_image('./images/cine_logo.png',(200,200))
        
        texto = Label(self.ventana, text='CINELUXE')
        texto.pack()
        
        # etiqueta para colocar la imagen 
        label = tk.Label(self.ventana,image=logo,bg='orange')
        label.place(relx=0.5,rely=0.5,anchor='center') # para que se posicione al centro de la ventana tenemos que poner relx y rely a 0.5
        
        
        boton1 = Button(self.ventana, text= 'Minimizar',bg='red',command=self.ventana.iconify) # el comando hace que se minimice la ventana 
        # si no se les da valores al pack, se van a agregar los elemnetos en el centro 
        boton1.pack(side=LEFT) 
        
        def imprimir ():
            labelImprimir = Label(self.ventana, text='Imprimiendo...')
            labelImprimir.pack()
            
        
        boton2 = Button(self.ventana,text='Imprimir',bg='blue',command=imprimir)
        boton2.pack(side=RIGHT)
        
        def sucursal():
            self.ventana.destroy()
            Sucursal()
            
        def funciones():
            self.ventana.destroy()
            Funciones()
        
        # POSICIONAMIENTO DE LOS PLACE 
        sucursalLabel = tk.Label(self.ventana,text='Sucursal:',bg='#fcfcfc',font=('Tahoma',10))
        sucursalLabel.place(x=30,y=40)
        
        sucursalBoton = Button(self.ventana,text='Ver sucursales disponibles',bg='gray',command=sucursal)
        sucursalBoton.place(x=100,y=40)
        
        funcionLabel = tk.Label(self.ventana,text='Funciones:',bg='#fcfcfc',font=('Tahoma',10))
        funcionLabel.place(x=30,y=90)
        
        funcionBoton = Button(self.ventana,text='Ver funciones disponibles',bg='gray',command=funciones)
        funcionBoton.place(x=100,y=90)
        

        
        self.ventana.mainloop() #para que la ventana se mantenga abierta 
        
        