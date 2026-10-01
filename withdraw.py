import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, InvalidOperation
import subprocess


DB = "database.txt"


 #find acc balance linked to the pin num
def get_balance(pin):
    with open(DB, "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) >= 2 and data[0].strip() == pin:
                try:
                    return Decimal(data[1].strip())
                except InvalidOperation:
                    return None

    return None


#update selected ammount in db
def update_balance(pin, new_balance):
    with open(DB, "r") as file:
        lines = file.readlines()

    updated = False

    for index, line in enumerate(lines):
        data = line.strip().split(",")

        if len(data) >= 2 and data[0].strip() == pin:
            lines[index] = f"{pin},{new_balance:.2f}\n"
            updated = True
            break

    if not updated:
        return False

    with open(DB, "w") as file:
        file.writelines(lines)

    return True


class Withdraw(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("ATM Withdrawal")
        self.geometry("450x350")
        self.configure(bg="OrangeRed3")

        title = tk.Label(
            self,
            text="Money Withdrawal",
            font=("Courier", 20, "bold"),
            width=20,
            bg="gold2"
        )
        title.place(x=60, y=35)

        pin_label = tk.Label(
            self,
            text="Enter PIN:",
            font=("Courier", 14),
            bg="OrangeRed3"
        )
        pin_label.place(x=45, y=110)

        self.pin_entry = tk.Entry(
            self,
            show="*",
            font=("Courier", 14),
            width=15
        )
        self.pin_entry.place(x=215, y=110)

        amount_label = tk.Label(
            self,
            text="Withdraw (RM):",
            font=("Courier", 14),
            bg="OrangeRed3"
        )
        amount_label.place(x=45, y=165)

        self.amount_entry = tk.Entry(
            self,
            font=("Courier", 14),
            width=15
        )
        self.amount_entry.place(x=215, y=165)

        withdraw_button = tk.Button(
            self,
            text="Withdraw",
            font=("Courier", 12),
            width=15,
            command=self.withdraw_money
        )
        withdraw_button.place(x=145, y=225)

        back_button = tk.Button(
            self,
            text="Back",
            font=("Courier", 12),
            width=15,
            command=self.go_back
        )
        back_button.place(x=145, y=280)

    def withdraw_money(self):

        pin = self.pin_entry.get().strip()
        amount_text = self.amount_entry.get().strip()

