# 형변환 : 자료형이 바뀌는 것을 말함
# - 암묵적 또는 명시적으로 자료형을 변환하는것

# 1. 암묵적 형변환
print(1+2.3) # type : int + float -> int 가 float으로 바뀌어서 float + float -> float 계산이 되는것
print(True + 2) # bool + int -> True는 1로 False 는 0 으로 반환이 되어 계산이 가능해짐 -> int + int -> in 결과값 : 3
print(True + True) # bool + bool -> int + int -> int 결과값 : 2

# 이게 안먹힐때가 있음
# 2. 명시적 형변환
# print('안녕' + 123) # TypeError: can only concatenate str (not "int") to str
print('안녕' + str(123)) # '안녕' + '123' -> '안녕123'

height = 175.456
print(int(height)) # 가장 간단하게 소수점 이하를 날려버리는 방법

value = '1234.567'
print(value*10) # 나는 1234.567 * 10 을 하고싶었는데 문자열이 10번 반복되게 됨
print(float(value)*10)

# 3. 논리형으로의 암묵적 형변환
# - 값이 있으면 True, 값이 없으면 False

# 값이 있는 경우
print(100,bool(100)) # 값이 있음
print(-100,bool(-100)) # 실수여도 값 o
print(' ', bool(' ')) # --> 띄어쓰기가 있으면 값이 있음
print('abcd', bool('abcd'))
print([1,2], bool([1,2]))
print((1,2), bool([1,2]))
print({'is_friday' : True} , bool({'is_friday' : True}))

# 값이 없는 경우
print(0, bool(0)) # 0은 값이 없음
print(0.0, bool(0.0))
print('', bool(''))
print([], bool([]))
print((), bool([]))
print({}, bool({}))

# 언제 쓰는지 예시
lst = []
if lst:
    print('list에 요소가 존재합니다.')
else:
    print('list에 요소가 존재하지 않습니다.')
