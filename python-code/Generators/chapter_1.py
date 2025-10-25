def infinite_data():
    count=0;
    while True:
        yield f"Refill {count}";
        count+=1;

data_passed=infinite_data();
for i in range(3):
    print(next(data_passed));