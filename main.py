from logging import exception
from random import *

import rand as rand

"""-----------------------------------------
01. 문자열 출력하는 방법
---------------------------------------------"""

"""
print('tiger')
print(10)
# , 자동 스페이스 추가
print(10,'tiger',25,'eagle',3.14)
print(True, False)
print(10);print(20)
"""

"""
---------------------------------------------------
02. 줄바꿈
-----------------------------------------------------
print(10)
print(20,"\n")
print(10)
print('----------------------')
print('-'*50)
print('*'*50)

print('%d %d %s' % (10,20,'호랑이'))

print(10, 20, 30)
print(10, 20, 30, sep = '')
print(10, 20, 30, sep = '&')
print(10, 20, 30, sep = '_')

print(10, 20, 30, end = ' ')
print(10, 20, 30, end = '\n')
print(40, 50, 60)
print(type(10)); print(type(True)); print(type('Tiger'))
print(type([])); print(type(())); print(type({}))

print('호랑이'+'고양이')
print(10 + 22)
#print(10 + 'Tiger')
print(10+int('10'))
print('Tiger' + str(10))
"""
"""
-------------------------------------------------
03.파이선은 변수선업타입 없다 알아서 지정한다.
--------------------------------------------
"""
"""
a = 10; b = 20
print(a,b)
a = 30; b = 40
print(a,b)
a, b = 50, 60
print(a,b)
a = b = 70
print(a,b)

b = 3+4j

a = 10
b = 20
b,a = a,b
print(a,b)

a = a + 1
a += 1

a = 10
b = 20
print(id(a),id(b))

a = 'Tiger'
b = 'Eagle'
c = 'Tiger'

print(id(a),id(b),id(c))

a = 0x10
print(a)

b = 0o376
print(b)

a = 1+2j
print(a+b)

print(a / b)
print(a%b)
print(a//b)

a= 2**8;
print(2**8)
"""

"""
#print(round(3.1415, 4))
str = "무궁화꽃이피었습니다"
#print(srt[-2])
#print(str[2:5])
#print(str[5-0])
#print(str[5:])
#print(str[:5])
#print(str[:])

str = "Apple"
a = str[0]
b = str[:2]
c = "B"+str[1:]

print(c)
"""

#-----------------------------------------------
#짝짓기 2개 방법( %, { } )
"""
print('호%d랑%s이' %(10, '사과'))
print('호%d랑이' %10)  #한개일때 ()생략
print('무궁화{0}꽃이{1}피었습니다'.format(10, 'Tiger'))

print('가나다%d마바%s사' %(10, 100))
print('가{0}나다마{1}바사'.format(20, 2000))
"""

#이거 확인해봐야됨
"""
print('아침%s출근길' % '배고픈')
print('%s개구리가 %s뛰었습니다.' % ('미친','멀리'))
print('{0}새가 {1}날아갑니다'.format('배고픈','서쪽으로'))
s = '무궁화{0}꽃이 {1}피었습니다'
print(s)
s.format('무지개','아주많이')
print(s)
t = s.format('무지개','아주많이')
print(t)
s = s.format('무지개','아주많이')
print(s)
s = '무궁화꽃이무궁화피었무궁화습니다무궁화'
print(len(s))  #문자를 카운트
print(s.count('무궁화'))  #내가 찾고자 하는 문자열 카운트
print('무궁화꽃이무궁화피었무궁화습니다무궁화'.count('무궁화'))
s = '무궁화꽃이꽃이피았습니다.'
print(s.find('피었')) #처음 찾은 문자열의 시작 인덱스 번호 출력  검색실패가 뜨면 항상 -1을 리턴함
"""
#-----------------------------------------------

