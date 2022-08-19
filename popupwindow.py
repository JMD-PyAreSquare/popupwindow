from tkinter import *

def flash(icon, title, msg, width, height, font, size):
    global popupwindow
    global popuplabel
    popupwindow = Tk()
    try:
        popupwindow.title(title)
    except:
        pass
    try:
        popupwindow.iconbitmap(icon)
    except:
        pass
    popupwindow.geometry(f'{width}x{height}')
    popupwindow.minsize(width,height)
    popupwindow.maxsize(width,height)
    popuplabel = Label(popupwindow, text=msg, font=(font, size))
    popuplabel.pack(padx=5, pady=5)
    popupwindow.mainloop()


