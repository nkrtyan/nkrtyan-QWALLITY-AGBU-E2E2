import endpoints
import json
import requests

def test_get_fund_courses(course_id, headers)
    for attempt in range(10)
    
    try:
        test_get_fund_courses_response = requests.get(endpoints.get_fund_courses_endpoint, headers=headers)

        if get_fund_courses_response:
            all_fund_courses = json.loads(get_fund_courses_response.text)

            for i in all_fund_courses["result"]:
                if int(course_id) == i["id"]:
                    print(f'New added course exists in list.')
                    break
                break
    except requests.RequestException as e:
        print(f'')