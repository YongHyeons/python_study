# tuple
# - 변경 불가한 (immutable) list
# - 저장 순서 기억

t1 = () # 빈 tuple 생성 - 가끔 씀
t2 = (10, ) # 하나만 만들고 싶을때 , 필수
# t2 = (10) -> 이렇게 할 경우엔 그냥 10과 동일하게 됨
t3 = (10,20) # 괄호 생략 가능하지만 그냥 쓰자

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))

# 대부분의 tuple 은 읽기 전용으로만 쓰고,
# 시퀀스 형이기때문에 indexing, slicing 가능

tpl = ('a', 'b', 'c', 'd')
print(tpl[0], tpl[1], tpl[2], tpl[3])
print(tpl[:3])

# tuple은 쓰기 바꾸기 오류남
# tpl[0] = 'A' #TypeError: 'tuple' object does not support item assignment
# 그렇다면 바꾸고싶을땐 어떻게 하나? -> 새로 만들어야함
tpl_ = ('A',tpl[1], tpl[2], tpl[3])
# tpl_ = ('A', *tpl[1:]) # *: unpacking 연산자 (안에 있는걸 꺼내줌) 결과값 : ('A', 'b', 'c', 'd')
# tpl_ = ('A', tpl[1:]) # 결과값 : ('A', ('b', 'c', 'd'))
print(tpl_)

# tuple 활용
# - 복수개의 값을 변수에 할당
# - 값 교환
# a= 100
# b - 200
a,b = 100, 200
print(a,b, type(a),type(b))

x, y = 100, 200
print(f'x={x}, y={y}')
x, y = y, x
print(f'x={x}, y={y}')