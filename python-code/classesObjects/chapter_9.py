class Inspect_tea:
    def __init__(self,age):
        self.age=age;
    @property
    def tea_age(self):
        return self.age+2;
    @tea_age.setter
    def tea_age(self,age):
        if(1<=age<=5):
            print(self.age);
        else:
            raise ValueError("The leaf age must be between 1 and 5 years");
res=Inspect_tea(3);
print(res.tea_age);