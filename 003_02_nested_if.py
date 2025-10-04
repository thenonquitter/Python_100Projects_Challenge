height = int(input("Enter your height in centimeters: "))

if height >= 120 :
    print("You can ride a roller coaster!")
    age = int(input("Enter your age: "))
    if age >= 18 :
        print("pay $10")
    elif age >= 10 :
        print("pay $8")
    else :
        print("pay $5")
else :
    print("You can not ride a roller coaster!")

# nested if (중첩된 if)

# if / elif / else
# elif는 쓰고 싶은 만큼 블록을 추가할 수 있다.