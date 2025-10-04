# logical operator
## A and B
## A or B
## not A

height = int(input("Enter your height in centimeters: "))

if height >= 120 :
    print("You can ride a roller coaster!")
    age = int(input("Enter your age: "))
    if age >= 18 :
        if 45 <= age <= 55:# age >= 45 and age <= 55
            print("You don't need to pay")
        else :
            print("pay $10")
    elif age >= 10 :
        print("pay $8")
    else :
        print("pay $5")
else :
    print("You can not ride a roller coaster!")