class OrderChai:
    def __init__(self,size,type_):
        self.size=size;
        self.type_=type_;
    def selected_order(self):
        print(f"{self.size} is size of type {self.type_}");
selected_chai=OrderChai(1,"Stringify");
selected_chai.selected_order();
