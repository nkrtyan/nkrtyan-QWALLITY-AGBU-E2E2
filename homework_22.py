#Find the maximum value in a list.
my_list=[45,15,56,78,14100,85,456,258,265,98,11256,56874]
maximum=my_list[0]
for number in my_list:
    if number>maximum:
        maximum=number
print("maximum_value", maximum)
# Nel, correct


#Find the minimum value in a list.
my_list=[45,15,56,78,14100,85,456,258,265,98,11256,56874]
minimum=my_list[0]
for number in my_list:
   if number<minimum:
      minimum=number
print("minimum_value", minimum)
# Nel, correct

#Calculate the sum of all elements in a list.
my_list=[45,15,56,78,14100,85,456,258,265,98,11256,56874]
summary=0
for number in my_list:
   summary=summary+number
print("sum", summary)
# Nel, correct

#Sort the list in ascending order.
my_list=[45,15,56,78,14100,85,456,258,265,98,11256,1]
for item in range(len(my_list)):
    for j in range(len(my_list) - 1):
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(my_list)