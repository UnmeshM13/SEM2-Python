#Question-1

data1 = ["hello"," user"," no."," 1026"]
data2 = (1026,)
data3 = "Hello world"
data4 = {'Name':"Unmesh",'Roll no.':1026}
data5={"hello","33",33}
print(type(data1))
print(type(data2))
print(type(data3))
print(type(data4))
print(type(data5))

print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")

#Question-2


str1="Python Program"
str2="string Operations"
print("Length of the str1 1 is ",len(str1)," and that of str2 is ",len(str2))
print("string concatenation",str1+str2)
print("string repetation",str2*3)
print("First element of string 2 is:",str2[0])
print("\nPerforming String slicing:\n")
print(str1[2:9])
print(str1[2:9:2])
print(str2[6:])
print(str2[:9:1])
print(str2[::-1])
print("Str1 in lower case is",str2.lower(),"and str2 in lower case is",str2.lower())
print("Str1 in upper case is",str2.upper(),"and str2 in upper case is",str2.upper())
print("str1 starts with Python:",str1.startswith("Python"))
print("str2 ends with Python:",str1.endswith("operations"))
print(str1.isalpha())
print(str1.isalnum())
print(str2.isspace())
print(str2.capitalize())
print("\nSplit operations:\n")
print(str1.split())
print(str2.split(" "))
print(str1.find('Pro'))
print(str1.index("Pro"))
print(str1.find('o',4,14))
print(str2.count('i'))
print("---------------------------------------------------------------------------------------------------------------------")
#list operations

list1=[911,'hello world','INFT']
list2=[55,'SFIT','a']
print("2nd element of list is   : ",list1[1])
print("list[0] before assignment:",list1)
list1[0]="B"
print("list[0] after assignment :",list1)
print("Slicing                  :",list1[1:2])
a=list1+list1
print(a)
print("Assigning empty list:")
my_list=list()
print("Empty list:",my_list)
print("squeez")
li=[1,2,2,3,4,4]
li=list(set(li))
print(li)
a="Aryan"
print("Deleting List:",list1.remove("INFT"))
print(list1)
list1.clear()
print(list1)
print("Use of membership operators in list:")
print(55 in list2)
print(34 in  list2)
a="TOP-G"
b=list(a)
print(b)
print("Sorting:",b.sort())
print(b)
print("length of list2 is:",len(list2))
list2.append("HELLO")
print(list2)
print("Index of SFIT is:",list2.index("SFIT"))
print("list befor pop:",list2)
list2.pop()
print("List after pop",list2)
list2.extend("IT")
print(list2)
print("---------------------------------------------------------------------------------------------------------------------")
#tuple operations
tup=("pyp",2,45,"game")
print("first element of tup:",tup[0])
print("Number of game elements are:",tup.count('game'))
print("First occurence of 2 is at index:",tup.index(2))
a="Unmesh"
b=tuple(a)
print(b)

print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")

#Question-3
 
print("Airthmetic Operator")

var1 = 2
var2 = 5

print("add",var1+var2)
print("sub",var1-var2)
print("mul",var1*var2)
print("div",var1/var2)
print("mod",var1%var2)
print("floor div",var1//var2)
print(var1,"raised to",var2,var1**var2)


print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")

#Question-4

print("Assignment Operation")
a=b=2
print("A is",a,"B is",b)
a+=3
b-=3
print("A+=3 is",a,"B-=3 is",b)
a/=3
b*=3
print("A/=3 is",a,"B*=3 is",b)
a%=3
b//=3
print("A%=3 is",a,"B//=3 is",b)
a**=3
print("A**=3 is",a)

print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")

#Question-5

print("Logical Operation")
c=8
d=5
print((c<10)and(d>0))
print((c<10)or(d>0))
print(not(c<10 and d>0))

print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")

#Question-6

print("Bitwise Operation")
a=10
b=2
c=0
print("A=",a,"B=",b,"C",c)
print("a&c ",a&c)
print("a|b",a|b)
print("a^b",a^b)
print("~c",~c)
print("a<<2",a<<2)
print("a>>2",a>>2)
print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")

#Question-7

print("Membership Operation")
a="hello this is a wonder full place"
print("hello"in a)
print("."not in a)
print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")

#Question-8

print("Identity Operation")
a="hello this is a wonder full place"
b="hello that is a wonder full place"
print(b is a)
print(b is not a)
 
print("\n")
print("---------------------------------------------------------------------------------------------------------------------")
print("\n")
