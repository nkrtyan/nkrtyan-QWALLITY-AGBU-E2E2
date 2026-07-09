string1 = "abc"
string2 = "xyz"
string3 = string1[0:2] + string2 [-1]
print(string3)
string4 = string2[0:2] + string1[-1]
print(string4)
string5 = f"{string4} {string3}"
print(string5)