# Project Name = QRcode Generator
# Developed By B SAI SANNIDH

from tkinter import *       # importing modules
from tkinter import messagebox
import qrcode

def qr():    # Defining qr function
    data = text.get()
    qrc = qrcode.make(data)
    loc = location.get() + "\\" + name.get()
    qrc.save(f'{loc}.png')
    messagebox.showinfo("QR CODE GENERATOR", "Qr code is successfully generated")

wn = Tk() # Main Window
wn.title("QRCodeGenerator")
wn.geometry('1280x720')
wn.config(bg="grey")


hf = Frame(wn,bg="grey")
hf.place(relx=0, rely=0.05,relwidth=1,relheight=0.15)
#hf.pack()

hl = Label(hf, text="Generate QR Code", bg='grey', font=('Times',40,'bold'))
hl.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)


hf1 = Frame(wn,bg="grey")
hf1.place(relx=0,rely=0.25,relwidth=1,relheight=0.15)
lbl = Label(hf1, text="Text/URL : ", bg='grey', font=('Times',20))
lbl.place(relx=0,rely=0.3,relwidth=0.4,relheight=0.5)
text = Entry(hf1, font=('Times',20))
text.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)

hf2 = Frame(wn,bg="grey")
hf2.place(relx=0,rely=0.45,relwidth=1,relheight=0.15)
lbl1 = Label(hf2, text="Location : ", bg='grey', font=('Times',20))
lbl1.place(relx=0,rely=0.3,relwidth=0.4,relheight=0.5)
location = Entry(hf2, font=('Times',20))
location.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)

hf3 = Frame(wn,bg="grey")
hf3.place(relx=0,rely=0.65,relwidth=1,relheight=0.15)
lbl2 = Label(hf3, text="Name : ", bg='grey', font=('Times',20))
lbl2.place(relx=0,rely=0.3,relwidth=0.4,relheight=0.5)
name = Entry(hf3, font=('Times',20))
name.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)


hf4 = Frame(wn,bg="grey")
hf4.place(relx=0,rely=0.85,relwidth=1,relheight=0.15)
butn = Button(hf4, text="Generate", activebackground="steelblue3", activeforeground="red", command=qr)
butn.place(relx=0.45,rely=0,relwidth=0.07,relheight=0.5)


f1 = Frame(wn, )
wn.mainloop()
