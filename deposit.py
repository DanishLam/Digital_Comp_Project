
import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, InvalidOperation
from pathlib import Path

DB = Path(__file__).resolve().parent / "database.txt"


# Find the account linked to the entered PIN
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


# Update the correct account without changing other accounts
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


class Deposit(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("ATM Deposit")
        self.geometry("450x350")
        self.configure(bg="OrangeRed3")

        title = tk.Label(
            self,
            text="Money Deposit",
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
            text="Deposit (RM):",
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

        deposit_button = tk.Button(
            self,
            text="Deposit",
            font=("Courier", 12),
            width=15,
            command=self.deposit_money
        )
        deposit_button.place(x=145, y=225)

        exit_button = tk.Button(
            self,
            text="Exit",
            font=("Courier", 12),
            width=15,
            command=self.destroy
        )
        exit_button.place(x=145, y=280)

    def deposit_money(self):

        pin = self.pin_entry.get().strip()
        amount_text = self.amount_entry.get().strip()

        # Validate PIN
        try:
            balance = get_balance(pin)
        except OSError:
            messagebox.showerror(
                "Error",
                "Unable to read the account database."
            )
            return

        if balance is None:
            messagebox.showerror(
                "Error",
                "Invalid PIN."
            )
            return

        # Validate deposit amount
        try:
            amount = Decimal(amount_text)

            if not amount.is_finite():
                raise ValueError

            if amount <= 0:
                raise ValueError

            if amount.as_tuple().exponent < -2:
                raise ValueError

        except (InvalidOperation, ValueError):
            messagebox.showerror(
                "Error",
                "Enter a valid positive amount with "
                "a maximum of two decimal places."
            )
            return

        # Calculate and save new balance
        new_balance = balance + amount
        # Ask customer to confirm the transaction
        confirm = messagebox.askyesno(
            "Confirm Deposit",
            f"Current Balance: RM {balance:.2f}\n"
            f"Deposit Amount: RM {amount:.2f}\n"
            f"New Balance: RM {new_balance:.2f}\n\n"
            "Do you want to proceed?"
            )
        if not confirm:
            messagebox.showinfo(
                "Cancelled",
                "Your deposit has been cancelled."
                )
            return
        
        try:
            success = update_balance(pin, new_balance)
        except OSError:
            messagebox.showerror(
                "Error",
                "Unable to save your deposit."
            )
            return

        if not success:
            messagebox.showerror(
                "Error",
                "Account could not be updated."
            )
            return

        # Confirm successful deposit
        messagebox.showinfo(
            "Deposit Successful",
            f"Amount Deposited: RM {amount:.2f}\n"
            f"New Balance: RM {new_balance:.2f}"
        )

        # Optional receipt
        receipt = messagebox.askyesno(
            "Receipt",
            "Would you like to view your receipt?"
        )

        if receipt:
            messagebox.showinfo(
                "Transaction Receipt",
                "========== ATM RECEIPT ==========\n"
                "Transaction: Deposit\n"
                f"Amount: RM {amount:.2f}\n"
                f"Previous Balance: RM {balance:.2f}\n"
                f"New Balance: RM {new_balance:.2f}\n"
                "Status: Successful\n"
                "==============================="
            )

        self.amount_entry.delete(0, tk.END)


if __name__ == "__main__":
    start = Deposit()
    start.mainloop()
