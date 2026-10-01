import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess



DB = "database.txt"

class Main_Start(tk.Tk):
    #System Window Creation 
    def __init__(self):
        super().__init__()
        self.title("ATM Protocal")
        self.geometry("450x350")
        self.configure(bg="OrangeRed3")
        
        
        self.L = Label(self, text= "Enter Pin:")
        self.L.config(font=("Courier", 14),
                 height= 1)
        
        self.Pin = Entry(self,
                    show="*")
            
        self.btn = Button(self, 
                     text="Enter", 
                     height= 2,
                     width= 15,
                     command= self.btn_switch)
        self.T = Label(self,
                  text= "Invalid PIN",
                  font=("Courier", 14),
                  bg="gold2",)

        
        
        
        self.L.place(x=100, y=107)
        self.Pin.place(x=250, y=110)
        self.btn.place(x=175, y=175)
        self.T.place_forget()
        
    def btn_switch(self):
        Pin_Input = self.Pin.get()
        
        with open(DB, "r") as file:
            for line in file:
                data = line.strip().split(",")
            
                if Pin_Input == data[0]:
                    subprocess.Popen(["python", "option.py"])
                    self.destroy()
                    
                elif Pin_Input != data[0]:
                    self.L.place(x=100, y=125)
                    self.Pin.place(x=250, y=129)
                    self.btn.place(x=175, y=185)
                    self.T.place(x=170, y=50)
        return None 

if __name__ == "__main__":
    start = Main_Start()
    start.mainloop()
