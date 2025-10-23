def inside_block():
    chai_type="yellow chai" #local scope;
    return chai_type;
outside_block=inside_block(); #global scope
print(outside_block);