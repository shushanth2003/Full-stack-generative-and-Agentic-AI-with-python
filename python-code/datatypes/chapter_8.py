extra_species=dict(type="Masala cafe",size=2,sugar="Medium level");
print(extra_species);

chai_recipe={"cardomon":"crushed","ginger":"sliced"};
print(f"Cardomon reacts {chai_recipe["cardomon"]}");

extra_chai_recipe={"mango":"sweeted","lemon":"citric"};
added_up_chai_recipe=chai_recipe.update(extra_chai_recipe);
print("Adding the extra reci")