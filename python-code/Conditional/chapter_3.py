device_status=input("check whether the status is active or inactive : " );
temperature=int(input("Enter the Temperature : "));
if(device_status=="active"):
    if(temperature>35):
        print("Warn: High Temperature");
    else:
        print("Moderate: Temperature normal");
else:
    print("device is inactive");