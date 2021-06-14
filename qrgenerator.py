import pyotp
import pyqrcode

def display():
    uri = pyotp.totp.TOTP('base32secret3232') \
        .provisioning_uri(name='user', issuer_name='qrgenerator')
    url = pyqrcode.create(uri)
    url.svg('qr.svg', scale=8)
    url.eps('qr.eps', scale=2)
    print(url.terminal(quiet_zone=1))
# import tkinter as tk
# 
# 
# class QRLabel(tk.Label):
    # def __init__(self, parent, qr_data):
        # super().__init__(parent)
# 
        # print('QRCodeLabel("{}")'.format(qr_data))
# 
        # uri = pyotp.totp.TOTP('base32secret3232') \
            # .provisioning_uri(name='user', issuer_name='qrgenerator')
        # qr_uri = pyqrcode.create(uri)
        # png_qr = 'QRCode.png'
        # qr_uri.png(png_qr, scale=8)
# 
        # self.image = tk.PhotoImage(file=png_qr)
        # self.configure(image=self.image)
# 
# 
# class DisplayQR(tk.Tk):
    # def __init__(self):
        # super().__init__()
# 
        # button_qr = tk.Button(text="Show", bg="white", command=self.display)
        # button_qr.grid(row=2, column=0)
        # self.qr_label = None
# 
    # def display(self):
        # if self.qr_label:
            # self.qr_lable.destroy()
        # self.qr_label = QRLabel(self, "QR code")
        # self.qr_label.grid(row=1, column=0)
# 
# 
if __name__ == '__main__':
    display()
    # DisplayQR().mainloop()
