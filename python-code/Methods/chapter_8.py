#impure function
def make_chai():
    return "chai is ready";
print(make_chai());

#recursive function;
def number(n):
    if(n==0):
        print("Number is returned into 0");
        return;
    print(n);
    number(n-1);
number(3);

#lambda function
pour_list=["banana","manago","banana","orange"];
filter_pour_duplicate_list=list(filter(lambda chai:chai!="banana",pour_list));
print(filter_pour_duplicate_list);
