from accounts import user_details
import single_email_transfer
def transfer(user_name:int, to_account: int, transfer_amount: int):
    if user_name in user_details:
        if to_account in user_details:
            amount = user_details[user_name][1]
            if transfer_amount<=amount:
                user_details[user_name][1] -= transfer_amount
                user_details[to_account][1] += transfer_amount
                print(f"current balance is {user_details[user_name][1]}")
                subject = " KYC online net banking – Account transfer Update for A/C "
                body = " Thank you for accessing KYC net banking for your amount transfer is {user_details[user_name][1]} "
                email = user_details[user_name][2]
                single_email_transfer.single_email_send(to_email = email,subject=subject,body = body)
            else:
                print(f"Insufficent amount in {user_name}")
        else:
            print(f"{to_account} user not found")

    else:
        print(f"{user_name} user not found")