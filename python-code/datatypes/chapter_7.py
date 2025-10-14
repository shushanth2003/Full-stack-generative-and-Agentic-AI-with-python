'''

Intermediate Level

Create a list of 5 numbers and find the sum and average.

Given a list [1,2,3,2,1,4,5,4], remove duplicates using a set.

Create a tuple (10, 20, 30) and convert it into a list.

Given a dictionary {"name":"Alice","age":25,"city":"Paris"}, print only the keys.

Add a new key-value pair "country": "France" to the same dictionary.
'''

#Create a list of 5 numbers and find the sum and average.
num=[1,2,3,4,5];
res=int(sum(num));
print(f"Total Number of Sum : {res}");
print(f"Total Number of Average : {res/2}");

#Given a list [1,2,3,2,1,4,5,4], remove duplicates using a set.
nums=[1,2,3,2,1,4,5,4];
result_set=set();
for i in range(0,len(nums)):
    result_set.add(nums[i]);
print(result_set);

#Create a tuple (10, 20, 30) and convert it into a list.
nums_tuple=(10,20,30);
list_update=list(nums_tuple);
print(list_update);