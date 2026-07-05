age = int(input("How old are you? "))
decades = age // 10
years = age % 10
print("You are %s decades and %s year(s) old" % (decades, years))
print("You are {} decades and {} year(s) old".format(decades, years))
print(f"You are {decades} decades and {years} year(s) old")