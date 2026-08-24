import register_user, nonadmin_login, add_balance, checking_balance

username, password = register_user.test_register_user()
header = nonadmin_login.test_login_user(username, password)
add_balance.test_add_balance(headers=header)
checking_balance.test_check_balance(headers=header)
print("Test scenario finished successfully")