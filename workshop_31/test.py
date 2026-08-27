"""   TEST SCENARIO

Create 4 functions(calls)
1. Register non admin user
2. Login with registered non admin user
3. Add account balance
4. Check that account balance is correct

"""

import data, register_user, nonadmin_login, add_balance, checking_balance, logging
from logging_conf import setup_logging

setup_logging()
username, password = register_user.test_register_user()
default_amount = data.register_body["account"] 
header = nonadmin_login.test_login_user(username, password)
add_amount = add_balance.test_add_balance(headers=header)
final_amount = checking_balance.test_check_balance(headers=header)

if final_amount == default_amount + add_amount:
    logging.info("balance was updated")

else: 
    logging.error("balance wasn't updated")

logging.info("Test scenario finished successfully")

