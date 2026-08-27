"""   TEST SCENARIO

Create 4 functions(calls)
1. Register non admin user
2. Login with registered non admin user
3. Add account balance
4. Check that account balance is correct

"""

import register_user, nonadmin_login, add_balance, checking_balance, logging


username, password, default_account = register_user.test_register_user()
header = nonadmin_login.test_login_user(username, password)
add_amount = add_balance.test_add_balance(headers=header)
final_amount = checking_balance.test_check_balance(headers=header)


if final_amount == default_account + add_amount:
    logging.info("Balance was updated")

else: 
    logging.error("Balance wasn't updated")

logging.info("Test scenario finished successfully")

