my_list=[1,3,4,3,9,7,8,7,4]
u_list=[]
for num in my_list:
    if num not in u_list:
        u_list.append(num)
print(u_list)