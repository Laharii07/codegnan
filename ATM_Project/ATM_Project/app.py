
import single_email_transfer
import login
import withdraw 
import transfer
import logout
import history
import deposite
import balance

operations = (
    "1.balance\n",
    "2.withdraw\n",
    "3.Deposit\n",
    "4.Transfer\n",
    "5.History\n",
    "6.logout",
    )


if __name__=="__main__":
    print("Welcome to the KYC online banking app")
    account = int(input("Please enter Account Number:"))
    password = input("Please enter your Password:")
    if login.login(user_name = account, password =password):
        while True:
            print(*operations)
            choice = int(input("Please select your opearation:"))

            if choice == 1:
                balance.balance(user_name = account)
            elif choice == 2:
                amount = int(input("please enter your withdraw amount:"))
                withdraw.withdraw(user_name=account, withdraw_amount=amount)
            elif choice == 3:
                amount = int(input("please enter your deposite amount:"))
                deposite.deposite(user_name = account, deposite_amount = amount)
            elif choice == 4:
                reciver_account = int(input("please enter your reciver account number:"))
                amount = int(input("please enter your transfer amount:"))
                transfer.transfer(user_name = account, to_account = reciver_account, transfer_amount = amount)
            elif choice == 5:
                history.history(user_name = account)
            elif choice == 6:
                logout.logout()
            else:
                print("Please enter between 1-6:")
             