"""
s='무궁화꽃이무궁화피엇무궁화습니다무궁화'
print(len(s))
print(s.count('무궁화'))
print('무궁화꽃이무궁화피엇무궁화습니다무궁화'.count('무궁화'))
s = '무궁화꽃이꽃이피었습니다'
#find()에서 값을 못찾을 시 -1이 리턴됨
print(s.find('피'))
s = 'Apple'
t = 'Apple + Orange'

s = s + ' Banana'

print(s); print(t)
print(s.lower())
t = s.lower()
print(t)
print(s.upper())
print(s.replace('Banana', 'Orange'))
"""

#-----------------------------------------------
"""
s = '무궁화 꽃이 피었습니다'
#대괄호 열고닫고는 리스트 [] = 리스트
print(s.split()) #['무궁화', '꽃이', '피었습니다']
t = s.split()
print(t)
print(len(t))
print(t[0], t[1]*3, t[2])
s = '무궁화,꽃이,피었습니다'
print(s.split(','))
"""
#1. 산술연산-----------------------------------------------
"""
print(16+3)
print(16-3)
print(16*3)
print(16/3)
print(16//3)
print(16%3)
print(16**3)
"""
#2. 관계연산-----------------------------------------------
"""
print(3>2)
print(3<2)
print(3>=3)
print(3<=3)
print(3==3)
print(3!=3)
"""
#3. 논리연산-----------------------------------------------
"""
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print(False or False)
print(False or True)
print(True or False)
print(True or True)
"""
#3. 부정연산-----------------------------------------------
"""
print(not(3>2))

#아래문장 세 문장은 똑같다. 5가 4보다 크냐(o) 그리고 6이 8보다 작으냐(o)
print(3+2>4 and 6<2*4)
print(True and True)
print(((3+2)>4) and (6<(2*4)))
"""
# Random -------------------------------------------------------------
#0.0-1.0 사이의 숫자를 랜덤으로 뽑는다

"""
print(random())
print(randint(3,5))
print(randrange(10, 200, 15))
"""#print((3<= x <= 5))
#-------------------------------------------------------------
#확인필요
"""
a = int (input('입력하세요'))
#print(a,type(a)) #입력받은 내용을 문자로 처리함
print(a*3)
"""


#4대 제어문----------------------------------------------------------
#아래 문장은 파이선에서 괄호를 열고 닫아도 되지만 정석은 아님
#제어문의 끝에는 : 붙는다
#조건이 확인될때는 자동 탭처리 된다
#1. if  ----------------------------------------------------------
"""
if 3>2:
    print(3)
if 3 > 1:
    print(1)
else:
    print(0)
"""
"""
a = 200
b = 200
if b > a:
    print("big b")
if a == b:
    print("samosamo")
elif a > b:
    print("big a")
"""
# 키보드로 부터 2자리의 숫자를 입력 받아(0-100) 10의자리수와 1의 자리수를 짝수 홀수 구분하여 다음과 같이 출력할수있도록 하세요
# 홀홀 = 우동 홀짝 = 짜장 짝홀 = 냉면  짝짝 = 탕수육---------------------------------------------------------------
# num = int(input("숫자를 입력하라"))

"""
num = randint(1, 100)

print(num)

a = num // 10
b = num % 10

if a % 2 == 1:       #홀
    if b % 2 == 1:          #홀
        print('우동')
    else:                   #짝
        print('짜장면')
else:                 #짝
    if b % 2 == 1:          #홀
        print('냉면')
    else:                   #짝
        print('탕탕탕탕 탕수육')
"""

# ---------------------------------------------------------------------

"""
if (False):
    print('Tiger')
else:
    print('Elephant')

#none, '',  = False
if (''):
    print('Tiger')
else:
    print('Lion')

if not (''):
    print('Tiger')
else:
    print('Lion')

if [10, 20, 30, 40]:
    print(1)
"""

# ---------------------------------------------------------------------

