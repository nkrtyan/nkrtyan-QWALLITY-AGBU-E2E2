import register, login_admin, add_course, check_course, del_course

# register.test_register_user()
header = login_admin.test_login_admin()
course_id = add_course.test_add_course(headers=header)
# login_admin.test_login_admin()
# add_course.test_add_course()
check_course.test_get_added_course(course_id=course_id, headers=header)
del_course.test_del_course(course_id=course_id, headers=header)

# print ("Test scenario was going successfully")