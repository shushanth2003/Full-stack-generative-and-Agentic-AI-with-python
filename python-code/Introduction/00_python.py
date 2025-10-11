def preparing_chai():
    if not kettle_in_water:
        pour_water_in_kettle()
    if not plugging_kettle:
        plugging_in_kettle()
    boil_the_water()
    add_integrients("sugar","tea powder","milk")
preparing_chai()