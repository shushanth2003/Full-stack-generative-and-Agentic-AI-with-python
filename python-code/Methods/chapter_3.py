def calculate_bills(cups,price_per_cups):
    total=0;
    if(cups=="small"):
        price_per_cups=10;
    elif(cup=="medium"):
        price_per_cups=20;
    elif(cup=="large"):
        price_per_cups=30;
    else:
        price_per_cups=0;
    total+=price_per_cups;
    return total;
calculate_bills_total=calculate_bills(input("Enter the Size of cups"),0);
print(calculate_bills_total);