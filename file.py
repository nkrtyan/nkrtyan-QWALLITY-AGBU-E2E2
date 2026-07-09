mylist=[1, 2, 3, 4]
if mylist[0] < mylist[1] and mylist[1] < mylist[2] and mylist[2] < mylist[3] and mylist[3] > mylist[0]:
    print(mylist[3], "is the maximum number")

    mylist=[1, 2, 3, 4]
if mylist[0] < mylist[1] and mylist[1] < mylist[2] and mylist[2] < mylist[3] and mylist[3] > mylist[0]:
    print(mylist[0], "is the minimum number")

mylist=[1, 2, 3, 4]
total = 0
for item in mylist:
    total += item
    print(total)


mylist=[1, 2, 3, 4]
sorted_list = sorted(mylist)
print(sorted_list[0], "is the minimum number")
print(sorted_list[-1], "is the maximum number")

