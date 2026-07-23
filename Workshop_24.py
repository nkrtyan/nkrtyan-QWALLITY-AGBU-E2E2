number_list = [18, 2, 100, 44, 5]
input_num = int(input("Enter a number: "))
if input_num in number_list:
    if input_num%2 == 0:
        print(f"The number {input_num} is even.")
    else:
        print(f"The number {input_num} is odd.")
    print(f"The number {input_num} exists in the list.")
else:
    print(f"The number {input_num} is not in the list.")
