from datetime import datetime


print("==========================================")
print("          TRANSACTION RECEIPT")
print("==========================================")

pin = input("Enter PIN: ")
transaction_type = input("Transaction Type (Deposit/Withdraw): ")
amount = float(input("Amount (RM): "))

date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

receipt = (
    "\n==========================================\n"
    "               ATM RECEIPT\n"
    "==========================================\n"
    f"Date        : {date_time}\n"
    f"Account     : ****{pin[-4:]}\n"
    f"Transaction : {transaction_type}\n"
    f"Amount      : RM{amount:.2f}\n"
    "Status      : SUCCESS\n"
    "==========================================\n"
    "       Thank you for using ATM!\n"
    "==========================================\n"
)

print(receipt)

with open("receipt.txt", "w") as file:
    file.write(receipt)

print("Receipt saved successfully.")