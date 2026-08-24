import endpoints
import json
import requests

def test_get_added_course(course_id, headers):
    for attempt in range(10):
        try:
            get_added_course_response = requests.get(endpoints.check_course_endpoint, headers=headers)

            if get_added_course_response:
                all_courses = json.loads(get_added_course_response.text)

                for item in all_courses['result']:
                    if int(course_id) == item["id"]:
                        print("New course was added")
                    break
                break
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}: Login failed. Retrying...")