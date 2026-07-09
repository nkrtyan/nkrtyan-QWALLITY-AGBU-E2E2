#maximum
list1 = [1, 5, 10, 14] # TODO, if the list contains 1000 number , you will have 1000 if? :) Instead use for cycle
if list1[0] < list1[1]:
    print (True)
if list1[1] < list1[2]:
    print (True)
if list1[2] < list1[3]:
    print (True)
print (max(list1))


#minimum

list1 = [1, 5, 10, 14]  # TODO, the same here
if list1[0] < list1[1]:
    print (False)
if list1[1] < list1[2]:
    print (False)
if list1[2] < list1[3]:
    print (False)
print (min(list1))

#total 1 if we have no long numbers

list1 = [1, 5, 10, 14]  # TODO, the same here
total = list1[0] + list1[1] + list1[2] + list1[3]
print(total)
# Nel, see below solution
numbers = [11, 3, 35, 64, 57, 8, 79]
total = 0
for number in numbers:
    total = total + number

print(f"Sum of the list: {total}")


#total 2

list1 = [1, 5, 10, 14] 
for item in list1:
    total = total + item 
print(total)

# TODO, task 4 is absent
