import tkinter as tk
from tkinter import ttk

class Test(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Prototype")
        self.geometry("500x500")
        
        #Serach Bar 
        self.search_var = tk.StringVar() #store string here
        self.search_var.trace('w', self.filter) #filter string when write
        self.search_var = ttk.Entry(self, textvariable=self.search_var) # input box that connect to search_var
        self.search_var.pack() #show the Entry fuction
        
        #Column View 
        self.column_view = ttk.Treeview(self) #display data in hierachy tree structure and multi column tabular format
        
        #Populate Column with data
        for i in range(10):
            self.column_view.insert('', 'end', text = f'Movie {i}')
        self.column_view.pack()
        
        
        
    def filter(self, *args):
        search_query = self.search_var.get()
        search_outcome = self.column_view.get()

if __name__ == '__main__':
    root = Test()
    root.mainloop()