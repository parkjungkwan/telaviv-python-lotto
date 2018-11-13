class A(object):
    def dothis(self):
        print('Doing this in A')
class B(A):
    pass
class C(object):
    def dothis(self):
        print('Doing this in C')
class D(B,C):
    pass




