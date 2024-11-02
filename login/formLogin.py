import tkinter as tk 
from tkinter.font import BOLD
import util.generic as utl
from tkinter import ttk, messagebox
from login.formMaster import MasterPanel

class App:
    
    # VERIFICAR EL INICIO DE SESION 
    def verificar(self):
        user = self.usuario.get()
        passw = self.password.get()
        if(user == 'arely' and passw == '1234'):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message='El usuario y/o contraseña no son correctos',title='Information')
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.config(bg='#fcfcfc',cursor='boat') # cursor da forma al cursor del mouse
        self.ventana.resizable(width=0,height=0) # que el usuario no pueda ampliar o hacer mas chica la imagen (0=false,1=true) (x (a lo ancho),y (a lo largo))
        utl.central_window(self.ventana,800,500)
        
        logo = utl.read_image('./images/cine_logo.png',(200,200))
        
        # frame logo (panel que contendrá al logo)
        #      meter ventana en el frame | sin bordes | tamaño | que sea solido | que tenga esos espacios respetados | color de fondo
        frame_logo = tk.Frame(self.ventana, bd=0,width=300,relief=tk.SOLID, padx=10, pady= 10, bg='gray')
        # que se posicione del lado izquiero | que se expanda en todo el espacio |que se llene tanto x como y 
        frame_logo.pack(side='left',expand=tk.NO,fill=tk.BOTH)
        label = tk.Label(frame_logo,image=logo,bg='gray')
        label.place(x=0,y=0,relwidth=1,relheight=1)
        
        # frame form 
        frame_form= tk.Frame(self.ventana, bd=0,width=300,relief=tk.SOLID, padx=10, pady= 10, bg='#fcfcfc')
        frame_form.pack(side='right',expand=tk.YES,fill=tk.BOTH)
        
        #frame form top 
        frame_form_top= tk.Frame(frame_form, bd=0,height=50,relief=tk.SOLID, bg='black')
        frame_form_top.pack(side='top',fill=tk.X)
        title= tk.Label(frame_form_top,text='Inicio de sesion',font=('Tahoma',30), fg='black',bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        # end frame_form_top
        
        # frame de ingreso de datos 
        frame_form_fill = tk.Frame(frame_form, bd=0,height=50,relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)
        
        # etiqueta usuario 
        user_label = tk.Label(frame_form_fill,text='Usuario', font=('Tahoma',14),fg='black',bg="#fcfcfc", anchor='w') # anchor w, que lo posicione al este (west)
        user_label.pack(fill=tk.X,padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Tahoma', 12))
        self.usuario.pack(fill=tk.X,padx=20,pady=10)
        
        # etiqueta password
        password_label = tk.Label(frame_form_fill,text='Contraseña', font=('Tahoma',14),fg='black',bg="#fcfcfc", anchor='w') # anchor w, que lo posicione al este (west)
        password_label.pack(fill=tk.X,padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Tahoma', 12))
        self.password.pack(fill=tk.X,padx=20,pady=10)
        self.password.config(show='*') #que todo lo que se escriba se ingrese con asteriscos
        
        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Tahoma',14,BOLD),bg='black', bd=0,fg='#fff',command=self.verificar)
        inicio.pack(fill=tk.X,padx=20,pady=20)
        inicio.bind('<Return>',(lambda event: self.verificar()))
        # bind indica un evento que queremos cachar, si le damos enter al boton, se identificará con una funcion lambda que se dispare el evento de la funcion 
        
        
        self.ventana.mainloop()
        
        
        
        