"""
REST API + PYTHON `requests` CHEAT SHEET (bonus — in case it's on the exam too)
==================================================================================
REST API testing in Python typically uses the `requests` library.
    pip install requests
"""

import requests

BASE_URL = "https://qwallity-prod.onrender.com"

# ---------------------------------------------------------------------------
# 1. HTTP METHODS — what they're for
# ---------------------------------------------------------------------------
# GET     -> retrieve data (e.g. get a list of customers)
# POST    -> create new data (e.g. register a user, add a course)
# PUT     -> fully update/replace an existing resource
# PATCH   -> partially update an existing resource
# DELETE  -> remove a resource


# ---------------------------------------------------------------------------
# 2. GET REQUEST
# ---------------------------------------------------------------------------
def get_courses():
    response = requests.get(f"{BASE_URL}/courses/fundamental/api")
    print(response.status_code)   # e.g. 200
    print(response.json())        # parsed JSON body as a Python dict/list
    return response


# ---------------------------------------------------------------------------
# 3. POST REQUEST — sending a JSON body
# ---------------------------------------------------------------------------
def register_user(email, password):
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/register/api", json=payload)
    # `json=payload` automatically serializes the dict AND sets the
    # Content-Type: application/json header for you.
    return response


def login(email, password):
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/login/api", json=payload)
    token = response.json().get("token")   # commonly used in the next request's headers
    return token


# ---------------------------------------------------------------------------
# 4. USING HEADERS (e.g. for authentication)
# ---------------------------------------------------------------------------
def add_course(token, course_name):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"course_name": course_name}
    response = requests.post(f"{BASE_URL}/add_course/api", json=payload, headers=headers)
    return response


# ---------------------------------------------------------------------------
# 5. DELETE REQUEST — often uses a path parameter
# ---------------------------------------------------------------------------
def delete_course(course_id):
    response = requests.delete(f"{BASE_URL}/courses/course/{course_id}")
    return response


# ---------------------------------------------------------------------------
# 6. CHECKING THE RESPONSE — status codes to know
# ---------------------------------------------------------------------------
# 1XX -> Informational
# 2XX -> Success            (200 OK, 201 Created, 204 No Content)
# 3XX -> Redirection
# 4XX -> Client Error        (400 Bad Request, 401 Unauthorized, 404 Not Found)
# 5XX -> Server Error         (500 Internal Server Error)

def assert_status(response, expected=200):
    assert response.status_code == expected, (
        f"Expected {expected}, got {response.status_code}: {response.text}"
    )


# ---------------------------------------------------------------------------
# 7. A TYPICAL END-TO-END TEST FLOW (matches the course's test-suite structure)
# ---------------------------------------------------------------------------
"""
1. POST  /register/api           -> Register User
2. POST  /login/api               -> Login, get a token
3. GET   /courses/fundamental/api  -> Get Fundamental Course list (baseline)
4. POST  /add_course/api            -> Add Fundamental Course
5. GET   /courses/fundamental/api    -> Check the added course now appears in the list
6. DELETE /courses/course/{id}        -> Delete the course by its id
"""

if __name__ == "__main__":
    resp = get_courses()
    assert_status(resp, 200)
    print("GET request OK")
