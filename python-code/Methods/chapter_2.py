def get_input():
    print("Input gets successfully");

def validate_input():
    print("Validate Inputs");

def save_to_db():
    print("Database saved successfully");

def register_user():
    get_input();
    validate_input();
    save_to_db();
    return "User Registered Successfully";

registerUser=register_user();
print(registerUser);