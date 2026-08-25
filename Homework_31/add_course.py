import requests
import endpoints
import data


def test_add_course(headers):
    for attempt in range(10):
        try:
            add_course_response = requests.post(endpoints.add_course_endpoint, json=data.course_body, headers=headers)
            course_id = add_course_response.json().get("id")

            if course_id:
                print(f"{course_id} Course added successfully.")
                break

        except requests.RequestException as e:
            print(e)

    return course_id
