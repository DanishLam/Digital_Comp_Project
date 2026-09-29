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
        
        
        L = Label(self, text= "Enter Pin:")
        L.config(font=("Courier", 14),
                 height= 2)
        
        self.Pin = Entry(self,
                    show="*")
            
        btn = Button(self, 
                     text="Test", 
                     height= 3,
                     width= 15,
                     command= self.btn_switch)
        
        
        L.place(x=100, y=100)
        self.Pin.place(x=250, y=110)
        btn.place(x=175, y=175)
        
    def btn_switch(self):
        Pin_Input = self.Pin.get()
        
        with open(DB, "r") as file:
            for line in file:
                data = line.strip().split(",")
            
                if Pin_Input == data[0]:
                    subprocess.Popen(["python", "option.py"])
                    self.destroy()
                    
                else:
                    print("Error")
        return None 

if __name__ == "__main__":
    start = Main_Start()
    start.mainloop()
