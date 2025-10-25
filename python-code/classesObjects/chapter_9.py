class BankAmount:
    def __init__(self,balance):
        self._balance=balance;
    @property
    def balance(self):
        return self._balance;
    @balance.setter
    def balance(self,amount):
        if(amount<0):
            raise ValueError("Bank Account remains negative balance make sure it encourage");
        self._balance=amount;
bankamount=BankAmount(5000);
print("Getting Bank Balance",bankamount.balance);
# res=BankAmount.balance(1000);
# print(res);
BankAmount.balance=200;
print("After Bank Balance",bankamount.balance);

class Employee:
    def __init__(self,salary):
        self.salary=salary;
    @property
    def salary_package(self):
        return self.salary;
    @salary_package.setter
    def salary_package(self,amount):
        if(amount>=10000):
            self.salary=amount;
        else:
            raise ValueError("less percentage of salary");
e=Employee(10000);
print("Average salary : ",e.salary);
e.salary_package=20000;
print("Average salary : ",e.salary);

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius;
    @property
    def fahrenheit(self):
        fahrenheit=(self.celsius*9/5)+32;
        return fahrenheit;
    @fahrenheit.setter
    def fahrenheit(self,tem):
        self.celsius=tem;
t=Temperature(40);
print(f"Before fahrenheit {t.fahrenheit}");
t.fahrenheit=10;
print(f"After fahrenheit {t.fahrenheit}")

        