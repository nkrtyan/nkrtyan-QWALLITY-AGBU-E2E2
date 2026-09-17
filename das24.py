my_list=[1,4,15,6,8,19,56,3]
input_num=int(input("enter a number"))
if input_num in my_list:
    print(f"{input_num} found in the {my_list}.")
    if input_num%2==0:
        print(f"{input_num} is even" )
    else:
        print(f"{input_num} is odd")
else:
    print(f"{input_num} not found in the {my_list}")


    