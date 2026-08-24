import registor_user
import login
import add_balance
import check_balance

registor_user.test_registor_user()
header = login.test_login_user()
add_balance.test_add_balance(headers=header)
check_balance.test_check_balance(headers=header)
print("Test scenario is finished successfully!")