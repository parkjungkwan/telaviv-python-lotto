# ************
# -- 데이터타입 변환
# ************
# to int
a = 3.3
b = 2.0
c = a + b
print(c)
print(int(c))

# to str
price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
print(total)
# del(str)
t = str(total)
print("합계 : "+t+" $")
# TypeError: can only concatenate str (not "int") to str

# to list
a_tuple = (1,2,3,4,5,6,7,8,9,10)
b_list = [1,2,3,4,5]

print(tuple(b_list))
print(list(a_tuple))
sample_cake = 'cake'
# del(tuple)
print(tuple(sample_cake))
del(list)
sample_list = list(sample_cake)
sample_list.append('s')
print(sample_list)