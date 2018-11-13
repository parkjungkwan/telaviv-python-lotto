# ************
# -- Main
# ************
from _14_support import fib
if __name__ == "__main__": # main
    f = fib(100)
    print(f)
''' 
    __name__ 은 모든 네임 스페이스에있는 전역 변수 (파이썬에서는 global은 모듈 수준 에서 실제로 의미 함)입니다. 일반적으로 모듈의 이름입니다 ( str 형식).
'''