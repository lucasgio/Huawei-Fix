from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as msg
from paralleladb import ParallelADB
import os.path
from io import open
import time

class Huawei:

    def __init__(self):
        self.huawei = Tk()
        self.titulo = 'HUAWEI FIX CUBACEL'
        self.icono = os.path.abspath('.\\imagenes\\logo.ico')
        self.size = '700x650'


    def config(self):
        # Creamos las dimensiones de la aplicacion
        self.huawei.geometry(self.size)
        # Movimiento de las dimensiones default(False)
        self.huawei.resizable(0,0)
        # Titulo de aplicacion
        self.huawei.title(self.titulo)
        # Icono
        self.huawei.iconbitmap(self.icono)

    # Funcion para mostrar mensaje de informacion
    def msjAyuda(self):
        msg.showinfo('Informacion',"""
            Este metodo soluciona el reinicio constante en 
            algunos telefonos huawei que despues de un update 
            aparece un popup exigiendo reinicio constante.

            NO es para hacer unlock permanente
        """)



    def framederecho(self):
        framederecho = Frame(self.huawei,width=350,height=650)
        framederecho.pack(anchor=W)
        # Subtitulo de la aplicacion
        subtitulo = Label(framederecho,text='HUAWEI FIX SIM CUBACEL')
        subtitulo.config(padx=50,pady=30)
        subtitulo.pack()
        # Intrucciones
        Label(framederecho,text='Instruccciones').pack(anchor=W,padx=20)
        Label(framederecho,text='1.Habilitar depuracion usb').pack(anchor=W,padx=20)
        Label(framederecho,text='2.Remover SIM CUBACEL').pack(anchor=W,padx=20)
        Label(framederecho,text='3.Presionar boton FIX').pack(anchor=W,padx=20)
        # Botones
        ayuda = Button(framederecho,text='Consejos',command=self.msjAyuda)
        ayuda.config(padx=20)
        ayuda.pack(side=LEFT,padx=20,pady=50)
        fix = Button(framederecho,text='FIX',command=self.remover)
        fix.config(padx=20)
        fix.pack(side=LEFT,)

    # Funcion con la logica del procedimiento
    def remover(self):
        try:
            adb = os.system('adb devices')
            #print(adb)
            if adb == 1 :
                Label(self.huawei,text='Intentando remover.....').pack(side=BOTTOM)
                adb = os.system('adb shell')
                adb = os.system('pm list package')
                adb = os.system('pm uninstall -k —user 0 com.huawei.tmecustomize')
                #print(adb)
                self.msgsucces()
            elif adb == 0:
                msg.showerror('Error',"""
                    1.Verifique el cable usb este conectado la pc
                    2.Verifique la depuracion usb este activa
                    3.Verifique que SIM este extraida correctamente
                    """
                )
        except Exception:
            msg.showerror('Error',"""
                Ha ocurrido un error, por favor intente de nuevo
                """
            )
  
    def msgsucces(self):
        msg.showinfo("Exito","""
            Ya fue removido exitosamente
            Por favor,reinicie e inserte la sim.

            Gracias
        """)

    def msgwelcome(self):
        msg.showinfo('Info',"""
            Este software esta realizado para distribucion gratuita
            Es un metodo que esta en la web solo fue 
            desarrollado para automatizar el proceso

            Desarrollado por Iosvany
            2021

        """)

    def run(self):
        self.huawei.mainloop()
if __name__ == '__main__':
    newhuawei = Huawei()
    newhuawei.config()
    newhuawei.framederecho()
    newhuawei.msgwelcome()
    newhuawei.run()

