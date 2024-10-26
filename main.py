from tkinter import*
import qrcode
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import random
win=Tk()
c=0
file=''
def erase2(event):
    global c
    if c==0:
        textt.delete('1.0',END)
        clrbutton.pack(pady=5)
        c+=1
    else:
        pass
    
def erase(event):
    fname.delete('0',END)

def clr():
    textt.delete('1.0',END)
    
def generate_qr_code():
    global file
    text = textt.get('1.0',END)
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    coloropt=["#641e16",'#512e5f','#4a235a','#154360','#1b4f72','#0b5345','#f1c40f','#f39c12','#F08080']
    color=random.choice(coloropt)
    img = qr.make_image(fill_color=color, back_color="white")
    file=img
    img_tk = ImageTk.PhotoImage(img)
    imglbl.pack(pady=10)
    imglbl.config(image=img_tk)
    imglbl.image = img_tk
    
    textt.pack_forget()
    scrollbary.place_forget()
    clrbutton.pack_forget()
    fname.pack_forget()
    genbutton.pack_forget()
    regenbutton.pack(pady=(20,5),side=LEFT,padx=(70,30))
    svgenbutton.pack(pady=(20,5),side=LEFT)
def regen():
    global c
    c=0
    imglbl.pack_forget()
    regenbutton.pack_forget()
    svgenbutton.pack_forget()
    textt.pack(pady=20)
    scrollbary.place(x=324,y=74,height=90,width=15)
    clrbutton.pack_forget()
    clr()
    fname.delete('0',END)
    fname.pack()
    genbutton.pack(pady=(20,5))
    
def svimg():
    if len(fname.get().strip()+".png")>4:
        name=fname.get().strip()+".png"
        path=os.getcwd()+"\QR codes"
        img_path = os.path.join(path,name)
        file.save(img_path)
        messagebox.showinfo("File info", "Image saved successfully.")
    else:
        messagebox.showwarning("Save Error", "Please enter file name.")
win.geometry("600x600")
win.config(bg="#1b2631")
win.title("Message to QR")
win.iconbitmap("qr.ico")

content_frame=Frame(win,bg="#1b2631",height=600,width=600)
content_frame.propagate(True)
content_frame.pack()
headlbl=Label(content_frame,text="MESSAGE to QR",font=("Arial Black",12),fg="#2ecc71",bg="#1b2631")
headlbl.pack(pady=(20,5))
line=Frame(content_frame,height=2,width=400,bg='white')
line.pack()
imglbl=Label(content_frame)

textt=Text(content_frame,font=("Arial Narrow",12,'bold'),height=5,width=30,
           bg="#ebedef",fg="#512e5f",relief='ridge',bd=5)
textt.pack(pady=20)
scrollbary=Scrollbar(content_frame,orient='vertical',command=textt.yview,bg='#148f77')
scrollbary.place(x=315,y=74,height=110,width=15)
textt['yscrollcommand']=scrollbary.set

textt.insert(END,"Enter your message!")
textt.bind('<ButtonRelease>',erase2)
clrbutton=Button(content_frame,text="Clear",font=("Bahnschrift",12),width=15,
                 fg="white",bg="#c0392b",cursor="hand2",command=clr)

preset=StringVar()
fname=Entry(content_frame,width=40,textvariable=preset)
fname.pack()
fname.bind('<ButtonRelease>',erase)
preset.set(value="Enter your filname")

genbutton=Button(content_frame,text="Generate",font=("Bahnschrift",12),width=15,
                 fg="white",bg="#2ecc71",cursor="hand2",command=generate_qr_code)
genbutton.pack(pady=(20,5))

regenbutton=Button(content_frame,text="Regenerate",font=("Bahnschrift",12),width=15,
                 fg="white",bg="#2ecc71",cursor="hand2",command=regen)

svgenbutton=Button(content_frame,text="Save",font=("Bahnschrift",12),width=10,
                 fg="white",bg="#2874a6",cursor="hand2",command=svimg)

win.mainloop()