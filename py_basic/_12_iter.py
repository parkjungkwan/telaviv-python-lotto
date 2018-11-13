# ************
# -- 이터
# ************
import sys
def fibonacci(n):
    a, b, counter = 0,1,0
    while True:
       if(counter > n):
           return
       yield a
       a, b = b, a + b
       counter += 1
f = fibonacci(5)
while True:
    try:
        print(next(f), end=' ') # 0 1 1 2 3 5
    except StopIteration:
        sys.exit()
