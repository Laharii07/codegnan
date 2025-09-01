operations = (
    "1.balance\n",
    "2.withdraw\n",
    "3.Deposit\n",
    "4.Transfer\n",
    "5.History\n",
    "6.logout",
    )
accounts = {12345:"laha@123",45678:"hari@123"}

user_details = {
    12345:["lahari",1000,"lahariganesula@gmail.com"],
    45678:["hari",2000,"hariganesula@gmail.com"]
}

def login(user_name:int, password:str):
    if user_name in accounts:
        if accounts[user_name] == password:
            print("successfully logged in to KYC online Net Banking")
            return True
        else:
            print("Wrong Password, check your credentials")
    else:
        print("User not Found")
    return False
def balance(user_name:int):
    if user_name in user_details:
        amount = user_details[user_name][1]
        print(f"current balance is{amount}")
    else:
        print("User not found")
    
def withdraw(user_name: int, withdraw_amount: int):
    if user_name in user_details:
        amount = user_details[user_name][1]
        if withdraw_amount <=amount:
            user_details[user_name][1] -= withdraw_amount
            print(f"successfully withdraw your amount {withdraw_amount}")
            print(f"current balance is {user_details[user_name][1]}")
        else:
            print("Insufficent amount in your account")
    else:
        print("User not found")
    
def deposite(user_name: int, deposite_amount: int):
    if user_name in user_details:
        user_details[user_name][1] +=deposite_amount
        print(f"current balance is {user_details[user_name][1]}")
    else:
        print("User not Found")
   
def transfer(user_name:int, to_account: int, transfer_amount: int):
    if user_name in user_details:
        if to_account in user_details:
            amount = user_details[user_name][1]
            if transfer_amount<=amount:
                user_details[user_name][1] -= transfer_amount
                user_details[to_account][1] += transfer_amount
                print(f"current balance is {user_details[user_name][1]}")
            else:
                print(f"Insufficent amount in {user_name}")
        else:
            print(f"{to_account} user not found")

    else:
        print(f"{user_name} user not found")

def history(user_name: int):
    print("Development under processing.........")
    
def logout():
    print("user successfully logout")
    exit()
    pass

if __name__=="__main__":
    print("Welcome to the KYC online banking app")
    account = int(input("Please enter Account Number:"))
    password = input("Please enter your Password:")
    if login(user_name = account, password =password):
        while True:
            print(*operations)
            choice = int(input("Please select your opearation:"))

            if choice == 1:
                balance(user_name = account)
            elif choice == 2:
                amount = int(input("please enter your withdraw amount:"))
                withdraw(user_name=account, withdraw_amount=amount)
            elif choice == 3:
                amount = int(input("please enter your deposite amount:"))
                deposite(user_name = account, deposite_amount = amount)
            elif choice == 4:
                reciver_account = int(input("please enter your reciver account number:"))
                amount = int(input("please enter your transfer amount:"))

                transfer(user_name = account, to_account = reciver_account, transfer_amount = amount)
            elif choice == 5:
                history(user_name = account)
            elif choice == 6:
                logout()
            else:
                print("Please enter between 1-6:")
            break  