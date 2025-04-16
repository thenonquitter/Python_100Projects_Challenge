#fuctions need certain data types
#len(12345) #len func can't take a int type.


#How to type-checking : type function
print(type("12345"))
print(type(12345))
print(type(123.45))
print(type(True))


#Type Casting
print(int("123")+int("345")) #str -> int

int()
float()
str()
bool()

# print("Number of letters in you name : " + str(len(input("Enter your name : "))))


#Mathmatical Operations
print(1+1)
print(1-2)
print(2*3)
print(4/2) #output float
print(4//2) #output int : after operate '/', change the type to int.
print(5//2) #caution : 소수점 아래로 버림
print(2**3)

#Number manipulation
print(int(3/2)) #소수점 아래 버림
print(round(3/2)) #반올림
print(round(10/3, 7)) #두번째 arg까지 남기고 반올림

#F-strings : 문자열과 다양한 datatype의 혼합을 쉽게 만듦.
score = 0 #int
height = 1.8 #float
is_winning = True #boolean
print(f"Your score is {score}, height is {height}, and the fact that you're winning is {is_winning}.")
