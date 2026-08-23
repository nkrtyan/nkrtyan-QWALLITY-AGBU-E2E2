import register_user
import login
import add_balance

username, password = register_user.test_register_user()

header = login.test_login_user(username, password)

add_balance.test_add_balance(headers=header)

print("Test scenario finished successfully!")