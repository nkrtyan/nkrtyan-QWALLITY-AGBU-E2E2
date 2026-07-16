# 1
my_list=[]
a,b=0,1
while(b<50):
    a, b = b, a+b
    my_list.append(a)
print(my_list)
# 2
string = input ("enter text:")
n=len(string)
# 3
for i in range(7):
    print("*")
if(i==6):
    print("*****")
