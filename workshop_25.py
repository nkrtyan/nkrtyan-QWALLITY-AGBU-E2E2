#1
num=int(input("Insert nunber:"))
for i in range(1,10):
    mult=num*i
    print(f"{num}*{i}={mult}")



#2
for item in range(1,10):
    for a in range(item):
        print(item, end="")
    print()