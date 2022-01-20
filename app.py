import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import qrcode
import cv2
import os

root = tk.Tk()
root.title("QR Code Generator")
root.minsize(300,485)
root.maxsize(300,485)
icon = tk.PhotoImage("icon.ico")
root.iconbitmap(icon)

if os.name == "nt":
    downloads = f"{os.getenv('USERPROFILE')}\\Downloads"
else:
    downloads = f"{os.getenv('HOME')}/Downloads"

def pop_up(msg:str):
    win = tk.Toplevel()
    win.wm_title("For you!")
    win.maxsize(300,150)
    win.minsize(300,150)
    win.iconbitmap(icon)

    l = tk.Label(win, text=msg)
    l.place(relwidth=1, relheight=0.2, rely=0.25, relx=0)

    b = ttk.Button(win, text="OK", command=win.destroy)
    b.place(relwidth=0.5, relheight=0.2, rely=0.5, relx=0.25)

def generate_code():
    url = url_input.get()
    code = qrcode.make(url)
    code.save(downloads + '/code.png')
    pop_up("The QR code is at " + downloads)

def decode():
    qr_code = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("image", ".jpg"), ("image", ".jpeg"), ("image", ".png")))
    det = cv2.QRCodeDetector()
    code_str, _, _ = det.detectAndDecode(cv2.imread(qr_code))
    pop_up(code_str)

canvas = tk.Canvas(root, bg="#f1f2f6") 
canvas.place(relx=0,rely=0, relwidth=1, relheight=1)

app_label = tk.Label(root, bg="#b33939", fg="#f1f2f6", text="QR Code Generator/Decoder")
app_label.place(relx=0,rely=0,relwidth=1,relheight=0.075)

img = tk.PhotoImage(file="code.png")
qr_label = tk.Label(root, image=img)
qr_label.place(width=225, height=225 , rely=0.1, relx=0.125)

url_input = ttk.Entry(root, justify='center')
canvas.create_window(150,300,window=url_input, width=250, height=35)

gen_btn = ttk.Button(root, text="Generate QR Code", command=generate_code)
gen_btn.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.1)

dcode_btn = ttk.Button(root, text="Decode QR Code", command=decode)
dcode_btn.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

bottom_label = tk.Label(root, bg="#b33939", fg="#f1f2f6", text="by dekaottoman")
bottom_label.place(relx=0,rely=0.925,relwidth=1,relheight=0.075)

root.mainloop()