essential_species={"cardomon","ginger","cinnamon"};
optional_species={"cloves","ginger","black pepper"};

all_species=essential_species | optional_species;

print(all_species);

common_species=essential_species & optional_species;
print(common_species);

#only the essential species
only_essential_species=essential_species - common_species;
print(only_essential_species);

print(f"To find whether it is correct or wrong = {True if "cinnamon" in essential_species else False}")