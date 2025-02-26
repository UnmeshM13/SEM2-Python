# Q1
a = int(input("Enter a number:"))
if a%2==0:
        print("Number is even")
else:
    print("Number is odd")
print("\n------------------------------------------------------------------\n")

# Q2
b = int(input("Enter a number:"))

if b>0:
    print("Number is positive")
elif b<0:
    print("Number is negative")
if b%2==0:
        print("Number is even")
else:
        print("Number is odd")


print("\n------------------------------------------------------------------\n")

# Q3
marks=int(input("Enter your marks:"))
if marks>89:
    print("grade A")
elif marks>79:
    print("Grade B")
elif marks>69:
    print("Grade C")
else:
    print("Fail")
print("\n------------------------------------------------------------------\n")

# Q4
year = int(input("Enter the year"))
if (year/4==0 and year%100 != 0) or year%400==0:
    print("Leap year")
else:
    print("Not Leap year")
print("\n------------------------------------------------------------------\n")

# Q5
age=int(input("Enter your age:"))
if age>=18:
    print("you can vote")
    if age<60:
        print('you are not eligible for senior citizen')
    else:
        print('you are eligible for senior citizen')
else:
    print("You are not eligible for vote")
    
print("\n------------------------------------------------------------------\n")


#post experiment exerxise
# Q1
a=int(input("Enter a number:"))
if a%3==0 and a%5==0:
        print("Number is multiple of both 3 and 5 ")
else:
        print("Number is  Not a multiple of both 3 and 5 ")
        
print("\n------------------------------------------------------------------\n")

# Q2
temp=int(input("Enter temperature in celsius:"))
if temp<=20:
        print("Cold")
elif temp>20 and temp<30:
        print("Moderate")
else:
        print("Hot")
print("\n------------------------------------------------------------------\n")

# Q3 
char=input("Enter a Letter: ")
tup = ('a','A','e','E','i','I','o','O','u','U')
if char in tup:
    print("Entered Letter is a Vowel")
else:
        print("Entered Letter is Consonant")
print("\n------------------------------------------------------------------\n")


"""
different way for Q1 & Q5
==>    Normal way 
# Q1

a=int(input("Enter a number:"))
if a%(3*5) == 0:
    print("Number is multiple of both 3 and 5)
else:
    print("Number is Not a multiple of both 3 and 5")

# Q5
if 'a' == char or 'e' == char or 'i' == char or 'o' == char or 'u' == char :
        print("Entered Letter is a Vowel")
elif 'A'==char or 'E'==char or 'I'==char or 'O'==char or 'U'==char :
        print("Entered Letter is a Vowel")
else:
        print("Entered Letter is Consonant")

"""
