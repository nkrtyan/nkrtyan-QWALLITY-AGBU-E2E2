my_list=[1,3,4,3,9,7,8,7,4]
u_list=[]
for num in my_list:
    if num not in u_list:
        u_list.append(num)
print(u_list)

# Nel, correct
# 2
my_list=[2,5,1,8,7]
del my_list[4]
del my_list[3]
del my_list[0]
print(my_list)
# Nel, correct

# 3
list1=[4,5,10,6,17]
list2=[9,8,7,12,11]
difference=[item for item in list1 if item not in list2] # TODO, i hope you understadn what is done here
print(difference)
# Nel, correct

# 4
my_tuple=(("apple",5),("name","Ani"),(4,"Hayk"))
my_dict=dict(my_tuple)
print(my_dict)
# Nel, correct

#5
my_tuple=(1,15,"kiwi",15)
my_list=list(my_tuple)
my_list.append(("kiwi",15))
print(tuple(my_list))
# Nel, correct

# 6
my_dict={"Armen":14,"Ani":9,"Hayk":6} # TODO< keep  format as i explained during lesson
my_dict["Arevik"]=1
print(my_dict)
# Nel, correct

# 7
my_dict={"Hasmik":15,"Gayane":20,"Karen":25,"Armen":30}
print(max(my_dict.values()))
print(min(my_dict.values()))
# Nel, correct

# 8 
set_1={15,6,8,11,9,2,33}
set_2={5,4,15,6,55,33,2}
print(set_1.union(set_2))
# Nel, correct

# 9
my_dict={
    "Siranush":"Avetisyan",
    "age":41,
    "address":"Droyi 4",
    "education":"YSU",
    "phone":["094999842","033659017"]
    }
import json
print(json.dumps(my_dict, indent=4))
print(my_dict["Siranush"])
print(my_dict["age"])
print(my_dict["address"])
print(my_dict["education"])
print(my_dict["phone"])
my_dict["email"]="siranushav@gmail.com"
import json # TODO, no need twice import the same lib, its enough once
print(json.dumps(my_dict,indent=4))
# Nel, correct


