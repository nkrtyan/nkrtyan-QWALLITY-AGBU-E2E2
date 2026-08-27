import endpoints
import data
import requests
import logging


logger = logging.getLogger(__name__)


def test_register_non_admin_user():

    register_data = data.register_body

    username = register_data["username"]
    password = register_data["password"]

    logger.info("Starting registration of non-admin user")

    for attempt in range(10):

        try:
            logger.info(f"Registration attempt {attempt + 1}/10")

            register_non_admin_user_response = requests.post(
                endpoints.register_endpoint,
                json=register_data,
                headers=data.headers
            )

            logger.info(
                f"Registration status code: "
                f"{register_non_admin_user_response.status_code}"
            )

            if register_non_admin_user_response.status_code == 201:

                logger.info("User registered successfully!")

                logger.info(
                    f"Registration response: "
                    f"{register_non_admin_user_response.json()}"
                )

                logger.info(f"Username: {username}")
                logger.info(f"Password: {password}")

                return username, password

            else:

                logger.warning(
                    f"Registration failed. "
                    f"Status code: "
                    f"{register_non_admin_user_response.status_code}"
                )

                logger.warning(
                    f"Response: "
                    f"{register_non_admin_user_response.text}"
                )

        except requests.RequestException as e:

            logger.error(
                f"Registration request failed "
                f"on attempt {attempt + 1}: {e}"
            )

    logger.error("Registration failed after 10 attempts.")

    return username, password