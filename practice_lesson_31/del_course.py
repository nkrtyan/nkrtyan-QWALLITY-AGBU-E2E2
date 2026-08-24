import endpoints
import requests

def test_del_course(course_id, headers):
    for attempt in range(10):

        try:        
            delete_course_response = requests.delete (endpoints.delete_course_endpoint%course_id, headers=headers)
            if delete_course_response:
                print(delete_course_response.status_code)
                print (f"{course_id} was deleted")
                print(delete_course_response.text)
                break

        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} was failed. Retrying...")

