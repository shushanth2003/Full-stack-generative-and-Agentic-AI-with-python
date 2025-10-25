def server_chai(chai_type):
    try:
        print(f"checking favor chai known or unknown {chai_type}");
        if(chai_type=="unknown"):
            raise ValueError("chai type is unknown")
    except ValueError as e:
        print("Error : ",e);
    else:
        print(f"It's show error");
    finally:
        print("If it is ok then ok");
server_chai("masala");
print("")
server_chai("unknow4n");    