chai=[1,2,4];
print("Before Arguments Methods : ",chai);
def edit_chai(cup):
    cup[2]=3;
edit_chai(chai);
print("After Arguments Methods : ",chai);

def sweet_chai(sugar,milk,level):
    print(sugar);
    print(milk);
    print(level);
sweet_chai("one spoon","half litres","low"); #positional level
sweet_chai(sugar="two spoon",milk="half litres",level="high"); #keywords

def integrediants(*integredents,**extras):
    print(f"Integredients Level of The Information : {integredents}");
    print(f"Extra Level of the Information : {extras}");
integrediants("cinnamon","sugar",addUp="yellow",level="high");


def make_chai(chai=None):
    if(chai is None):
        chai=[];
    chai.append("sugar");
    print(chai);
make_chai();
make_chai();