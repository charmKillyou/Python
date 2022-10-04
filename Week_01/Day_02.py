'''
str1 = "저의 이름은 "
str2 = "'홍길동' 입니다."
str3 = str1 + str2
print(str3)

str4 = "홍길동\n"
print(str4 * 3)
print("--------" * 5)

a = "Hong Gil Dong"
b = len(a)
print(b)
print(len(a))
print(len("안녕하세요???")

num = 0
sum = 0
while num <= 1000:
    num += 1
    if num % 3 == 0:
        sum += num
        print("결과 : %d" %sum)

a = "나는 홍길동이다"
print(a[3]+a[4]+a[5])
print(a[3:6])
print("감사합니다"[1:4])

a = "Love of my life"
b = a[8:10]
print("b :", b)
print(a[8:-2])

c = "I want to break free"
print(c[:6])
print(c[10:])
print(c[-10:])
print(c[:])

a = "20220930Sunny"
year = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[-5:]
print(year, month, day, weather)

form = "내 이름은 %s이고요, 키는 %d 입니다"
print(form %("독고일성", 170))

print("%s" %"hi")
print("%10s" %"hi")
print("%f" %3.14)
print("%.2f" %3.14)
print("%.2f" %3.167)
print("%10.2f" %3.14)

print("은행의 이자율은 %f%% 입니다" %0.5)
print("은행의 이자율은 %.1f%% 입니다" %0.5)
print("은행의 이자율은 %.2f%% 입니다" %0.5)

print("은행의 이자율은 {}% 입니다".format(0.5))
print("은행의 이자율은 {:.2f}% 입니다".format(0.5))
print("은행의 이자율은 {:.4f}% 입니다".format(0.5))

a = "aaabbcccccdd"
print(a.count("c"))

b = "Python is the best best hot language"
print(b.find("b"))
print(b.find("z"))  # 없는 문자 -1 반환
print(b.index("b"))
print(b.index("z")) #  에러 발생

d = "@".join("abcd")
print(d)

e = "I love Python"
print(e.replace("Python", "Java"))

lang = "I love Java"
print(lang.replace("Java", "Python"))

f = "너와 나의 연결고리"
fList = f.split(" ")
print(fList)

a = "안^녕^하^세^요"
aList = a.split("^")
print(aList)

b = "안 녕 하 세 요"
bList = b.split()
print(bList) # 안, 녕, 하, 세, 요

num = "881122-1068234"
year = "19" + num[:2]
month = num[2:4]
day = num[4:6]
print("홍길동씨는 %s년 %s월 %s일에 태어났습니다" %(year, month, day))
print("홍길동씨는 {}년 {}월 {}일에 태어났습니다".format(year, month, day))

a = "a:b:c:d"
print(a)
b = a.replace(":", "^")
print(b)

c = type(3.14)
print(c)

name = "임충"
title = "80만 금군교관"
print(name + "님은" + title + "이십니다.")
print("%s님은 %s이십니다." %(name, title))

score = 89
#print("성적은 " + score) # 오류
print("성적은 " + str(score))
print(score + int("10"))

kor = 85
eng = 95
math = 89
sum = kor + eng + math
avg = sum / 3
print("합계 : %d, 평균 : %.2f" %(sum, avg))
print("합계 : {}, 평균 : {:.2f}".format(sum, avg))

str = "KoreaIT"
print("/".join("KoreaIT"))
print("/".join(str))
print("=" * 20)
print(str.upper())
print(str.lower())

stri = "   pyt   hon   "
print(stri.lstrip())
print(stri.rstrip())
print(stri.strip())
print(len(stri.lstrip()))

a = "나 는 늘 행 복 합 니 다 ."
print(a.replace(" ", ""))

person = input("이름을 입력하세요 : ")
print(f"{person}님 반가워요.")
print(person + "님 반가워요.")
print("{}님 반가워요.".format(person))

a = input()
b = input()
print(int(a) + int(b))
print(a + b) #인풋 입력값 = 문자열

print("enter your name and age: ", end="")
name, age = input().split(" ")
print(f"{name}님은 {age}살 입니다.")
print("{}님은 {}살 입니다.".format(name, age))

year = "2022"
month = "9"
day = "30"
print(year, month, day)
print(year, month, day, sep="/")
print(year, month, day, sep="-")
print(year, month, day, sep="")

hp1 = "010"
hp2 = "1234"
hp3 = "5678"
print(hp1, hp2, hp3, sep="-")

print("{0}{1}".format("홍길동", "길동"))
print("{1}{0}".format("홍길동", "길동"))
print("{0:10s}님은 {1:03d}살 입니다.".format("홍길동", 20))
print("{1:7.2f} {0}".format("홍길동", 178.4))
'''
'''
# User Infomation
nameStr = "홍길동"
ageNum = 18
phoneStr = "010-2982-5869"

korScoreNum = 30
engScoreNum = 45
mathScoreNum = 92
socScoreNum = 52
sciScoreNum = 71

sumNum = korScoreNum + engScoreNum + mathScoreNum + socScoreNum + sciScoreNum
avgNum = sumNum / 5
###################################

# % Formatter
print("""안녕하세요. 제 이름은 %s입니다. 나이는 %d살이고, 전화번호는 %s입니다.
제 성적을 말씀드리겠습니다. 
국어는 %d점, 영어 %d점, 수학 %d점입니다.
사회는 %d점, 과학은 %d점입니다.
총합 %d점이라 평균 %.1f점입니다.""" %(nameStr, ageNum, phoneStr, korScoreNum, engScoreNum, mathScoreNum, socScoreNum, sciScoreNum, sumNum, avgNum))

# str.format() Formatter
print("""안녕하세요. 제 이름은 {name}입니다. 나이는 {age}살이고, 전화번호는 {phone}입니다.
제 성적을 말씀드리겠습니다. 
국어는 {kor}점, 영어 {eng}점, 수학 {math}점입니다.
사회는 {soc}점, 과학은 {sci}점입니다.
총합 {sum}점이라 평균 {avg:.1f}점입니다.""".format(name = nameStr, age = ageNum, phone = phoneStr, kor = korScoreNum, eng = engScoreNum, math = mathScoreNum, soc = socScoreNum, sci = sciScoreNum, sum = sumNum, avg = avgNum))

# f-string Formatter
print(f"""안녕하세요. 제 이름은 {nameStr}입니다. 나이는 {ageNum}살이고, 전화번호는 {phoneStr}입니다.
제 성적을 말씀드리겠습니다. 
국어는 {korScoreNum}점, 영어 {engScoreNum}점, 수학 {mathScoreNum}점입니다.
사회는 {socScoreNum}점, 과학은 {sciScoreNum}점입니다.
총합 {sumNum}점이라 평균 {avgNum:.1f}점입니다.""")

# % Formatter -> str.format() Formatter -> f-string Formatter 순으로 발전
# 마지막에 f-string Formatter가 제일 좋다는 의미는 아님
# 가독성 측면에서 f-string Formatter가 가장 우수
# 차후 회사에 취직했을 경우에 다른 Formatter를 사용하여 개발하는 직원이 있을 수 있어 해석하는 방법을 알 필요가 있음
'''

