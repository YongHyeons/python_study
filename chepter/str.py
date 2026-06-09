# str
# - 문자열
# - ' " ''' """ 로 감싸서 표현

S = '안녕'
s = "안녕"

print(s, type(s))

a = """
문자열 주석 아님. 
그냥 문자열!
"""

print(a, type(a))

b = """문자열 주석 아님. 
그냥 문자열!"""

print(b, type(b))

# 더하기 연산 - 연결
print('💖💖💖' + '😗😗' + '🦢🦢🦢')

# 곱하기 연산
print('✌️' * 3)

# 빼기 연산 안됨 -> 오류 #TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print('❤️' - '👌')

# 문자  (문자 + 배열)
# - 인덱스를 통해 접근 가능
# - 0-based index : 0부터 시작, 길이-1
x = 'Friday'
print('x의 길이 : ', len(x)) # 길이가 6이므로, 0~5까지 인덱스를 제공
print(x[0], x[1], x[2], x[3], x[4], x[5])
#print(x[6]) #IndexError: string index out of range

# 역인덱스
print(x[-1], x[-2], x[-3], x[-4], x[-5], x[-6])

# slicing 지원
# - 문자열의 일부를 가져오는 방법
# - [sstart:stop:step]
# - start 시작하는 인덱스              - inclusive
# - end 종료 인덱스 (포함되지 않음)      - exclusive
# - step 건너뛸 개수 (기본값 1)
txt = 'hello world'
print('text의 길이 : ', len(txt))

print(txt[0:5:1])
print(txt[0:5]) # step 생략시 기본값 1처리
print(txt[:5]) # start 생략시 0번지부터 slicing
print(txt[6:11])
print(txt[6:]) # end 생략시 끝까지 slicing
print(txt[:]) #전체를 프린트함
print(txt[::2])
print(txt[::-1]) #step이 음수인 경우 뒤에서부터 가져온다.
print(txt[:-6:-1])

# 문자열 불변타입 (immutable)
# - 메모리에 할당된 값을 수정할 수 없다
# - 수정하면 새 값을 할당한다
s = 'hello'
print(id(s)) # 실제 메모리 값을 확인
s = s + 'world'
# s += 'world'
print(id(s)) # 메모리 값이 변경된다

# 멤버쉽 검사 in
# - 포함 되었는지 여부를 True/False 로 반환해 줌
txt = '안녕하세요'
print('안녕' in txt)
print('펭하' in txt)

# 포맷팅
# - 형식문자열의 일부를 다른 변수/값으로 치환
# - %
# - str.format()
# - f-string : 3.6 부터 지원
x = 10
y = 3.14
print('%d + %.2f = %d' % (x, y, x + y)) # %d - (decimal : 순서를 잘 지켜줘야함 (전통적인 방식) 돌아는가지만 f-string을 써라)
print('{} + {} = {}'.format(x, y, x + y))
print(f'{x} + {y} = {x+y}') # 가장 추천

# str api
# - 공식 문서 - python api documentation -> language reference -> str
# - https://docs.python.org/ko/3.13/library/stdtypes.html#str

# str.replace(old, new)
# - 특정 문자열을 치환해서 새 문자열을 반환
today = '2025-04-11'
today_ = today.replace('-','/')
print(today_)

# str.strip()
# - 시작/끝부분 공백 제거
some = '      하하하 ㅋㅋㅋㅋ      '
print('[',some.strip(),']')