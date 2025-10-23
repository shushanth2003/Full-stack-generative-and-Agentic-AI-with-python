flavor=["Ginger","out of stock","lemon","discontinued","tulsi"];

for flavors in flavor:
    if(flavors=="out of stock"):
        continue;
    if(flavors=="discontinued"):
        break;
    print("favour is discontinued");
print("favor is out of stock");