"""
s = '무궁화 꽃이 피었습니다'
print(s.split())
m = s.split()
print(m)
"""
"""
if'무궁화' in m:
    print('찾앗다')
else:
    print('못찾앗다')
"""
"""
a = 0
while a < 10:
    a += 1
    print(a)
print('Tiger')
"""
"""
a = 0
while a < 10:
    a += 1
    if a == 3:
        continue
    if a == 6:
        break
    print(a)
print('Tiger')
"""
# 우박수 구하기 ---------------------------------------------------------------------
"""
num = 23
while(True):
    if num == 1:
        break
    if num % 2 == 1 :
        num = num * 3 + 1
    else:
        num = num / 2
    print(num)
print(num)
"""
# 아래 삼항연산 확인 필요!!
"""
num = 23
while(True):
    if num == 1:
        break
    if num % 2 == 1:
        num = num * 3 + 1
    else:
        num = num / 2
    num = num % 2 == 1 or num * 3 + 1 and num / 2

    print(num)
print(num)
"""


# print (range(0, 10), type(range(0, 10)))

"""
a = list(range(0, 10))
# a = 0 >= x > 10
print(a)
a = list(range(5, 10))
print(a)
a = list(range(3, 20, 2))
print(a)
"""

# 아래 for문 확인 필요
"""
for i in [1, 2, 3]:
    print(i)

for i in [1, 2, 3]:
    print(i, end='\n')

for i in [1, 2, 3]:
    print(i, end=' ')
print()

for i in ['월', '화', '수', '목', '금', '금', '금']:
    print(i, end=' ')
print()

for i in ['동물1', '동물2', '동물3', '동물4', '동물5', '동물6', '동물7']:
    print(i, end=' ')
print()

for i in range(0, 10):
    print(i, end=' ')
print()
"""
# 5단 출력 ---------------------------------------------------------------------

"""
for i in range(1, 10):
    a = 5*i
    print('5 * ', i, '=', a)
"""

# 1 - 10 더하기 ---------------------------------------------------------------------

"""
a = 0
for i in range(1, 11):
    a = a + i
print(a)
"""

# 2중 for 문 ---------------------------------------------------------------------

"""
for i in range(0, 3):
    for j in range(0, 4):
        a = i, j
        print(a, end='')
    print()
"""
"""
k = 0
for i in range(0, 3):
    #세로 반복 회수
    for j in range(0, 4):
        #가로 반복 회수
        print('%02d' %k, end=' ')
        k += 1
    print()
"""

"""
아래와 같이 결과물을 출력하시오
6 8 2 3 19
4 7 8 4 23
6 1 6 1 14
"""

"""
for i in range(0, 3):
    b = 0
    for j in range(0, 4):
        a = randint(1, 9)
        print(a, end=' ')
        b = b + a
    print(b)
"""

# ---------------------------------------------------------------------201027
"""
print(65)
print(chr(65))
print(ord('B'))
"""
# ---------------------------------------------------------------------
# CRUD 의 C 생성
# ---------------------------------------------------------------------

"""
a = [10, 20, 30]
print(a)
b = ['animal1', 'animal2', 'animal3']
print(b)
c = [10, 3.14, True]
print(c)
"""
"""
a = [10, 20, 30, 40]
#print(a)
print(a[0], a[1], a[2], a[3])
"""
#
"""
for i in a:
    print(i, end=' ')

for i in [1, 2, 3, 4]:
    print(i, end=' ')

"""
# 이 세개를 i 대신해서 많이 사용
"""
for value in a:
    print(value, end=' ')
for item in a:
    print(value, end=' ')
for data in a:
    print(value, end=' ')
"""
# ---------------------------------------------------------------------
# CRUD 의 Update
# ---------------------------------------------------------------------
"""
a = [10, 20, 30, 40]
a[0] = 50
print(a)
print(id(a[0]), id(a[1]))
a[0] = 60
print(id(a[0]), id(a[1]))
"""
# ---------------------------------------------------------------------
# CRUD 의 Delete
# ---------------------------------------------------------------------
"""
del a[0]
print(a)

print(len(a))
"""

