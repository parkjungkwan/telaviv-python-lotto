# ************
# -- 반복문
# ************
# for loop
for i in 'Python':
    print("현재 회전 글자 :", i)
print()



for i in [11,33,15,55,20,6,7,44]:
    if i % 2 == 0:
        print(str(i)+'는 짝수 ') # i 는 홀수
    else:
        print(str(i)+'는 홀수 ')
    
print()

for i in [11,33,15,55,7]:
    if i % 2 == 0:
        print('짝수 리스트') 
        break
    else:
        print('홀수 리스트') 
    
print()