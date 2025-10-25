def make_chai_notes():
    yield "sugar";
    yield "milk";
    yield "grapes";

res=make_chai_notes();
for reses in res:
    print(reses);

def init_chai_notes():
    yield "sugarcane";
    yield "babycone";
    yield "vegetables";
result=init_chai_notes();
print(next(result));
print(next(result));
print(next(result));