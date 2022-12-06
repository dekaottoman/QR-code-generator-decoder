from tkinter import PhotoImage, filedialog
import customtkinter
import qrcode
import cv2
import os

def pop_up(msg:str):
        win = customtkinter.CTkToplevel()
        win.wm_title("For you!")
        win.maxsize(300,180)
        win.minsize(300,180)
        icon = PhotoImage("code.ico")
        win.iconbitmap(icon)

        frame = customtkinter.CTkFrame(master=win)
        frame.pack(pady=20, padx=20,fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text=msg, font=("Berlin Sans FB", 16))
        label.pack(pady=10, padx=10)

        btn = customtkinter.CTkButton(master=frame, text="OK", font=("Berlin Sans FB", 16),command=win.destroy)
        btn.pack(ipady=5,ipadx=5,pady=10,padx=10)

def generate_code(url_input:customtkinter.CTkEntry):
    url = url_input.get()
    code = qrcode.make(url)
    downloads = f"{os.getenv('USERPROFILE')}\\Downloads"
    code.save(downloads + '/code.png')
    pop_up("The QR code is at >>\n" + downloads)

def decode():
    qr_code = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("image", ".jpg"), ("image", ".jpeg"), ("image", ".png")))
    code_detector = cv2.QRCodeDetector()
    code_str, _, _ = code_detector.detectAndDecode(cv2.imread(qr_code))
    pop_up(code_str)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system")
        self.title("QR Code Generator")
        icon = PhotoImage("code.ico")
        self.iconbitmap(icon)

        height = 300
        width = 300

        self.geometry(f"{width}x{height}")
        self.minsize(300,300)
        self.maxsize(300,300)

        #self.geometry(f"{width}x{height}")
        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=20,padx=20, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="QR Code\nGenerator & Decoder", font=("Berlin Sans FB", 18))
        label.pack(pady=10, padx=10)

        url_input = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Text Here",justify="center",width=200, font=("Consolas", 16))
        url_input.pack(ipady=5,ipadx=5,pady=5)

        btn_gen = customtkinter.CTkButton(master=frame, text="Generate Code", font=("Berlin Sans FB", 16),command=lambda:generate_code(url_input))
        btn_gen.pack(ipady=5,ipadx=5,pady=10,padx=10)
        
        btn_dec = customtkinter.CTkButton(master=frame, text="Decode QR Code", font=("Berlin Sans FB", 16),command=decode)
        btn_dec.pack(ipady=5,ipadx=5,pady=10,padx=10)

        bot_label = customtkinter.CTkLabel(master=frame, text="From CSE Workshop with love ❤️\n-dekaottoman", font=("Consolas", 12))
        bot_label.pack(pady=5, padx=10)

    

if __name__ == "__main__":
    app = App()
    app.mainloop()