# dict
# - dictionary 사전 자료형
# - 하나의 요소(item)를 key - value 형식으로 저장
# - 하나의 dict 안에 key 는 중복될 수 없다.
# - key 는 immutable 자료형(int, float, str, tuple) 만 가능하다. -> list 불가능
# - value 는 모든 자료형 가능, 중복도 가능
# - 저장된 순서를 기억하지 않는다 (key를 통해 value 를 조회 -> 그래서 index 가 필요가 없음)
# - indexing, slicing 불가능

dct = {}
dct = {
    'a' : 10,
    'b' : 20,   # list, tuple, dic 다 마지막에 콤마(,) 써도 상관없음
    'a' : 100   # 이렇게 중복이 될 경우 오류를 내지 않고 둘다 존재할 수 없으니 덮어써버린다. (마지막꺼가 최종)
}
print(dct,type(dct))

# 요소 조회
print(dct['a'], dct['b'])
key = 'a'
print(dct[key])

# 다만 존재하지 않는 key 를 검색하면 list에서 존재하지 않는 index 찾았던것 처럼 key 오류가 난다
# print(dct['c']) #KeyError: 'c'

# 이런 상황을 방지하기 위해 get() 이 존재함
print(dct.get('a'))
print(dct.get('c')) # 존재하지 않는 key 값 조회시 기본값 (None)처리
print(dct.get('c', '값없음')) # 존재하지 않는 key 값 조회시 뒤에 써준 걸로 표시해줌

# 요소 추가
dct['c'] = 3
print(dct)

dct.update({'d': 4, 'e': 5})
dct.update(f=5)
print(dct)

# 값(value) 제거
dct['f'] = None
print(dct)

# 요소(item) 제거
dct.pop('e')
print(dct)

# dict 내장함수
dct2 = dict(name = '홍길동', age = 22)
print(dct2)

# key/value 로 구성된 tuple 을 list로 전달
dct3 = dict([('name', '신사임당'), ('age', 33)])
print(dct3)

# dict api
# https://docs.python.org/ko/3.13/library/stdtypes.html#dict

# dict.key()
keys = dct3.keys()
print(keys, type(keys)) # <class 'dict_keys'>

# dict.values()
values = dct3.values()
print(values, type(values)) #<class 'dict_values'>

# dict.items()
items = dct3.items()
print(items, type(items)) # <class 'dict_items'>

# dict 반복 순회하면서 많이 씀 (iterable)
for key in dct3:
    print(f' {key} = {dct3[key]}')

for key in dct3.keys():
    print(f' {key} = {dct3[key]}')

# 이렇게 둘이 똑같음. dct3.keys() 이렇게 하면 더 명확하게 적는것

# 만약 value만 나타내고싶다?
for value in dct3.values():
    print(value)
# 참고로 dictionary 는 key 를 통해 value 를 찾는거지 value 를 통해 key 를 찾는건 없다

for item in dct3.items():
    print(item, type(items))

#보통은 위처럼 잘 안쓰고 밑에처럼 쓴다
for key, value in dct3.items():
    print(key, value)

abc = ('A','a')
m,n = abc
print(m,n) # 이런 느낌으로다가 위에 코드를 사용하는것

# 프로그래밍 할때는 복사할일이 많은데 거기엔 얕고 깊은 복사가 있다 (list,set,tuple 다 해당됨)
# 얕은 복사 (sallow copy) : 특정 객체 (메모리 조각) 에 대한 참조 주소만 복사
# 깊은 복사 (depp copy) : 특정 객체 내용에 대한 실제 복사
sample = {
    'name' : '기계식 키보다',
    'price' : 30000,
    'origin': 'kor',
}

# 얕은 복사 : sample 의 주소값만 복사가 됨
other = sample
print(id(sample), id(other))

sample['name'] = '멋진키보드'
print(other['name'])
# 분명 Sample의 정보를 바꿨는데 other 에서 이름도 바뀌는것을 볼 수 있음 . 왜냐하면 같은 메모리주소에 있는걸 나타내니까

#같은 객체 여부 검사
print(sample is other)

# 깊은 복사 copy()
another = sample.copy()
print(id(sample), id(another))
print(sample is another) # False 내용이 같은지 물어보는게 아니다

sample['price'] *= 10

print(sample)
print(another)  # 공간이 아예 다르기 때문에 sample 값을 변경했을때 another의 값까지 바꾸지 않는다

# 리스트 얕은 / 깊은 복사
prices = [10000,20000,30000]

# prices의 복사본을 만들어 원본과 동시에 관리
prices_change = prices
prices_change[0] = 100
print(prices)
print(prices_change)
# prices의 복사본을 만들어 각각 10% 값을 올려서 관리 (원본은 변경되면 안됨)
prices_discount = prices.copy()
prices_discount[0] *= 1.1
prices_discount[1] *= 1.1
prices_discount[2] *= 1.1
prices_discount[3] *= 1.1

print(prices)
print(prices_discount)