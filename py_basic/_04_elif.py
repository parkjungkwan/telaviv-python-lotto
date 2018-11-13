# ************
# -- 분기문
# ************
# elif
# if else
amount = int(input("총액 입금"))
if amount < 1000:
    discount = amount * 0.05
    print("5% 할인 금액 ",discount)
elif amount < 5000 :
    discount = amount * 0.1
    print("10% 할인 금액 ",discount)
else:
    discount = amount * 0.15
    print("15% 할인 금액 ",discount)
print("실 지급액 ", amount - discount)
