from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as msg
from paralleladb import ParallelADB
import os.path
from io import open
import time


# Instanciamos el objeto
huawei = Tk()

# Creamos las dimensiones de la aplicacion
huawei.geometry('700x600')

# Movimiento de las dimensiones default(False)
huawei.resizable(0,0)

# Titulo de aplicacion
huawei.title('HUAWEI FIX METODO SIM CUBACEL')
# Funcion para mostrar mensaje de informacion
def msjAyuda():
    msg.showinfo('Informacion',"""
        Este metodo no es para hacer unlock a ningun huawei
        Funcional solamente para eliminar el reinicio constante
        en algunos modelos de Huawei
    """)
# Funcion con la logica del procedimiento
def remover():
    try:
        adb = ParallelADB.run('adb device')
        #adb = os.system('adb devices')
        print(adb)
        if adb == 0 :
            Label(frameizquierdo,text='Intentando remover.....').pack()
            adb = ParallelADB.run('adb shell')
            adb = ParallelADB.run('pm list package')
            adb = ParallelADB.run('pm uninstall -k —user 0 com.huawei.tmecustomize')
            print(adb)
        elif adb == 1:
            msg.showerror('Error',"""
                1.Verifique el cable usb este conectado la pc
                2.Verifique la depuracion usb este activa
                3.Verifique que SIM este extraida correctamente
            """)
    except Exception:
        msg.showerror('Error',"""
            Ha ocurrido un error, por favor intente de nuevo
        """)

# Primer Frame
frameizquierdo = LabelFrame(huawei,width=400,height=600)
frameizquierdo.pack(side=LEFT)
frameizquierdo.pack_propagate(False)

# Contenido del primer frame
    # Texto e Instruciones
subtitulo = Label(frameizquierdo,text='METODO FIX HUAWEI SIM CUBACEL')
subtitulo.pack(pady=20)
Label(frameizquierdo,text='Instrucciones').pack(anchor=W)
Label(frameizquierdo,text='1.Habilitar a depuracion usb').pack(anchor=W)
Label(frameizquierdo,text='2.Retirar la SIM CUBACEL').pack(anchor=W)
   # Boton de ayuda
ayuda = Button(frameizquierdo,text='Ayuda',command=msjAyuda)
ayuda.config(padx=50)
ayuda.pack(side=LEFT)
   # Boton de unlock
doit = Button(frameizquierdo,text='Remover',command=remover)   
doit.config(padx=50)
doit.pack(side=LEFT)



# Segundo Frame
framederecho = LabelFrame(huawei,width=350,height=600)
framederecho.config(bg='green')
framederecho.pack(side=RIGHT)
framederecho.pack_propagate(False)
huaweimg = Image.open('./imagenes/huawei.png')
img = ImageTk.PhotoImage(huaweimg)
Label(framederecho,image=img).pack()










huawei.mainloop()

