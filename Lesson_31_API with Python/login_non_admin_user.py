import requests
from requests.auth import HTTPBasicAuth
import endpoints
import data
import logging


logger = logging.getLogger(__name__)


def test_login_user(username, password):

    logger.info("Starting login test")

    for attempt in range(10):

        try:
            logger.info(f"Login attempt {attempt + 1}/10")

            login_response = requests.post(
                endpoints.login_endpoint,
                auth=HTTPBasicAuth(
                    username=username,
                    password=password
                )
            )

            logger.info(
                f"Login response status code: "
                f"{login_response.status_code}"
            )

            if login_response.status_code == 200:

                token = login_response.json().get("token")

                if token:
                    logger.info("Login successful.")

                    data.headers["Authorization"] = f"Bearer {token}"

                    logger.info("Authorization header added.")

                    return data.headers

                logger.warning("Token was not received.")

            else:
                logger.warning(
                    f"Login failed. Response: "
                    f"{login_response.text}"
                )

        except requests.RequestException as e:

            logger.error(
                f"Login request failed on attempt "
                f"{attempt + 1}: {e}"
            )

    logger.error("Login failed after 10 attempts.")

    return None