# set
# - 중복값을 허용하지 않는다.
# - set api 에는 집합 관련 연산을 지원함 (합집합, 교집합, 차집합, 여집합)
# - 시퀀스 형이 아님
# - 중복 제거 목적으로 사용함
# - 순서를 저장하지 않음

st = {2,3,2,3,1,2,3,4,3,2}
print(st,type(st))

# list 중복 제거
lst = [2,3,2,3,1,2,3,4,3,2]
st2 = set(lst)
print(st2,type(st2))
lst2 = list(st2)
print(lst2,type(lst2))

# tuple 중복 제거
tpl = ('a', 'b', 'c', 'c', 'x', 'a')
print(set(tpl))

# 요소 추가
my_nums = {20,30,40}
my_nums.add(50)
print(my_nums)

# 요소 수정
my_nums.remove(50) # 삭제하고자 하는 값을 전달
# my_nums.remove(100) # KeyError: 100 존재하지 않는 값을 삭제시 오류
my_nums.discard(100) # 값이 없어도 오류나지 않음
print(my_nums)

# 반복 순회 가능 (iterable 객체이기 때문에)
for value in my_nums:
    print(value)

# 모든 요소 제거
my_nums.clear()
print(my_nums)

# 집합 연산
m = {1,2,3,4,5,6,7,8,9,10}
n = {2,4,6,8,10,12,14,16,18,20}

print('합집합 : ', m.union(n))
print('교집합 : ', m.intersection(n))
print('차집합 : ', m.difference(n))
print('대칭 차집합 : ', m.symmetric_difference(n)) # 합집합에서 - 교집합



