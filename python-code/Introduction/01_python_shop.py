class Chai:
    def __init__(self,sweetness,milklevel):
        self.sweetness=sweetness
        self.milklevel=milklevel
    def sip(self):
        print("Add a coffee")
    def add_a_sugar(self,amount):
        print("Add a Sugar",amount)

my_chai=Chai("medium",4)
my_chai.add_a_sugar(5);