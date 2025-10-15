names=[];
for initial in range(0,3):
    name=input("Enter the name");
    names.append(name);
for queue in range(0,len(names)):
    print(f"order ready for {names[queue]}");