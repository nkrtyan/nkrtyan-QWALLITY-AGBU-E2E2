my_list=[45,15,56,78,14100,85,456,258,265,98,11256,56874]
new_num = int (input("Enter a number:"))
if new_num in my_list:
    print (f"The number {new_num} exists in the list.")
else:
    print(f"The number {new_num} is not in the list.")

if new_num % 2 ==0:
    print(f"The number {new_num} is even.")
else: print (f"The number {new_num} is odd.")
    
