# 파일(File)의 개념
#   - 컴퓨터를 실행할 때 가장 기본이 되는 저장 단위
#   - 보통 아이콘을 더블 클릭해서 실행하는 단위: 컴퓨터는 아이콘이 아닌 "실행파일"을 실행시키는 것 

# 파일 입출력의 개념
#   - 표준 입출력과 파일 입출력



#      표준 입력 장치    - 입력 관련                                       출력 관련                          표준출력장치
#                         (Input())                                      (print()) 

                  

#      파일             - 파일 입력 관련                                   파일 출력 관련                      출력
#                         (read(), readline(), readlines())               (write(), wrtielines())

# 파일(File) 입출력의 기본 과정

#   1단계) 파일 열기 :  읽기용: 변수명 = open("파일명", "r")
#                      쓰기용: 변수명 = open("파일명", "w")
#   2단계) 파일처리
#   3단계) 파일닫기
#          1단계에서 open() 함수로 연 변수명을 close() 함수로 종료: 변수명.close()

#    + 모드(Mode): open() 함수의 마지막 매개변수로 파일을 열 때 어떤 용도인지 결정

#         종류          |  설명
#     -------------------------------------------------------------------------     
#        생략           |   r과 동일 
#        r              |   읽기 모드, 기본값
#        w              |   쓰기 모드, 기존에 파일이 있어면 덮어씀
#        r+             |   읽기/쓰기 겸용 모드
#        a              |   쓰기 모드, 기존 파일이 있으면 이어서 쓴다. append
#        t              |   텍스트 모드, 텍스트 파일을 처리한다. 기본값
#        b              |   이진 모드, 이진 파이을 처리한다. 

#     ** with ~ as문   
#          -- 프로그램을 만들다 보면 close() 함수를 호추랗지 않고 프로그램을 종료해서 종종 문제가 발생한다.
#             아예 close() 함수를 사용하지 않으려면 다음과 같이 with ~ as 문으로 파일을 연다.

#              with open("C:/Temp/data1.txt","r") as inFp:
#              inList = inFp.readlines()
#              print(inList) 

#    파일 다루기
#      + 파일 입출력은 기본적으로 텍스트 파일을 의미
#      + encoding : 파일을 읽을 때 사용하는 문자 해석 방법
#         - utf-8: 윈도우를 제외하고 전세계적으로 일반적으로 사요오디는 방법
#         - cp949: 윈도우에서 사용하는 방법
#      + 파일 읽기 - 텍스트 데이터 읽어오기

#        f = open("c:/python/dream.txt","r")
#        contents = f.read()
#        f.close()
#        print(contents)

#####################################################################################################
# 파일 입출력 연습 - 파일 읽기 연습
#      -- dream.txt 파일을 읽기 모드로 열어서 파일 객체로 얻어 온다.  

#####

# f = open("C:\source\dream.txt","r")
# file_content = f.read()
# f.close()

# print(file_content)
# print(type(file_content))    # <class 'str'>

##### with ~ as 구문을 사용해서 파일을 읽어 들이는 방법 

# with open("C:\source\dream.txt","r") as file_ref:
#     file_content = file_ref.read()
# print(file_content)
# print(len(file_content))

#####  readlines(): 파일의 내용을 한 줄씩 읽어서 리스트에 담아서 리턴하는 방법

# with open("C:\source\dream.txt","r") as file_ref:
#     file_content = file_ref.readlines()
#     # 객체 타입 = string 문자열: 문자 시퀀스 - file_content[0]
#     # 문자 슬라이싱 : 문자열[시작인덱스:끝인덱스]

# print(file_content[:10])
# print(len(file_content))

#####  파일쓰기 (기존 파일을 덮어씀)

# file_handle = open("C:\source\count.txt","w", encoding="utf-8")
# for i in range(1,11):
#     data = "{}번째 줄입니다.\n".format(i)
#     file_handle.write(data)
# file_handle.close()

##### append (기존 파일에 추가)

# file_handle = open("C:\source\count.txt","a", encoding="utf-8")
# for i in range(11,21):
#     data = "{}번째 줄입니다.\n".format(i)
#     file_handle.write(data)
# file_handle.close()

#####  with ~ as 

# with open("C:\source\count2.txt","w", encoding="utf-8") as file_handle: 
# for i in range(1,11):
#     data = "{}번째 줄입니다.\n".format(i)
#     file_handle.write(data)

#####################################################################################################
### 파일 글자 통계 정보 출력

# with open("C:\source\dream.txt","r", encoding="utf-8") as file_handle: 
#     file_content = file_handle.read()
#     word_list = file_content.split(" ")
#     line_list = file_content.split("\n")

# print("총 글자 수: ", len(flie_content))
# print("총 단어 수: ", len(word_list))
# print("총 줄 수: ", len(line_list))

#####################################################################################################
### CSV 파일 읽어서 출력하기

# import csv

# with open("C:\source\fruit.csv","r", encoding="utf-8") as file_handle:
#     csvRead = csv.reader(file_handle)
#     fruit = []
#     for i in csvRead:
#         fruit.append(i)
#         print(i)

 ### CSV 파일로 저장하기 - csv 파일을 생성해서 프로그램에서 처리한 최종 데이터를 영구저장하기

# import csv

# with open("C:\source\fruit2.csv","w", encoding="utf-8") as file_handle:                 # 개행
#     writer = csv.writer(file_handle, delimiter=",")
#     writer.writerow(["사과","배","감"])
#     writer.writerow(["귤","수박","메론"])
#     writer.writerow(["포도","참외","복숭아"])
#     writer.writerow(["레몬","두리안","망고"])


# with open("C:\source\fruit2.csv","w", encoding="utf-8", newline="") as file_handle:     # 개행없음
#     writer = csv.writer(file_handle, delimiter=",")
#     writer.writerow(["사과","배","감"])
#     writer.writerow(["귤","수박","메론"])
#     writer.writerow(["포도","참외","복숭아"])
#     writer.writerow(["레몬","두리안","망고"])
