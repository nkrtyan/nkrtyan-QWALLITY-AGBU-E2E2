import register_user
import login
import Lesson_31_homework.add_balance as add_balance
import check_balance


register_user.test_register_user()
header = login.test_login_user()
add_balance.test_add_balance(headers=header)
check_balance.test_check_balance(headers=header)

print("Test scenario is finished successfully!")