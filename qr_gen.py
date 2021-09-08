import tkinter as tk
from tkinter import filedialog
import qrcode
import cv2
import os

root = tk.Tk()
root.maxsize(400,800)
root.minsize(400,800)
root.title('QR Code Generator')

if os.name == "nt":
    downloads = f"{os.getenv('USERPROFILE')}\\Downloads"
else:
    downloads = f"{os.getenv('HOME')}/Downloads"

def generate_code():
    url = url_input.get()
    code = qrcode.make(url)
    code.save(downloads + '/code.png')
    export_label = tk.Label(root, text="The QR code is at " + downloads, font=10, bg="#82ccdd", fg="#0a3d62")
    export_label.place(relheight=0.075, relwidth=1, relx=0, rely=0)

def decode():
    qr_code = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("image", ".jpg"), ("image", ".jpeg"), ("image", ".png")))
    det = cv2.QRCodeDetector()
    code_str, _, _ = det.detectAndDecode(cv2.imread(qr_code))
    export_label = tk.Label(root, text=code_str, font=("Sans Serif",12), bg="#82ccdd", fg="#0a3d62")
    export_label.place(relheight=0.075, relwidth=1, relx=0, rely=0.275)

canvas = tk.Canvas(root, width=400, height=800, bg="#f1f2f6")
canvas.pack()

url_label = tk.Label(root, text="Enter the string to be coded below", font=10, bg="#82ccdd", fg="#0a3d62")
url_label.place(relheight=0.075, relwidth=1, relx=0, rely=0)

url_input = tk.Entry(root)
canvas.create_window(200,100,window=url_input, width=250, height=35)

btn = tk.Button(root, text="Generate Code", font=7, bg="#82ccdd", fg="#0a3d62", command=generate_code)
btn.place(relwidth=0.7, relheight=0.075, relx=0.15, rely=0.175)

export_label = tk.Label(root, text="Load QR code to Decode", font=10, bg="#82ccdd", fg="#0a3d62")
export_label.place(relheight=0.075, relwidth=1, relx=0, rely=0.275)

btn = tk.Button(root, text="Load QR Code", font=7, bg="#82ccdd", fg="#0a3d62", command=decode)
btn.place(relwidth=0.7, relheight=0.075, relx=0.15, rely=0.375)

img = tk.PhotoImage(file="dekaottoman.png")
qr_label = tk.Label(root, image=img)
qr_label.place(relwidth=0.8, relheight=0.4 , rely=0.5, relx=0.1)

dekaottoman = tk.Label(root, text="By dekaottoman", font=10, bg="#82ccdd", fg="#0a3d62")
dekaottoman.place(relheight=0.075, relwidth=1, relx=0, rely=0.925)

root.mainloop()