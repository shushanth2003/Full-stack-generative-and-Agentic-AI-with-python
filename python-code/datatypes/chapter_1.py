species_list=set();

print(f"Initial Species List ID : {id(species_list)}");

species_list.add(1);
species_list.add(2);
species_list.add(1);
print(f"After Initial Species List ID : {id(species_list)}")

print(f"species List ${species_list}");