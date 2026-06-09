lst = [1,2,3] # 0, 1, 2 번지에 값 할당
print(lst, type(lst))

print(lst[0], lst[1], lst[2])

print('변경전 id : ',id(lst))

# 맨뒤에 요소 추가
lst.append(4)
print(lst)
print('변경후 id : ',id(lst))

lst.insert(1,1.5)
print(lst)

lst.pop(2)
print(lst)

data = '홍길동,20,서울,서초구'
data_ = data.split(',')
print(data_, type(data_))

name = data_[0]
age = data_[1]
add1 = data_[2]
add2=data_[3]
print(name,age,add1,add2)



lst = ['a', 'b', 'c']
# for 변수 in 순회객체 :
for v in lst:
    print(v)

# 인덱스 순회
for index, v in enumerate(lst):
    print(index, v)
