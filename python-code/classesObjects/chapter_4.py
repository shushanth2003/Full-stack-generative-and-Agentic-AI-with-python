class Basicchai:
    def __init__(self,type_):
        self.type=type_;
    def prepare(self):
        print(f"Chai is Prepared in different type {self.type}");

class Masalachai(Basicchai):
    def adding_species(self):
        print("cinnomen, yellow masala, ginger");

class Chaishop:
    chai_basic=Basicchai;
    def __init__(self):
        self.chai=self.chai_basic("Regular");
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop");
        self.chai.prepare();


class Fancyshop(Chaishop):
    chai_cls=Masalachai;

shop=Chaishop();
fancy=Fancyshop();
shop.serve();
fancy.serve();
