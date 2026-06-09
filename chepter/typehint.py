# type_hint
# - 파이썬은 동적 타이핑을 지원한다. - 다이나믹 타이핑
# - 변수에는 자료형이 없고, 대입되는 리터럴에 따라 자료형이 결정된다.

x = '안녕'
x = 123
print(type(x))
# 이렇게 될경우 x의 자료형은 잠시 str 였다가 int 로 바뀌게 됨

def act(x):
    '''
    x 를 가지고 문자열로 바꿔 xx 하는 함수
    :param x:
    :return:
    '''
    print(x)

# 위처럼 하면 난해해 지니까 진작에 문제점을 제거해주자
# 요즘 이렇게 유연한 언어를 이런식으로 엄격하게 쓰려고 하는 경향이 있음
def act(x = int):
    '''
    x 를 가지고 문자열로 바꿔 xx 하는 함수
    :param x:
    :return:
    '''
    print(x)

# - 정적 코드 작성시에 타입 검사를 수행하는 type_hint 를 지원
# - 이건 이름에서도 알수있듯 그냥 hint 고 실제 실행시에는 무시된다

# type hint 지정 해보자
greeting : str = 'hello'
greeting = 123
print(greeting)

# 이것처럼 실제 실행할땐 오류가 안나는데 노란 밑줄이 나타나며 경고를 준다

n:int = 123
f:float = 3.14
score: int = 90
has_coupon: bool = True

# 이렇게 list,tuple,dict,set을 지정해줄수도 있고 그 안에 자료형도 정해줄수있다
nums: list[int] = [1,2,3]
users: tuple[int, str, str] = (123,'홍길동','honggd')
# 자료형이 여러가지일경우에는 |을 사용해서 또는 을 표시해줌
# 아니면 object를 써서 모든것 가능 이라고 표시 할 수 있다
info: dict[str, str|int] = {'name': '심사임당', 'age': 42}
chars: set[str] = {'a', 'b', 'c'}
# 이렇게 추가적으로 작성해보자 나의 의도가 더 명확해진다

# 상수 표현
# - 파이썬 관례상 대문자로 작성된 변수는 상수로 취급 !!!
# - 상수란 ? 한번 값이 지정되면 절대 바뀌어서는 안되는 변수이다
# - 파이썬 자체에선 이러한 기능이 없음
# - 그래서 바꿔도 문제 없이 실행은 되지만 경고를 표시해줌
# MAX_COUNT = 10
# MAX_COUNT = 5 # 제대입하면 안됨

from typing import Final
MAX_COUNT: Final[int] = 10
MAX_COUNT = 5   # 이것도 오류가 나진 않지만 경고를 줌
print(MAX_COUNT)

