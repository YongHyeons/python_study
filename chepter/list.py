# List
# - 컨테이너 자료형
# - 여러 literal을 묶어서 관리할 수 있음
# - ** 저장된 순서를 기억 **
# - 시퀀스형(str, list, tuple) : 인덱싱/슬라이싱 가능, 멤버쉽 확인 가능

lst = [1,2,3] # 0, 1, 2 번지에 값 할당
print(lst, type(lst))

print(lst[0], lst[1], lst[2])

# list는 요소를 추가/ 삭제 가능한 mutable 자료형이다.
# string 같은 경우엔 변수의 내용물을 바꿨을때 id 값, 그러니까 메모리값을 변경했는데 list 경우엔 그대로 사용한다
print('변경전 id : ',id(lst))

# 맨뒤에 요소 추가
lst.append(4)
print(lst)
print('변경후 id : ',id(lst))

# 원하는 인덱스 요소 추가
lst.insert(1,1.5)
print(lst)

lst.insert(0,0)
print(lst)

# 값 변경
lst[0] = -1
print(lst)

# 특정 인덱스 값 제거
lst.pop(2)
print(lst)

# 2차원 list
students = [['홍길동',20],['신사임당',22,'여'],['이순신',48,'전남','여수시']]
print(students)

# 인덱싱 (차례대로)
print(students[0])
print(students[0][0])

print(students[1][2])
print(students[len(students)-1][len(students[len(students)-1])-1])

# csv 데이터를 list로 관리 --> 정말 자주 쓸거임
# - csv : Comma Seperated Value
# - 말은 Comma 지만 띄어쓰기, tap, / 등등 여러가지로 나눌 수 있음
# - '홍길동,20,서울,서초구'
data = '홍길동,20,서울,서초구'
data_ = data.split(',')
print(data_, type(data_))

name = data_[0]
age = data_[1]
add1 = data_[2]
add2=data_[3]
print(name,age,add1,add2)

# list 반복 순회가능
# 모든 iterable형은 반복문이 가능
lst = ['a', 'b', 'c']
# for 변수 in 순회객체 :
for v in lst:
    print(v)

# 인덱스 순회
for index, v in enumerate(lst):
    print(index, v)

# 더하기/곱하기 연산
foods = ['🍔', '🍖']
drinks = ['☕']
print(foods + drinks)
# 결과값 : ['🍔', '🍖', '☕']
# 이렇게 나오지 않음 -> [['🍔', '🍖'],['☕']]
print(foods * 3)

# list api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#list

# list.sort() - mutable 연산 (직접 리스트를 바꿈 : in-place 연산)
# sorted() - immutable 연산 (직접 리스트를 바꾸지 않고 새로 만들어서 줌 : not-in-place 연산)

fruits = ['orange', 'apple', 'banana', 'kiwi']
# fruits.sort() # 숫자는 낮은순부터, 영어는 알파벳순으로 오름차순을 만들어줌
# fruits.reverse() # 이렇게 하면 그냥 기존에 있던 순서를 꺼꾸로 바꿔줌
fruits.sort(reverse=True) # 이렇게 하면 알파벳 역순으로 만들어줌
print(fruits)

nums = [20, 25,10, -10]
nums.sort()
print(nums)

# key 정렬함수 ---->?????
fruits.sort(key=len)
print(fruits)

# 커스텀 정렬 기준함수
def my_sort(elem):
    return len(elem) , elem # tuple 로 우선순위 지정

fruits.sort(key=my_sort)
print(fruits)

print('list.sort() 반환값 : ', fruits.sort()) # 반환하지 않음. none

#sorted를 이용해서 immutable연산처리 -> 새로 만들어 줌
fruits = ['orange', 'apple', 'banana', 'kiwi']
fruits1 = sorted(fruits)
print(fruits1)

# slicing 을 통한 값 변경
# --> texts 는 그대로 있음 -> 이 말은 즉, slicing 을 만들땐 immutable 로 해서 보여줌 (not-int-place)
texts = ['hello', 'hi', '안녕', '곤니찌와']
print(texts[:2], type(texts[:2]))

# 이렇게 대입했을땐 mutable 방식으로 처리가 됨 in-place
texts[:2] = ['ㅋㅋㅋ', '호호호']
print(texts)

# 연결 연산 결과를  기존 list에 반영
a = [1, 2]
b = [3, 4]
c = a+b
print(a,b,c)
# a와 b 는 직접 영향을 받지 않았다는걸 알 수 있음
# 만약 a + b 를 진짜 a 에 적용하고 싶으면 어떤식으로 해야할까?
# mutable 이 아닌 immutable 식으로 하고 싶다면?
# a = a + b 이런식으로 바로 담아주면 된다
# 저렇게 쓰는것보단 프로그래밍에서는 a += b 를 더 선호함
a += b
print(a)

