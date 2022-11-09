print(5)
print(-10)
#abs ( 값 ) -> 절대값 구하기 
# pow( ) 차수식 4^2 max 최대값 구하기 ,min 최소값, round 반올림 

from math import *
print(floor(2.77   )) 
print(ceil(3.15))
print(sqrt(16)) 

# 랜덤 함수
from random import *
print(random()) # 0.0 ~ 1.0 
print(random()*10)  
print(int(random()*10))  

print(randrange(1,46)) # 1~ 46 미만의 임의의 값

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 


#------------------------------------------------------------------------------
#Q1 
x = randint(4,28)
print("오프라인 스터디 날짜는 " , x , "일 입니다. ")

sent = 'dddd'
print(sent)

sent2 = "aaaaa"
print(sent2)

sent3 = """
dfdfd
dfasdf,f
sdfasgs/fdsf.
"""

print(sent3)


#------------------------------------------------------------------------------
# 문자열 자르기  (문자열 인덱스는 0부터 시작 )
min = "123456-1234567"
print("성별"  + min[7]) # 7번째 인덱스의 값 출력 
print("연도" + min[0:2]) # 0 ~ 1 번쨰 값 
print("월 " + min[2:4]) # 2 ~ 3 번째 값
print("일 " + min[4:6])
print("생년월일 " + min[:6]) # 0 ~ 5번째 까지의 값 
print("뒷 자리 " + min[7:]) # 7 ~ 마지막 까지의 값 
print("뒷 자리 (뒤 부터 출력  ) " + min[-7:]) # -7번째 부터 값 
print("뒷 자리 (뒤 부터 출력  ) " + min[-11:-7]) # -7번째 부터 값 



#------------------------------------------------------------------------------
#대소문자 변환
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python" , "Java"))


index = python.index("n") #  5 
#index("찾는 문자") 찾는 문자의 인덱스 번호를 반환 
print(index)

index = python.index("n" , index + 1)  # 15 
# index("찾는 문자" , index + 1 ) 찾는 문자중에 첫번째 문자는 패스 
# 두번째로 나오는 문자의 인덱스 번호를 반환 
print(index)
print(python.find("n"))  # index랑 같은 함수 오류 시 종료유무만 다름 
print(python.find("Java")) # 즉시 종료 하지않음 // -1 리턴
# print(python.index("Java")) 에러 : 즉시 종료 
print(python.count("n"))


#------------------------------------------------------------------------------
#문자열 포멧
print("나는 %d 살 입니다.  " %20)
print("나는 %s을 좋아해요   " %"파이썬")
print ("Apple 은 %c 로 시작해요." %"A")

print("나는 %s 살 입니다.  " %20)
print("%s %s " %("ㅇㅇ" ,"ㄹㄹ"))

print("나는 {}" .format(20))
print("{}{} " .format("ㅇㅇ","ㄹㄹ"))
print("{0}{1} " .format("ㅇㅇ","ㄹㄹ")) # 순서대로 format (0 , 1)
print("{1}{0} " .format("ㅇㅇ","ㄹㄹ")) # print 의 {} 숫자는 마음대로 설정 가능 

print("{age} ff {color} dd" .format( age = 20 , color="빨간색")) # 변수를 직접 설정 가능 
print("{color} ff {age} dd" .format( age = 20 , color="빨간색"))


age = 20 
color ="빨간색"
print(f"{color} ff {age} dd") # format을 안쓰고 이미 선언된 변수를 print할때는 f를 붙여서 사용 

#------------------------------------------------------------------------------
#Q2 자동으로 비밀번호를 만들어주는 프로그램 
site = "http://naver.com"
my_str = site.replace("http://" , "") # replace ("찾으려는 문자열" , "바꿀 문자열") -> 뒤에 "" 공백을 입력함으로써 앞의 http://는 지워진다. 
my_str = my_str[:my_str.index(".")] # 문자열 자르기 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +"!"
print("{0} 의 비빌먼호는 {1} 입니다. " .format(site , password))


#------------------------------------------------------------------------------
# 리스트 [] 
# subway1 = 20; 
# subway2 = 30; 
# subway3 = 10; 

subway = [10,20,30]
print(subway)

subway = ["조세호","유재석","박명수"]
print(subway)
print(subway.index("조세호"))

subway.append("하하") # 추가 
print(subway)

subway.insert(1, "정형돈")
print(subway)

# subway.pop()
# subway.pop()
# subway.pop()
# print(subway)
print(subway.pop())

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [ 4 ,2, 3,1 ,5,6,2,1,5]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
# 모두 지우기
# num_list.clear
print(num_list)

# 다양한 자료와 함꼐 사용가능 

# 리스트 확장 리스트 + 리스트 
num_list.extend(subway)
print(num_list)



