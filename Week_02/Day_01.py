'''
a = []
b = [1, 2, 3, 4, 5]
c = ["홍길동", "김길동", "이길동"]
d = [1, 2, 3, "무송", "화영"]
e = [1, 2, 3, [4, 5, 6]]
f = [b, c]
g = list() #비어있는 리스트
print(a, b, c, d, e, f, g)

a = [1, 2, 3, 4, 5]
print(a[2])
print(a[-3])

b = a[0] + a[3]
print(b)

c = [1, 2, 3 "a", "b", "c"]
#print(c[2] + c[4]) #타입이 맞지않음

a = [1, 2, 3, [4, 5, 6], 7, 8, 9]
print(a)
print(a[3][1]) #a[3] = [4, 5, 6]

b = [1, 2, [3, 4, [5, 6]]]
print(b)
print(b[2][2][1])

list = [1, 2,[5, 6, 7, 8, [9, 10]], 3, 4]
print(list[2][3], list[2][4][1], list[-1])
print(list[2][4][1])

a = "I love Python"
print(a[2: 7])
b = ["I", " ", "l", "o", "v", "e"]
print(b[2: 4])

b = [1, 2, 3, [4, 5, 6, 7]]
print(b[3][1:3])

c = [1, 2, 3, [6, 7, [10, 11, 12], 8, 9], 4, 5]
print(c[3][2][:2], c[3][3:])

a = [1, 2, 3]
b = [2, 3, 4]
c = a + b
print(c)
d = c * 3
print(c)
print(len(d))
print(len(c))

f = [1, 2, 3, [6, 7, [10, 11, 12], 8, 9], 4, 5]
print(len(f))
print(f)

a = [1, 2, 3, 4, 5, 6, 2, 3, 5, 2, 1]
a.append(5)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

b = [1, 5, 6, 7, 1, 3, 5]
print(sorted(b))
print(list(reversed(b)))
print(b)

a = ["안", "녕", "하", "세", "요"]
print(a.index("녕"))
a.insert(1, "영")
print(a)

g = [5, 4, 3, 2, 1]
g2 = g.pop()
print("g2 : ", g2)
print(g)

i = [1, 2, 3, 3, 4]
j = [3, 4, 5]
print("3의 갯수 : ", i.count(3) + j.count(3))
print(i)
print(j)
i.extend(j)
print(i)
print(j)

x = [1, 3, 5, 4, 2]
print(list(reversed(sorted(x))))
x.sort(reverse=True)
print(x)

a = [1, 2, "a", "b"]
b = (1, 2, "a", "b")
print(type(a))
print(type(b))
a[1] = 3
#b[1] = 3 #튜플 요소 변경불가
print(a, b)

a = ()
b = (1, )
c = (1, 2, 3, "a", "b")
d = 1, 2, 3, 4, 5
e = (1, 2, (3, 4), 5)
print(a, b, c, d, e)
test = (1, 2, 3, 4, 5)
print(test[3])
print(test[:2])

a = (1, 2, 3)
a = a + (4, 5)
print(a)

asd = {
    "가위" : "주먹",
    "주먹" : "보",
    "보" : "가위"
}
#print(asd["가위"])

print("가위바위보 족보")
while True:
    a = input()
    if a == "종료":
        print("종료합니다.")
        break
    elif a not in asd:
        print("다시 입력해주세요.")
    else:
        print(f"{asd[a]}를 내세요.")

dic = {}
print(dic)
dic1 = {
    1: "무송",
    2: "호연작",
    3: "송강"
}
print(type(dic1))
#print(dic1[0]) #인덱스 접근불가 오류
print(dic1)
dic1[1] = "임충"  #dic[Key] = value 요소 변경
print(dic1)
dic1[4] = "화영"  #dic[Key] = value 요소 추가
print(dic1)
del dic1[3]     #del dic[Key] 요소 삭제
print(dic1)

dic2 = {
    1: "무송",
    2: "무송",
    3: "송강",
    4: "화영"
}
print(dic2)

test = {
    "이름": "Musong",
    "나이": 30,
    "주소": "Pusan",
    "신조": ["믿음", "소망", "사랑"]
}
print(test)
del test["주소"]
print(test)
print(test["나이"])
print(test["신조"][1:])

a = {
    1: "a",
    1: "a",
    1: "c",
    2: "d"
}
print(a)
b = {
    1: "a",
    2: "a",
    3: "a",
    4: "d"
}
print(b)

b_keys = list(b.keys())
print(b_keys)
b_values = list(b.values())
print(b_values)
b_items = list(b.items())
print(b_items)
print(b_items[1][1])
#b.clear() #전체 삭제
print(b[4])
print(b.get(4)) # 키값 입력시 밸류값 리턴
print(4 in b)
print("b" in b)
'''
user = {
    "name": "Paul",
    "birth": "11/28",
    "age": 30
}
print(user)
user["age"] = 35
print(user)
user["주소"] = "서울"
print(user)
