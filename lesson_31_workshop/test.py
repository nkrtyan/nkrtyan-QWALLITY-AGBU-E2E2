"""
Test Scenario: E2E User Balance Top-Up
    1. Register non-admin user
    2. Login user & get auth header
    3. Add balance to account
    4. Get updated balance
    5. Verify: final_balance == default_balance + added_amount
"""

import register_user, login_user, add_balance, get_balance 
from logger_config import setup_logging
import logging

setup_logging()
username, password, default_amount = register_user.test_register_user() 
header = login_user.test_login_user(username, password)
add_amount = add_balance.test_add_balance(headers=header)
final_amount = get_balance.test_get_balance(headers=header)

if final_amount == default_amount + add_amount:
    logging.info(f"{final_amount} = {default_amount} + {add_amount}")
    logging.info("Balance added successfuly")
else:
    logging.info(f"{final_amount} != {default_amount} + {add_amount}")
    logging.error("Balance is not added")

logging.info("Test scenario is finished successfuly")
print("Test scenario is finished successfuly")