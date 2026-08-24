import data
import endpoints
import requests

def test_add_course(headers):
    for attempt in range (10):
        try:
            add_course = requests.post(endpoints.add_course_endpoint, json=data.course_body, headers=data.headers)
            course_id = add_course.json().get("id")

            if course_id:
                print(f"{course_id} course was added successfully")
                break

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt+1} failed. Retrying...")

    return course_id

