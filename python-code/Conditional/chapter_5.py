coach_available=input("Enter the availablity seats (sleeper,ac,general,luxary) : ").lower();
match(coach_available):
    case "luxary":
        print("seat available, it fully comfortable and meals will be provided");
    case "sleeper":
        print("seat available, but meals and ac will not provided");
    case "ac":
        print("seat available,ac will be provided but meals will not provided");
    case "general":
        print("seat available,sleeper,ac,food will not provided");
    case _:
        print("Invalid seat type");