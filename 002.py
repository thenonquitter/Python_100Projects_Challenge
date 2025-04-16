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

print("Number of letters in you name : " + str(len(input("Enter your name : "))))