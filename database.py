def database(pin):
    DB = "database.txt"
    
    with open(DB, "r") as file:
        for line in file:
            data = line.strip().split(",")
            
            
            if data[0] == pin:
                return data[1]
    return None


#Just some testing
#pin = input("Enter PIN: ")
#amount = database(pin)
#print("Amount:", amount)