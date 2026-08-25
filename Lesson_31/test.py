import register_non_admin_user
import login_non_admin_user
import Add_account_balance
import Get_account_balance


username, password = register_non_admin_user.test_register_non_admin_user()

header = login_non_admin_user.test_login_non_admin_user(
    username,
    password
)

Add_account_balance.test_Add_account_balance(headers=header)

Get_account_balance.test_Get_account_balance(headers=header)

print("Test scenario is finished successfully")