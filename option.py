import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess
from database import database

class Main_Start(tk.Tk):
    #System Window Creation 
    def __init__(self):
        super().__init__()
        self.title("OPTION")
        self.geometry("500x500")
        self.configure(bg="OrangeRed3")
        


if __name__ == "__main__":
    start = Main_Start()
    start.mainloop()
