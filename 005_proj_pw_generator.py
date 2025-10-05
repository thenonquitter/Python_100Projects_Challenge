import random

# 알파벳 (대문자 + 소문자)
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# 숫자 (0~9)
numbers = ['0','1','2','3','4','5','6','7','8','9']

# 특수기호
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("암호 생성기")
n_let = int(input("글자 몇개 들어가길 원해?"))
n_num = int(input("숫자 몇개 들어가길 원해?"))
n_sym = int(input("특수문자 몇개 들어가길 원해?"))

# # 쉬운 버전
# pw = []
#
# for i in range(n_let):
#     pw += random.choice(letters)
# for i in range(n_num):
#     pw += random.choice(numbers)
# for i in range(n_sym):
#     pw += random.choice(symbols)
# print("생성된 암호 : ", end="")
# for i in pw :
#     print(i, end="")

# 어려운 버전
pw2 = []

for i in range(n_let):
    pw2 += random.choice(letters)
for i in range(n_num):
    pw2 += random.choice(numbers)
for i in range(n_sym):
    pw2 += random.choice(symbols)

print(pw2)
# random.shuffle(pw2) #리스트의 배열을 섞어버림
# print(pw2)
# print("생성된 암호 : ", end="")
# for i in pw2 :
#     print(i, end="")

mixed_pw = random.sample(pw2, (n_let + n_num + n_sym)) #리스트의 배열을 비복원 추출하여 섞어서 return함
print("생성된 암호 : ", end="")
for i in mixed_pw:
    print(i, end="")
print("\n\noriginal pw list : ", pw2)
print("mixed pw list: ", mixed_pw)




# # 어려운 버전
# # 난수 생성 -> 0,1,2를 경우의 수로
# # 각 경우의 수마다 -를 시키고 임의의 문자 random 출력
# # 0이 되면 skip
# # 실패함. 예외처리에 문제.
#
# hard_pw = []
#
# for i in range(n_let+n_num+n_sym):
#     select_type = random.randint(1, 3)
#
#     if select_type == 1:
#         if n_let > 0 :
#             n_let -= 1
#             hard_pw += random.choice(letters)
#         else :
#             select_type = random.randint(2,3)
#             if select_type == 2 :
#                 n_num -= 1
#                 hard_pw += random.choice(numbers)
#             else :
#                 n_sym -= 1
#                 hard_pw += random.choice(symbols)
#
#     elif select_type == 2:
#         if n_num > 0 :
#             n_num -= 1
#             hard_pw += random.choice(numbers)
#         else :
#             select_type = random.choice([1,3])
#             if select_type == 1 :
#                 n_let -= 1
#                 hard_pw += random.choice(letters)
#             else :
#                 n_sym -= 1
#                 hard_pw += random.choice(symbols)
#
#     elif select_type == 3:
#         if n_sym > 0 :
#             n_sym -= 1
#             hard_pw += random.choice(symbols)
#         else :
#             select_type = random.randint(1,2)
#             if select_type == 1 :
#                 n_let -= 1
#                 hard_pw += random.choice(letters)
#             else :
#                 n_num -= 1
#                 hard_pw += random.choice(numbers)
#
# print("생성된 암호 : ", end="")
# for i in hard_pw:
#     print(i, end="")