# 콤마 중요
"""
a = [10, 'Tiger', [200, 'Elephant', [30, 'Eagle']]]
print(a)
print(a[2][1])
print(a[2][2][1])

a = 'Apple'
a = ['a', 'p', 'p', 'l', 'e']
print(a[0])
a[0] = 50
print(a)
"""
"""
a = ['a', 'b', 'c', 'd', 'e']
#인덱스 번호 1번 부터 3-1 개 까지 가져오세요
print(a[1:3])
a[1:3] = 'Foo', 'woo'
print(a)
a[1:3] = 'Hoo', 'Joo', 'Koo', 'Loo'
print(a)
"""
# Delete Skill
"""
a = ['a', 'b', 'c', 'd', 'e']
# a[1:3] = []
print(a)

del a[1:3]
print(a)
"""
"""
a = ['o', 'r', 'a', 'n', 'g', 'e']
print(a)
a.append(10)
print(a)
a.insert(0, 10)
print(a)
a.pop()
print(a)
a.pop(3)
print(a)
"""
"""
a = ['o', 'r', 'a', 'n', 'g', 'e']
a.remove('a')
a.remove('n')
try:
    a.remove('kk')
except: print('예외 발생')
pass

# 프로그램에서 못찾으면 익셉션 처리한다

b = a.index('g')
print(b)

a.sort()
print(a)
a.reverse()
print(a)
"""
"""
a = ['a', 'c', 'e', 'f', 'd', 'b']
a.sort()
print(a)

a = ['a', 'c', 'e', 'f', 'd', 'b']
a.reverse()
print(a)

a = ['a', 'c', 'e', 'f', 'd', 'b']
a.sort(reverse=True)
print(a)
"""
# append ---------------------------------------------------------------------
"""
a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 2, 3]
a.append([4, 5])
print(a)

a = [1, 2, 3]
a.extend([4])
print(a)

a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

a = [1, 2, 3]
a = a + [4, 5, 6]
print(a)
"""

