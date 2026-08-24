import register_user, login_user, add_balance, get_balance
from logger_config import logger
username, password = register_user.test_register_user()

header = login_user.test_login_user(username, password)
add_balance.test_add_balance(headers=header)
get_balance.test_get_balance(headers=header)

logger.info("Test scenario is finished successfuly")
print("Test scenario is finished successfuly")