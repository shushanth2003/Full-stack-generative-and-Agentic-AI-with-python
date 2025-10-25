class Makecount:
    size=1;
    def describe(self): #self arguments
        self.size=10;
        return self.size;
make_count=Makecount();
#describe the variable and class
print(f"Initializing the count : {make_count.describe()}");
        