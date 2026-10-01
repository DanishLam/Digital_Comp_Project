import tkinter as tk
from tkinter import messagebox
import subprocess

DB = "database.txt"

# Retrieve the balance linked to the entered PIN
def get_balance(pin):
    with open(DB, "r") as file:
        for line in file:
            data = line.strip().split(",")

           # Check if the PIN matches an account in the database
            if len(data) >= 2 and data[0].strip() == pin:
                return float(data[1].strip())

    return None


class Balance(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ATM Balance")
        self.geometry("450x350")
        self.configure(bg="OrangeRed3")

        title = tk.Label(
            self,
            text="Check Balance",
            font=("Courier", 20, "bold"),
            width=20,
            bg="gold2"
        )
        title.place(x=80, y=50)

        pin_label = tk.Label(
            self,
            text="Enter PIN:",
            font=("Courier", 14),
            bg="OrangeRed3"
        )
        pin_label.place(x=80, y=130)

        self.pin_entry = tk.Entry(
            self,
            show="*",
            font=("Courier", 14)
        )
        self.pin_entry.place(x=220, y=130)

        check_button = tk.Button(
            self,
            text="Check Balance",
            font=("Courier", 12),
            command=self.check_balance
        )
        check_button.place(x=145, y=190)

        back_button = tk.Button(
            self,
            text="Back",
            font=("Courier", 12),
            command=self.go_back
        )
        back_button.place(x=190, y=250)

    def check_balance(self):
        pin = self.pin_entry.get()

        balance = get_balance(pin)

      # Display an error if the PIN is not found
        if balance is None:
            messagebox.showerror(
                "Error",
                "Invalid PIN."
            )
        else:
            # Display the user's current account balance
            messagebox.showinfo(
                "Balance",
                f"Your current balance is RM {balance:.2f}"
            )

    def go_back(self):
        subprocess.Popen(["python", "option.py"])
        self.destroy()

if __name__ == "__main__":
    start = Balance()
    start.mainloop()
