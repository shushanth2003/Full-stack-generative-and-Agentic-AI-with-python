remainder=50;
if(available:=remainder%10==0):
    print(f"Not Divisible! remainder avaiable {available}");

available_size=["large","medium","small"];
if(size:=input("Enter the Available Size : ") in available_size):
    print(f"Cup Size {size} is available") ;
else:
    print("Hence It's not available");

