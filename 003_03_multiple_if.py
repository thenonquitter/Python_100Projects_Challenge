# multiple if
# A,B,C 조건을 하나씩 검토
# if condition A :
#     do a
# if condition B :
#     do b
# if condition C :
#     do c

# nested if
# A,B,C 조건중에 해당하는 것 한가지만 선택
# if condition A :
#     do a
# elif condition B :
#     do b
# else condition C :
#     do c

bill = 0
size = input("What size do you want? (S, M or L): ")
pepperoni = input("Do you have pepperoni? (Y/N): ")
extra_cheese = input("Do you have extra cheese? (Y/N): ")

# 사이즈에 따른 가격 결정
if size == 'S' or size == 's' :
    bill += 15
elif size == 'M' or size == 'm' :
    bill += 20
else :
    bill += 25

# 페퍼로니 추가에 따른 가격 추가
if pepperoni == 'Y' or 'y' :
    if size == 'S' or size == 's' :
        bill += 2
    else :
        bill += 3

# 치즈 추가에 따른 가격 추가
if extra_cheese == 'Y' or 'y' :
    bill += 1

print(f"Your bill is ${bill}.")