# ************
# -- 데이터타입 6가지 
# ************
''' 
    Number : int, float, complex
    String : str
    List 
    Tuple
    Dictionary
    Set
'''
# String

hello = "Hello Python !!"
print(hello) # 
print(hello[0]) 
print(hello[2:5])
print(hello[2:])
print(hello * 2)
print(hello + " TEST ")

# List
list = ['abcd', 786, 2.23, 'john', 70.2]
slist = [123,'john']

print(list) # ['abcd', 786, 2.23, 'john', 70.2]
print(list[0]) # abcd
print(list[1:3]) # [786, 2.23]
print(list[2]) # 2.23
print(slist * 2) # [123, 'john', 123, 'john']
print(list + slist) # ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']

# Tuple
''' Tuple can be thought of as read-only list '''
tuple = ('abcd', 786, 2.23, 'john', 70.2)
stuple = (123, 'john')

print(tuple)
print(tuple + stuple)

temp = list[2]
print(temp)
list[2] = 1000.7
list[2]
temp = tuple[2]
print(temp)
tuple[2] = 1000.7
# TypeError: 'tuple' object does not support item assignment

# dictonary
''' dictionaries are kind of hash-table type '''
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

sdict = {'name':'john', 'code':6783, 'dept':'sales'}
print(dict['one'])
print(dict[2])
print(sdict)
print(sdict.keys())
print(sdict.values())