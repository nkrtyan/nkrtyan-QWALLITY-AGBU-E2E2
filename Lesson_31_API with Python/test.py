import logging
logging.basicConfig (
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

import register_non_admin_user
import login_non_admin_user
import Add_account_balance
import Get_account_balance


logger = logging.getLogger(__name__)


def test_api_flow():

    logger.info("========== TEST SCENARIO STARTED ==========")

    # 1. Register non-admin user
    logger.info("Step 1: Register non-admin user")

    username, password = (
        register_non_admin_user.test_register_non_admin_user()
    )

    if not username or not password:
        logger.error("Registration failed.")
        return

    # 2. Login with registered user
    logger.info("Step 2: Login with registered user")

    headers = login_non_admin_user.test_login_user(
        username,
        password
    )

    if not headers:
        logger.error("Login failed.")
        return

    # 3. Add account balance
    logger.info("Step 3: Add account balance")

    balance_response = (
        Add_account_balance.test_add_account_balance(
            headers=headers
        )
    )

    if not balance_response:
        logger.error("Adding balance failed.")
        return

    # 4. Check account balance
    logger.info("Step 4: Check account balance")

    actual_balance = (
        Get_account_balance.test_Get_account_balance(
            headers=headers
        )
    )

    if actual_balance is None:
        logger.error("Could not get account balance.")
        return

    logger.info(
        f"Account balance received successfully: {actual_balance}"
    )

    logger.info(
        "TEST SCENARIO FINISHED SUCCESSFULLY"
    )


if __name__ == "__main__":
    test_api_flow()