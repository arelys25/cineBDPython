from PIL import ImageTk, Image


# FUNCION PARA LEER IMAGEN
def read_image (path,size):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")


# CENTRAR VENTANA
def central_window (ventana,aplicacion_ancho,aplicacion_largo):
    pantallaAncho = ventana.winfo_screenwidth()
    pantallaLargo = ventana.winfo_screenheight()
    x= int ((pantallaAncho/2) - (aplicacion_ancho/2))
    y= int ((pantallaLargo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
