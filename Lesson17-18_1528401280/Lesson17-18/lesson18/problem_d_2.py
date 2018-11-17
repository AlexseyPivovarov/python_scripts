class A:
    pass
class B(A):
    pass
class E(A):
    pass
class D(E,A):
    pass
class M(B,D):
    pass
print(M.__mro__)
