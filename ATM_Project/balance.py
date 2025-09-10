from accounts import user_details
import single_email_transfer


def balance(user_name:int):
    if user_name in user_details:
        amount = user_details[user_name][1]
        print(f"current balance is{amount}")
        
        single_email_transfer.single_email_send(to_email =  user_details[user_name][2],
                                                subject= " KYC online net banking - Account Balance Update for A/C ",
                                                body =  " Thank you for accessing KYC net banking your balance is {amount} "
                                                )
    else:
        print("User not found")