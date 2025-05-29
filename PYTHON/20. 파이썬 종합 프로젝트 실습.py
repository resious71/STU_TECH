# 
#  [] 효과적인 알고리즘의 코드 구현 방법 연습
#    1) Egg Drop Competition 
#       - 내용물이 부서지지 않도록 하는 완중 장치를 만들었다. 완충 장치의 성능을 알기 위해 달걀을 하나 넣고 
#         100층 빌딩에서 낙하실험을 하여 달걀이 몇 층까지 깨지지 않고 견디는지 테스트 하고자 한다.  
#         몇 층까지 깨지지 않을까? 
# 
#    >> 달걀 낙하 실험 층수 맞추기 프로그램
#    >> 필요 지식 - 파이썬 기본 문법, 외부 모듈 활용, 랜덤 숫자, 조건문, 반복문
#    
#    >> 기본 로직 설계
#    >> 달걀 낙하 실험에서 달걀이 깨지는 층수 맞추기
#    >> 달걀이 깨지는 층수를 맞추면 "정답"입니다. 출력
#    >> 숫자를 못 맞추면 "틀렸습니다" 출력
# 
#    >> 랜덤 함수를 사용해서 1 ~ 100까지의 숫자를 생성
#    >> 무한 반복 실행을 방지하기 위해 시도 회수를 8회로 제한
# import random
# #   
# #    >> 프로그램 구현을 위한 변수 선언
# #    >> 숫자를 담을 변수와 시도횟수를 제한할 변수 선언
# #    >> 달걀이 깨지는 층수를 담을 변수
# chance = 8    # 시도 횟수 제한
# count = 0
# egg_number = random.randint(1,100)

# #    >> 달걀이 깨지는 층수를 맞추는 반복문 

# while count < chance:
#     count = count + 1
#     # 사용자가 입력한 숫자를 담을 변수
#     user_number = int(input("달걀이 깨지는 층수를 입력하세요: "))

#     if egg_number == user_number:
#         print("정답")
#         break
#     else:
#         print("틀렸습니다.")

# print("달걀 낙하 실험 프로그램 종료 !!!")

###########################################################################################
#
#   >> 달걀 낙하 실험 프로그램 2
#   >> 시도횟수를 5번으로 제한
#   
#   >> 구현 방식 = 기본 로직 구현 + 정답 힌트 제공
#
# import random
# chance = 5    # 시도 횟수 제한
# count = 0
# egg_number = random.randint(1,100)
# print("1~100 사이의 숫자를 맞춰보세요. - 시도 가능 횟수{}".format(chance))

# while count < chance:
#     count = count + 1
#     # 사용자가 입력한 숫자를 담을 변수
#     user_number = int(input("달걀이 깨지는 층수를 맞추어 보세요: "))

#     if egg_number == user_number:
#         break     # 정답을 맞추면 while 문 종료
#     elif egg_number > user_number:
#         print("{} 보다 큰 숫자입니다.".format(user_number))
#     elif egg_number < user_number:
#         print("{} 보다 작은 숫자입니다.".format(user_number))

# if egg_number == user_number:
#     print("정답: {} 이 맞습니다.".format(egg_number))
# else:
#     print("실패: {} 이었습니다.".format(egg_number))

# print("달걀 낙하 실험 프로그램 종료 !!!")
#
###########################################################################################
#
#   >> 달걀 낙하 실험 프로그램 3
#
#
# import random
# import os

# chance = 5    # 시도 횟수 제한
# count = 0
# egg_number = random.randint(1,100)

# # 실행 콘솔 창에서 기존 메시지 클리어하기
# os.system("cls")
# print("1~100 사이의 숫자를 맞춰보세요. - 시도 가능 횟수{}".format(chance))

# while count < chance:
#     count = count + 1
#     # 사용자가 입력한 숫자를 담을 변수
#     user_number = int(input("달걀이 깨지는 층수를 맞추어 보세요: "))

#     if egg_number == user_number:
#         break     # 정답을 맞추면 while 문 종료
#     elif egg_number > user_number:
#         print("{} 보다 큰 숫자입니다.".format(user_number))
#     elif egg_number < user_number:
#         print("{} 보다 작은 숫자입니다.".format(user_number))

# if egg_number == user_number:
#     print("정답: {} 이 맞습니다.".format(egg_number))
# else:
#     print("실패: {} 이었습니다.".format(egg_number))

# print("달걀 낙하 실험 프로그램 종료 !!!")
