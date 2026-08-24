import register_user
import login
import add_balance
import check_balance

username, password = register_user.test_register_user()

headers = login.test_login_user(username, password)

if headers:
    add_balance.test_add_balance(headers)
    
    
    check_balance.test_check_balance(headers)

print("Test scenario is finished successfully!")
