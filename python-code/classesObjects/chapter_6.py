class A:
    label="Labeling class : A";
class B(A):
    label="Labeling class : B";
class C(A):
    label="Labeling class : C";
class D(B,C):
    label="Labeling class : D";
cup=D();
print(cup.label);
print(D.__mro__);