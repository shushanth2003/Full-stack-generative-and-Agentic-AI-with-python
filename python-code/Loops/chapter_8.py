staff=[("Amit",16),("hiteesh",17),("prakesh",56)];

#checking the eligible to manage the team
for name,age in staff:
    if(age>=18):
        print(f"{name} is eligible to manage the team");
        break;
else:
    print("No one eligible to manage the team");