#  tuple---------------------------------------------------------------------
"""
a = (10, 20, 30)
b = [10, 20, 30]
print(a, type(a))
print(b, type(b))

a = 10,
b = (10,)
c = 10
d = (10)
print(type(a), type(b), type(c), type(d))
f = 10, 20, 30
print(type(f))
e = b, a, c, d, f
print(type(e))
f = [10, 20, 30]
print(type(f))
e = [b, a, c, d, f]
print(type(e))

a = [10, 20, 30]
b = tuple(a)
print(type(a), type(b))
print((10,) + (20, 30))
print('호' + '랑')
a = 1, 2, 3, 5
b = 1, 2, 3
c = a + b
print(c)
print(a == b)
print(a <= b)
for number in a:
    print(a)
"""
"""
#리스트 수정 어떻
a = 10, 20, 30
b = [10, 20, 30]
print(a[0])

#b[0]= 200  #실패
b[0]= 200   #성공
print(a)

a = [10, '호랑이', [20, 30], (40, '코끼리', [50, 60], [70, 80])]  #중첩가능
print(a)

a = []
b = list()
print(type(a), type(b))
c = ()
d = tuple()
print(type(c), type(d))
"""
"""
e = [10, 20]
f = list('apple')
print(e, f)

a = 'Ti ge r'
b = a.split(' ')
print(b)
# 오프셋 기준점으로부터 상대적으로 떨어진 거리
a = [10, 20, 30]
print(a[0], a[-0])  #-는 오른쪽부터
"""
#  dictionary---------------------------------------------------------------------
"""
# a = {k : v, k : v...} dictionay
a = {1: 10, 2: 20, 5: 40}
print(type(a))
print(a)
a = {10: 'Tiger', 20: 'Elephant', 30: "Eagle"}
print(a)
a = {1: 10, 2: 20, 2: 30} # 중복시 값 갱신 최근 데이터로 출력
print(a)
a = {1: 10, 2: 'Tiger', 3: [10, 20], 4: (30, 40), 5: {6: 10, 7: 10}}
print(a)
a = {'호랑이': 10, '코끼리': 20, '독수리': 30}
print(a)
a = {'name': '홍길동', 'age': 20, 'salary': 300}
print(a)
"""
"""
#  dictionary CRUD_C ---------------------------------------------------------------------
a = {}
a['name']= '독수리'
a['age']= 20
a['height'] = 100
b = a['name']

#  dictionary CRUD_U ---------------------------------------------------------------------
print(b, a['name'])
a['name'] = '도깨비'
print(a)

#  dictionary CRUD_D ---------------------------------------------------------------------
del(a['name'])
print(a)
#del a['name']  이거도 가능
print(a)
"""
"""
a = {'name': '홍길동', 'age': 20, 'salary': 300}
b = a['name']
c = a.get('name')
#print(b)
#print(c)
#print(a.keys())
#print(a.values())
#a = range(0, 10)
#print(a)
#for i in a.keys():
#    print(i)

print()
for data in a.items():
    print(data[1])
#    print('Tiger')
#    print(type(data))
for value in a.values():
    print(value)
for key in a.keys():
    print(key)
"""
#얕은 복사는 공유 깊은복사는 완전히 새로운것을 만드는것
""" 얕은복사
a = [1, 2, 3]
b = a
a.append(5)
a.append(99)
print(b)
print(id(a))
print(id(b))
"""
"""#깊은복사
a = [1, 2, 3]
b = a[:]
a.append(5)
a.append(99)
print(a)
print(b)
print(id(a))
print(id(b))
"""
"""
import copy
a = {1: 100, 2: 200, 3: 300}
b = copy.deepcopy(a)
print(a)
print(b)
print(id(a))
print(id(b))
"""
"""
def func01():
    print(1)
    print(2)
    print(3)


print(99)
func01()
print(100)
func01()

def func02(sinlim):
    print(sinlim)
    print(sinlim*sinlim)


func02(50)

def func03():
    print('함수3번')
    return 100


func03()
a = func03()
print(a)
print(func03()*7)
"""

# 정말 이것은 주의하자 당연히 사용할수없다
# print(func03())
"""
def func04(num):
    print('함수 4번', num)
    return 777

func04(100)
a = func04(200)
#print(a)
print(func04(300))
"""


"""
# 전달인수 업고 리턴 없다
def funcnono():
    print(1)


funcnono()


# 전달인수 있고 리턴 없다
def funcyesno(num):
    print(2)


funcyesno(1)

# 전달인수 없고 리턴 있다
def funcnoyes():
    print(3)
    return 33


a = funcnoyes()
print(a)
print(funcnoyes()*7)
funcnoyes()


# 전달인수 있고 리턴 있다
def funcyesyes(num):
    print(4)
    return 44


a = funcyesyes(1)
print(a)
"""
"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a < b)
print(a <= b)
print()

a = [1, 2, 3]
b = [1, 2, 3, 4]
print(a < b)
print(a <= b)
print()

a = [1, 2, 3]
b = [1, 2, 3, -4]
print(a < b)
print(a <= b)
print()

a = [1, 2, 3, 4, 5]
b = [1, 3, 4, 6]
print(a < b)
print(a <= b)
print()
"""
"""
def func05(a, b, c):
    sum = a * b + c
    print(sum)
    print(a * a + b * b + c * c)



func05(2, 3, 4)
func05(3, 4, 5)
"""
"""
def func06():
    print(1)
    return;
    print(2)



func06()
"""
"""
def func07(a, b):
    print(7)
    print(type(a), type(b))



func07(10, 'Tiger')

def func08(a, b, c = 10, d = 20):
    print(a, b, c, d)



