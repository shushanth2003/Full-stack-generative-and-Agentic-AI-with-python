cup_size=input("choose the cup size (small,large,medium) : ").lower();
if cup_size=="small":
    print(f"cup size is {cup_size} price tag Rs.10");
elif(cup_size=="medium"):
    print(f"cup size is {cup_size} price tag Rs.20");
elif(cup_size=="large"):
    print(f"cup size is {cup_size} price tag Rs.30");
else:
    print("Unknown cup size");