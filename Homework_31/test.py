import register_user, login, add_course, get_fundamental_courses, delete_course


register_user.test_register_user()
header = login.test_login_user()
course_id = add_courses.test_add_course(headers = header)
get_fundamental_courses.test_get_fund_courses(course_id = course_id, headers = header)
delete_course.test_delete_course(course_id = course_id, headers = header)
print("Test scenario is finished successfully!")