func08(1, 2)
func08(1, 2, 3)
# 함수의 인수값을 초기화
# 주의! 함수의 인수의 끝에서부터 초기화를 시켜서 들어온다
"""
"""
#아래꺼 가변인수전달
def func09(*args):
    print('*'*30)
    for data in args:
        print(data)


func09()
func09(10, 20)
func09(10, 20, 'Tiger')

def func10(a, b, *args):
    print(a, b)
    for data in args:
        print(data)


func10(1, 2)
func10(100, 200, 300)
func10(100, 200, 'Tiger')
"""
"""
#딕셔너리 3가지 방법으로 출력

def func11(a, b, *args, color, data):
    print(a, b, color, data
          )

func11(1, 2, color = 3, data = 4)

def func12(**star):
    print(star)
    print(type(star))
    for values in star.values():
        print(values)
    for item, v in star.items():
        print(item, v)
    for keys in star.keys():
        print(keys)
    for items in star.items():
        print(items)



func12(a = 10, b =20)
"""
"""
class Apple:                #클래스
    def __init__(self):     #생성자
        print('hello')


a = Apple()                  #객체

class Apple:                #클래스
    def __init__(self):     #생성자
        pass


a = Apple()                  #객체

class Apple:
    def __init__(self):
        print(123)
    def func01(self):
        print(1)



