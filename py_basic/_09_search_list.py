# ************
# -- 리스트 검색
# ************
no = int(input("숫자입력 :"))
numbers = [11,33,55,39,75,32,21,23,41,13]
for i in numbers:
    if i == no:
        print('리스트에 있는 숫자')
        break
else:
    print('해당숫자가 리스트에 없음')
