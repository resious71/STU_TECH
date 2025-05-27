#
# > 예외 처리 (Exception Handling)
#     + 오류가 발생할 때 파이썬이 처리하지 않고 프로그래머가 작성한 코드를 실행하도록 하는 방식
#     + 파일 처리, 문자열 처리, 리스트 처리 등에서 활용해야 하는 상황이 많이 발생함
#     + 필요 상황) 파일을 삭제 --> 파일이 존재하지 않아서 오류가 발생
#         - try, exception 문을 사용해서 파이썬의 오류 대신 사용자가 오류 메시지를 작성해서 프로그램이 종류되지 않고  
#            정상적인 흐름을 이어가게 하는 역할을 담당함  
#     + except 문 뒤에는 아무것도 명시하지 않으면 모든 종류의 오류 처리가 가능해짐
#     + 필요하다면 오류의 종류에 따라서 다른 오류 처리도 가능함
# 
#      try:
#          실행할 문장등
#      except 예외_종류 1:
#          오류일 때 실행할 문장들
#      except 예외_종류 1:
#          오류일 때 실행할 문장들
# 
#      + ERRORS
#         - ImportError, IndexError, KeyError, NameError, RuntimeError, SyntaxError, ZeroDivisionError, IOError 등
# 
 
# 예외 발생시키기
# import os
# os.remove("c:/fruit.csv")   # 예외 발생 (파일이 없음) --> FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다: 'c:/fruit.csv'

# 예외 처리 기본 구조

# import os

# try:
#     os.remove("c:/fruit.csv")
# except:
#     print("파일이 존재하지 않습니다. 삭제할 파일 이름을 확인하세요")

# print("추가 코드 실행 확인")
# print("====== End of Code ======")

# 예러 종류에 따른 예외 처리
# 1) except ValueError
# 2) except ZeroDisisionError
# 3) except KeyboardInterrupt

# num1 = input("숫자1 입력: ")
# num2 = input("숫자2 입력: ")

# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     while True:
#         res = num1/num2
#         print(res)
# # except:
# #     print("에러 발생")

# except ValueError:
#     print("문자는 숫자로 변환할 수 없습니다.")
# except ZeroDivisionError:
#     print("0으로는 나눌 수 없습니다.")
# except KeyboardInterrupt:
#     print("사용자가 강제 종료했습니다.")   

#  try, except, else, finally 구문 연습
#   - try 문에서 오류가 발생하면 except 문으로 이용하여 프로그램이 실행됨
#   - 오류가 발생하지 않는다면 else 문으로 이동하여 프로그램이 실행됨
#   - finally 문은 오류 발생 여부와 상관없이 무조건 실행됨

# num1 = input("숫자1 입력: ")
# num2 = input("숫자2 입력: ")

# try:
#     num1 = int(num1)
#     num2 = int(num2)
# except:
#     print("에러 발생")
# else:
#     print(num1, "/", num2, "=", num1/num2)
# finally:
#     print("프로그램을 종료합니다.")

# try ~ finally 구문 연습 (종합)
#   - 구문 : try ~ except ~ else ~ finally
#    1) try 문에서 오류가 발생하면 excpet 문으로 이동하여 프로그램이 실행됨
#    2) 오류가 발생하지 않으면 else 문으로 이동하여 프로그램이 실행됨
#    3) finally 문은 예외 발생 여부와 상관없이 무조건 실행됨

# num1 = input("숫자1 입력: ")
# num2 = input("숫자2 입력: ")

# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1, "/", num2, "=", num1/num2)
# except ValueError:
#     print("문자는 숫자로 변환할 수 없습니다. 숫자를 입력하세요")
# except ZeroDivisionError:
#     print("0으로는 나눌 수 없습니다.")
# except KeyboardInterrupt:
#     print("사용자가 ctrl + v를 눌렀습니다.")    
# except:
#     print("프로그램 실행 중 어떤 임의의 오류가 발생했습니다.")
# else:
#     print("프로그램 개발에서 에러가 발생하지 않은 경우에 대한 로직 추가 가능")
# finally:
#     print("프로그램을 종료합니다.")
#     print("이 영역의 코드는 반드시 실행됩니다.")


