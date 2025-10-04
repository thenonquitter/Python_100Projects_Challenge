import sys, random

scissor = '''
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
'''
rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
'''
paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
'''
choices = [scissor, rock, paper]

print("야 가위바위보로 맞짱뜨자")
user_choice = int(input("가위 낼 거면 0, 바위 낼 거면 1, 보 낼 거면 2를 쳐 : "))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    sys.exit("바보임? 0,1,2만 입력해야지 ㅋㅋㅋㅋ 너 패뱈ㅋㅋㅋㅋㅋ")

print(f"너의 선택은 : \n{choices[user_choice]}")
print(f"나의 선택은 : \n{choices[computer_choice]}")

if user_choice == computer_choice:
    print("흥 비겼네 찌찌뽕")
elif ((user_choice == 2 and computer_choice == 0)
      or (user_choice == 0 and computer_choice == 2)) :
    if user_choice == 2 :
        print("너 졌어 ㅋㅋㅋㅋ")
    else :
        print("ㅠㅠㅠ 너 이김")
else :
    if user_choice < computer_choice :
        print("응~ 너 졌어 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
    else :
        print("ㅠㅠㅠㅠㅠㅠ 니가 이김")
