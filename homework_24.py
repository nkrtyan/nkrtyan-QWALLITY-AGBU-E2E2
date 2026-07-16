"""1. Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
"""
a=0
b=1
list100=[a, b]
for item in range(0, 50):
    while a+b<50:
        a, b = b, b+a
        list100.append(b)
print(list100)
# Nel, correct,  we no need to append to the list, or cycle to loop and print elements next to each other

"""2. Write a Python program that accepts a string and calculates the number of digits and letters.  
Sample Data: Python 3.13
Expected Output:
Letters 6
Digits 3
"""
listletters=[]
listdigits=[]
for let in "Python 3.13":
    if let.isalpha():
        listletters.append(let)
    elif let.isdigit():
        listdigits.append(let)
print("Letters" , len(listletters))
print("Digits" , len(listdigits))
# Nel, corerct

"""3. Write a Python program to print alphabet pattern 'L'  
Expected Output:
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*****  """
for items in range (1,8):
    if items<7:
        print("*", end="\n")
      
    else:
        print("* "*5)
# Nel, correct

   