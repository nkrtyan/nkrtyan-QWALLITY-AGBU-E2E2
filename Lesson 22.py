str1 = "abc"
str2 = "xyz"
new_str1 = str2[ :2]+str1[2 : ]
new_str2 = str1[ :2]+str2[2 : ]
print(new_str1, new_str2)