a = Apple()
a.func01()
"""
# 기본함수 4개 정의 ( 1. 전달 x 리턴 x, 2. 전달 o 리턴 x, 3. 전달 x 리턴 o, 4. 전달 o 리턴 o)
# class Apple:
#     def __init__(self):
#         pass
#
#     def func01(self):
#         print(1)
#
#     def func02(self, name):
#         self.name = name
#
#     def func03(self):
#         return 100;
#
#     def func04(self, age):
#         return 100;
#
#
#
# a = Apple()
# a.func01()
# a.func02('Spencer')
# a.func03()
# a.func04()

# self =자바의 this 다

# class Apple:
#     def __init__(self):
#         print(id(self))
#         pass
#
#
#
# a = Apple()
# print(id(a))

# 눈으로 많이 보는 코드!!!
# 동적 = dynamic(필요할때 만듬), 정적 = static(처음부터 끝까지)
# class Apple:
#     # num = 10
#
#     def __init__(self, num):
#         self.num = num
#
#     def func(self):
#         print(self.num)
#
# a = Apple(20)
# # print(a.num)
# a.func()

# class Apple:
#     a1 = 10
#
#     def __init__(self):
#         self.a2 = 100
#
#     def func(self):
#         n3 = 30
#         print(self.a1, self.a2, n3)
#
#
# a = Apple()
# a.func()

# class Apple:
#     def __init__(self):
#         pass
#     def func1(self):
#         print(1)
#     def func3(self):
#         print(3)
#
#
# class Orange(Apple):
#     def __init__(self):
#         pass
#     def func2(self):
#         print(2)
#     def func3(self):
#         print(333)
#     def func4(self):
#         self.func2()
#         self.func3()
#         super().func3()
#
# a = Orange()
# a.func3()
# a.func2()
# a.func1()
# a.func4()
#
# print(Apple.mro())
# a1 = Apple()

# class Dog:
#     def __init__(self):
#         pass
#     def cry(self):
#         print('개울어요')
#
# class Cat:
#     def __init__(self):
#         pass
#     def cry(self):
#         print('고양이울어요')
#
# class Snake:
#     def __init__(self):
#         pass
#     def cry(self):
#         print('뱀울어요')
# class Animal:
#     def __init__(self):
#         pass
# a = Dog()
# a.cry()
# b = Cat()
# b.cry()
# c = Snake()
# c.cry()
# a4 = [Dog(), Cat(), Snake()]
# print(a4)
# for Animal in a4:
#     Animal.cry()

# class Apple:
#     def func1(self):
#         print(1)
#         pass
# def func2(a):
#     print(2)
# func2(Apple())
# a = Apple()
# a.func1()

# class Zoo:
#     def __init__(self, Animal):
#         self.Animal = Animal
#     def cry(self):
#         # self.Animal()
#         self.Animal.cry()
#
# class Dog:
#     def cry(self):
#         print('망망')
# class Cat:
#     def cry(self):
#         print('야옹')
#
# t1 = Zoo(Dog())
# t1.cry()
# t2 = Zoo(Cat())
# t2.cry()

# a = 4 / 0

# try:
#     a = 4 / 0
#     print(0)
# except:
#     print(1)
#
# print(2)

# try:
#     a = 4 / 0
#     print(0)
# except Exception as e:
#     print(1)
# finally:
#     print(3)
# print(2)

# a = [10, 20, 30]
# b = a.index(30)
# print(b)
# try:
#     c = a.index(100)
# except Exception as e:
#     print(e)
#
# print('Tiger')

# file = open("sample.txt", "w", encoding="utf-8")
# file.write("코끼ㅣ리")
# file.close()

# for i in range(5):
#     print(i)
#
# for i in range(2, 7):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)

# file = open("sample.txt", "w", encoding="utf-8")
# for i in range(5):
#    file.write("호랑이")
# file.close()

# file = open("sample.txt", "w", encoding="utf-8")
# for i in range(5):
#    file.write(str(i))
# file.close()

# 파일 = 오픈, 클로즈 생략 가능 한 문장
# with open("sample.txt", "w", encoding="utf-8") as file:
#     for i in range(1):
#         file.write("호랑이" + str(i) + "\n")

# file = open("sample.txt", "r", encoding="utf-8")
# data = file.readline()
# print(data)
# if data:
#     print(10)
#
# data = file.readline()
# print(data)
#
# if data:
#     print(20)
# file.close()
#
# if "호랑이":
#     print(1)
# if "":
#     print(2)


# file = open("sample.txt", "r", encoding="utf-8")
# while True:
#     data = file.readline()
#     print(data)
#     if not data:
#         break
# file.close()

# file = open("sample.txt", "r", encoding="utf-8")
#
# data = file.readlines()
# print(data, end="")
#
# for item in data:
#     print(data[0])
#
# file.close()
#
# a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4\n']
#
# for i in range(0, len(a)):
#     a[i] = a[i].replace('\n', "")
#
# print(a)
#
# a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4\n']
# print(a)
# for i, v in enumerate(a):
#     print(i, v)
#     a[i] = v.replace('\n', '')
# print(a)

# file = open("sample.txt", "r", encoding="utf-8")
# data = file.read()
# file.close()
#
# print(data)

# import Tiger
# Tiger.func1()
# from Tiger import *
# func1()
# import Tiger as t
# t.func1()
# import A as b

# print(__name__)
#
# import Tiger as t
# t.func2()

# 주석을 잡아서 설명을 해야되는데 정리가 안되네...
# if __name__ == '__main__':
#     import Tiger as t
#     t.func1()
#     print('yessirskiii')
#
# def main():
#     print(1)
#
#
# if __name__ == '__main__':
#     main()

# Apple = {'n1':'호랑이', 'n2': '호호호항히', 'n3': '코끼리'}
# print(Apple['n1'])
#
# Orange = {10: 20, 20: '독수리', 30: True}
# print(Orange[10], Orange[20])

# Kiwi = {'이름': '홍길동',
#         '나이': 20,
#         '특기': ['독서', '무술', '프로그램'],
#         '가족': {'어머니': '엄마', '아버지': '아빠'}
# }
# print(Kiwi['이름'], Kiwi['나이'])
# print(Kiwi['특기'][0])
# print(Kiwi['가족']['어머니'])

# data = {
#     "response":{
#         "body":{
#             "items":[{
#                     "addr":1234,
#                     "name":"홍길동"
#                 },
#                 "득템"
#             ]
#         },
#         "page":100
#     },
#     "header":{
#         "result":200,
#         "msg":"OK"
#     }
# }
# print(data["response"]["body"]["items"][0]["addr"])
#
# print(data["response"]["body"]["items"][0]["name"])
# print(data["response"]["body"]["items"][1])

# Apple = {'n1':'호랑이', 'n2': '호호호항히', 'n3': '코끼리'}
# print(Apple['n1'])
# print(Apple.get('n3'))
# try:
#     Apple['n4']
# except:
#     print('검색하지 못했습니다')
#
# num = print(Apple.get('n4'))
# print(num)
# if num == None:
#     print('검색 못햇어요')

# A = [10, 20, 30]
# print(sum(A))
# a = 3, 4, 5, 6
# print(sum(a))

# def func1(a):
#     return a > 0
#
# print(list(filter(func1, [-2, -1, 0, 1, 2])))

# def f1():
#     print(1)
# # f1()
# a = f1
#
# def f2():
#     print(2)
#
# def f3(tt):
#     tt()
#     print(3)
# print(f3(f2))
#
# def f4():
#     return 999
#
# def f5(tt):
#     print(tt)
#
# f5(999)

# def f1(num):
#     t = {10: '호랑이', 20: '독수리', 30: '앵무새'}
#     return t[num]
# print(f1(10))

# 반복문과 조건문을 이용하여 리스트 생성 = 컴프리핸숀
# a = [i for i in range(5)]
# print(a)
#
# a = [i*3 for i in range(5)]
# print(a)

# a = [10, 20, 30, 40]
# b = [i + 2 for i in a if i > 25]
# print(b)

# print(dir(()))

# a = [10, 20, 30, 40]
# a.insert(3, 99)
# print(a)
# a.append('호랑이')
# a.append(100)
# a.insert(len(a), 99)
# a.remove(10)
# print(a)

# a = [10, 20, 30, 40]
# # b = a.pop(2)
# # print(b)
# print(a)
# print(filter(a.remove, ))

# index value
# a = [10, 20, 30]
# for key, value in enumerate(a):
#     print(key, value)
# a = 'print(10 + 20)'
# eval('print(10 + 20)')
# lean 3,5,7
# max(3,4,5,6)
# a = list 1,2,3,4
# print(a)
# print(bin(200))
# print(oct(100))
# print(hex(100))
# a = int('123')
# print(type(a))
# a = str(123)
# print(type(a))
# a = list('Apple')
# print(type(a))
# a = divmod(7, 3)
# print(type(a))
# for i in a:
#     print(i)
# print(True and True)
# print(all[True, True, True])
# print(True or True)
# a = [2, 7, 3, 9, 5]
# a.sort
# print(a)
import time
# a = time.localtime(time.time())
# print(a.tm_year)
# print(a)
# b = ['월', '화', '수', '목', '금', '금', '금']
# print(b[a.tm_wday()])
# datetime.now()
# print(time.perf_counter())
# time.sleep(1)

def f1():
    print(1)
f1()

f2 = lambda: print(12)
f2()
print(type(f2))

f3 = lambda x: print(x)
f3(3)

f4 = lambda x, y: print(x + y)
f4(10, 20)

f5 = lambda x, y: x + y
print(f5(100, 200))

def f6(ff) : ff()
def f2():
    print('Tiger')
f6(f2)

f6(lambda : print('코끼리'))

def func03(ff) : ff(10,20)
func03(lambda x,y : print(x+y))

def f1(a):
    return a>0

a = filter(f1, [-2, -1, 0, 1, 2])
print(list(a))

a = filter(lambda a: a>0, [-2, -1, 0, 1, 2])
print(list(a))

a = (i for i in range(5))
print(type(a))
b = sum(a)
print(b)

#sum(리스트) sum(generator))

