from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

class otp_verifier(Tk):
    def calling(self):
        self.geometry("600x550")
        self.resizable(False, False)
        self.n=random.randint(1000,9999)
        self.client=Client("AC0246d1826f74e50ce20af48b2b66b237","9ef3cbd8611415585f08b0eab2c294c4")
        self.client.messages.create(to=["+917988631834"],
                                   from_="+16073005209",
                                   body=self.n)
    def Labels(self):
        window=otp_verifier()
        self.c=Canvas(self,bg="white",width=400,height=200)
        self.c.place(x=100,y=100)
        self.Login_Title=Label(self,text="OTP verification",font=("Helvetica",20,"bold"),bg="white") #login title on top
        self.Login_Title.place(x=210,y=110)
    def Entry(self):
        self.User_Name=Text(self,borderwidth=2,wrap="word",width=29,height=2)
        self.User_Name.place(x=190,y=160)
    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit.png")
        self.submitButton=Button(self,image=self.submitButtonImage,command=self.checkOTP,border=0)
        self.submitButton.place(x=208,y=300)

        self.resendOTPImage= PhotoImage(file="resendotp.png")
        self.submitButton = Button(self, image=self.resendOTPImage, command=self.resendotp, border=0)
        self.submitButton.place(x=208, y=400)
    def checkOTP(self):
        try:
            self.userInput=int(self.User_Name.get(1.0,"end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo","Login Success")
                self.n="done"
            elif self.n=="done":
                messagebox.showinfo("showinfo","already login")
            else:
                messagebox.showinfo("showinfo","wrong OTP")
        except:
            messagebox.showinfo("showinfo","Invalid OTP")

    def resendotp(self):
        self.n = random.randint(1000, 9999)
        self.client = Client("AC0246d1826f74e50ce20af48b2b66b237", "9ef3cbd8611415585f08b0eab2c294c4")
        self.client.messages.create(to=["+917988631834"],
                                   from_="+16073005209",
                                   body=self.n)
if __name__=="__main__":
    window=otp_verifier()
    window.calling()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()
