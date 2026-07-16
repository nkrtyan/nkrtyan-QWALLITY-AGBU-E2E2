number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_num = int(input("enter x number"))
if input_num in number_list:
    print(f"{input_num} found in the{number_list}.")
    if input_num%2 == 0:
        print(f"{input_num} is even")
    else:
        print(f"{input_num} is odd")
else:
    print(f"{input_num} not foud in the {number_list}.")



for number in range(7):
    if number == 3 or number == 6:
        continue
    print (number, end = " ")