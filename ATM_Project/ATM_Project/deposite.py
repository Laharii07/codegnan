from accounts import user_details 
import single_email_transfer   
def deposite(user_name: int, deposite_amount: int):
    if user_name in user_details:
        user_details[user_name][1] += deposite_amount
        print(f"current balance is {user_details[user_name][1]+deposite_amount}")
        subject = " KYC online net banking – Account deposite Update for A/C "
        body = " Thank you for accessing KYC net banking your balance is{user_details[user_name][1]} "
        email = user_details[user_name][2]
        single_email_transfer.single_email_send(to_email = email,subject=subject,body = body)
    else:
        print("User not Found")
