"""test scenario"""
import data, register_user, nonadmin_login, add_balance, checking_balance

username, password = register_user.test_register_user()
default_amount = data.register_body["account"] 
header = nonadmin_login.test_login_user(username, password)
add_amount = add_balance.test_add_balance(headers=header)
final_amount = checking_balance.test_check_balance(headers=header)

if final_amount == default_amount + add_amount:
    print("balance was updated")

else: 
    print("balance wasn't updated")

print("Test scenario finished successfully")