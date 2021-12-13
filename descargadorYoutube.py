import pytube
from pytube import YouTube
import tkinter
from tkinter import *
from tkinter import ttk
import os

previousprogress = 0
##Es la encargada de la barra progresiva
def progress_func(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    while liveprogress > previousprogress:
        previousprogress = liveprogress
        print(str(liveprogress) + "%")
        progress['value']= liveprogress
        ventana.update_idletasks()

#Funcion de seleccion del modo de descarga
def descargar() :
    if seleccion.get() == 'video':
        descargar_video()
    elif seleccion.get() == 'audio':
        descargar_audio()

#Funcion de descarga en formato video
def descargar_video():
    global previousprogress
    url= cajaTexto.get()
    try:
        yt= YouTube(url, on_progress_callback= progress_func)
        video= yt.streams.filter(progressive=True, file_extension='mp4').first()	# Establece la resolucion
        try:
            # Iniciando descarga
            print("Inciando descarga")
            etiqueta2["text"]= "Iniciando descarga"
            video.download("Descarga")
            print("Descarga completa")
            etiqueta2["text"]= "Descarga completa"
        except:
            etiqueta2["text"]= "Error al descargar"
    except:
        etiqueta2["text"]= "Error al conectar con internet"
    previousprogress= 0

#Funcion de descarga en formato audio
def descargar_audio():
    global previousprogress
    url= cajaTexto.get()
    try:
        yt= YouTube(url, on_progress_callback= progress_func)
        audio= yt.streams.filter(only_audio= True).first()
        try:
            # Iniciando descarga
            print("Inciando descarga")
            etiqueta2["text"]= "Iniciando descarga"
            direccion= audio.download("Descarga")
            os.rename(direccion, direccion[:-4]+ '.mp3')
            print("Descarga completa")
            etiqueta2["text"]= "Descarga completa"
        except:
            etiqueta2["text"]= "Error al descargar"
    except:
        etiqueta2["text"]= "Error al conectar con internet"
    previousprogress= 0


# Ventana principal
ventana= tkinter.Tk()
ventana.title("Descargador de Youtube")
etiqueta1= tkinter.Label(ventana, text= "Bienvenido al desacargador...").pack()
opciones= ["video", "audio"]
cajaTexto= tkinter.Entry(ventana)
cajaTexto.pack()

seleccion= StringVar()
seleccion.set(opciones[0])
drop= OptionMenu(ventana, seleccion, *opciones)
drop.pack(pady= 20)

etiqueta2= tkinter.Label(ventana)
etiqueta2.pack()
progress= ttk.Progressbar(ventana, orient= HORIZONTAL, length= 400, mode= "determinate")
progress.pack(pady= 10)

boton1= tkinter.Button(ventana, text= "Descargar", padx= 15, pady= 10, command= descargar).pack()
ventana.mainloop()

