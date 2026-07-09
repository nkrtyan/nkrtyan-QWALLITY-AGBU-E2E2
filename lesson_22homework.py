
#maximum

list1 = [1, 5, 10, 14] 
if list1[0] < list1[1]:
    print (True)
if list1[1] < list1[2]:
    print (True)
if list1[2] < list1[3]:
    print (True)
print (max(list1))


#minimum

list1 = [1, 5, 10, 14] 
if list1[0] < list1[1]:
    print (False)
if list1[1] < list1[2]:
    print (False)
if list1[2] < list1[3]:
    print (False)
print (min(list1))

#total 1 if we have no long numbers

list1 = [1, 5, 10, 14] 
total = list1[0] + list1[1] + list1[2] + list1[3]
print(total)

#total 2

list1 = [1, 5, 10, 14]
total = 0
for item in list1:
    total = total + item 
print(total)


