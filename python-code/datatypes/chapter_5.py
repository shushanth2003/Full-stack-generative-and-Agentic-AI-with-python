integridents=["water","milk","black tea"];
integridents.append("sugar");
print(integridents);

#remove the string
integridents.remove("water");
print(integridents);

spices_options=["ginger","cardomen"];
chai_integridents=["water","milk"];

spices_options.extend(chai_integridents);
print(spices_options);

spices_options.insert(2,"salt");
print(spices_options);

delete_spices_options=spices_options.pop();
print(delete_spices_options);
spices_options.reverse();
print(spices_options);
spices_options.sort();
print(spices_options);

# maximum array
maximum=[1,2,3,4];
print(max(maximum))