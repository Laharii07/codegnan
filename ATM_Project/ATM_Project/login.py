from accounts import accounts
from accounts import user_details

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