#------------------------------------------------------------------------------
#데이터 사전 { key : value , .....}
cabinet = { 3:"유재석" , 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 값이 없을때 프로그램 종료
print(cabinet.get(5)) # 값이 없어도 none을 출력하고 종료하지 않음

print(cabinet.get(5 , "사용 가능")) # 값이 없으면 뒤의 문자열 출력

print(3 in cabinet) # 사전에 키값이 있는 지 확인 있으면 True 없으면 False

cabinet = { "A-3":"유재석" , "B-100":"김태호"}

cabinet["C-20"] = "조세호" # 키 값으로 C-20 이 있으면 뒤의 문자열로 업데이트 
# 키값이 없다면 데이터 추가 
print(cabinet)
#키 삭제 
del cabinet["A-3"]
print(cabinet)
# 키값만 출력 , value 만 출력 , 전부 출력 
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()



#------------------------------------------------------------------------------
# 튜플 (내용 변경 X 속도가 빠름 )
menu = ( "돈까스 " , " 치즈까스 ")
print(menu[0])
print(menu[1])

# name ="김종국"
# age = 20
# hobby = "코딩"
# 튜플로 활용 가능 
(name , age , hobby) = ( "김종국" , 20 , "코딩")

# 집합 (Set) 중복 X 순서가 없음 
my_set = {1,2,3,4,5,5,5,5}
print(my_set)

java = {"유재석" , "김태호" , "양세형"}
python = set(["유재석" , "박명수"])

#교집합 
print(java & python)
print(java.intersection(python))
#합집합
print(java|python)
print(java.union(python))
#차집합
print(java - python)
print(java.difference(python))

#데이터 추가
python.add("김태호")
print(python)

#데이터 삭제
java.remove("김태호")

#------------------------------------------------------------------------------
# 자료구조의 변경
menu = { "커피" , "우유" ,"주스" }  # set 타입 
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu,type(menu))

#------------------------------------------------------------------------------
#Quiz
from random import *
# lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,22,22,22,22,22,22,22,22]
# 함수를 통해 간단하게 가능 
users = range(1, 21 ) # 1 ~ 20 까지 숫자를 생성 range는 리스트가 아님 리스트 함수 사용 불가 
users = list(users)
print(users)
list = set(str(users)) # 중복 체크
shuffle(users)
print(users)
# 중복 당첨자가 나올 가능성이 있음 
# print("치킨 : " , sample(users,1))
# print("커피 : ", sample(users,3))
print("-- 당첨자 발표 -- ")
winner = sample(users, 4)
print("치킨 : {0}" .format(winner[0]))
print("커피 : {0}" .format(winner[1:]))


#------------------------------------------------------------------------------
#if 
weather = input("오늘 날씨는 어때요 ?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크 챙기세요")
else:
    print("맑아요~")

temp = int(input("기온 > ")) # input은 항상 String타입으로 데이터를 받음 정수형변환이 필요
if 30 <= temp :
    print ("너무 더워요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨 ")
elif 0 <= temp < 10 : 
    print("외투를 챙기세요 ")
else:
    print("너무 추워요")

#------------------------------------------------------------------------------
# 반복문 
print("대기 번호  1")
print("대기 번호  2")
print("대기 번호  3")
print("대기 번호  4")

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}" .format(waiting_no))

for waiting_no in range(1,6): # 1 ~ 5
    print("대기번호 : {0}" .format(waiting_no))

#------------------------------------------------------------------------------
# #while
customer = "토르"
index = 5
while index >= 1:
    print("{0} , 커피가 준비 되었습니다. {1} 번 남았어요 ".format(customer , index))
    index -=1
    if index == 0:
        print ("커피를 버렸습니다.")

#------------------------------------------------------------------------------
# 무한 반복 
customer = "아이언맨"
index = 0
while True:
    print("{0} , 커피가 준비 되었습니다. {1} 번 ".format(customer , index))
    index +=1

customer = "토르"
person = "Unknown"
while person != customer:
    print ("{0} , 커피 준비 . " .format(customer))
    person = input("이름이 >?")


#------------------------------------------------------------------------------
# continue break 
absent = [2,5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("수업 끝 {0} ".format(student))
        break
    print("{0} , 책을 읽어봐" .format(student))

#------------------------------------------------------------------------------
# 한줄 for 문
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

student = [ "aaaaaaa" , "bbbb" , "ccccccccc"]
student = [len(i) for i in student]
print(student)

student = [ "aaaaaaa" , "bbbb" , "ccccccccc"]
student = [i.upper() for i in student]
print(student)

from random import *
cnt = 0 
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[O] {0}번쨰 손님 ( 소요시간 : {1} ) " .format(i , time))
        cnt += 1
    else:
        print("[ ] {0}번쨰 손님 ( 소요시간 : {1} )" .format(i , time))

print( " 총 탑승 승객 : {0} " .format(cnt))