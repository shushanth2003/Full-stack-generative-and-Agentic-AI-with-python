class outofintegredients(Exception):
    pass;
def add_integridents(sugar,milk):
    if(sugar==0 and milk==0):
        raise outofintegredients("out of stock");
    else:
        print("It's avaiable");
add_integridents(0,0);