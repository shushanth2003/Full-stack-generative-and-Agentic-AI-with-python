class Chai:
    def __init__(self,type_,strength):
        self.type=type_;
        self.strength=strength;
class GingerChai(Chai):
    def __init__(self,type_,strength,species_Level):
        super().__init__(type_,strength);
        self.species_Level=species_Level;
gingerchai=GingerChai(1,"super",100);
print(gingerchai.type);
print(gingerchai.strength);
print(gingerchai.species_Level);