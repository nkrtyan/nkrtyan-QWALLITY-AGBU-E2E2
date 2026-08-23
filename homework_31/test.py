from register_user import test_register_user
from login import test_login_user
from add_balance import test_add_balance
from check_balance import test_check_balance, get_current_balance


def test_full_balance_flow():
    test_register_user()
    test_login_user()
    balance_before = get_current_balance()
    test_add_balance()
    test_check_balance(balance_before)


test_full_balance_flow()