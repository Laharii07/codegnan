from accounts import user_details

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