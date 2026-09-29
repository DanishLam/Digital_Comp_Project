import tkinter as tk
from tkinter import *
import subprocess

class Main_Start(tk.Tk):
    #System Window Creation 
    def __init__(self):
        super().__init__()
        self.title("ATM System")
        self.geometry("500x500")
        self.configure(bg="OrangeRed3")
        
        Title = Label(self, 
                      text= "Option",
                      font=("Courier", 20, "bold"),
                      width= 15,
                      bg="gold2")
        
        Balance_BTN = Button(text="Balance",
                             font=("Courier", 14),
                             command=self.balance_switch,
                             width=12)
        
        Withdraw_BTN = Button(text="Withdraw",
                             font=("Courier", 14),
                             command=self.withdraw_switch,
                             width=12)
        
        Deposit_BTN = Button(text="Deposit",
                             font=("Courier", 14),
                             command=self.deposit_switch,
                             width=12)
        
        Exit_BTN = Button(text="Exit",
                             font=("Courier", 14),
                             command=self.exit_switch,
                             width=12)
        
        Title.place(x=135, y=50)
        Balance_BTN.place(x= 185, y=150)
        Withdraw_BTN.place(x= 185, y=200)
        Deposit_BTN.place(x= 185, y=250)
        Exit_BTN.place(x= 185, y=300)

    def balance_switch(self):
        subprocess.Popen(["python", "balance.py"])
        self.destroy()
        
    def withdraw_switch(self):
        subprocess.Popen(["python", "withdraw.py"])
        self.destroy()
        
    def deposit_switch(self):
        subprocess.Popen(["python", "deposit.py"])
        self.destroy()
        
    def exit_switch(self):
        self.destroy()


if __name__ == "__main__":
    start = Main_Start()
    start.mainloop()
