f1 = "set_temp_variable = {\n"
f2 = "\ttemp_"
f3 = "\n}\n"
f4 = "add_to_temp_variable = {\n"
f5 = "set_variable = {\n\t"
f6 = "divide_variable = {\n\t"
f7 = "subtract_from_variable = {\n\t"
f8 = "multiply_variable = {\n\t"
f9 = "add_to_variable = {\n\t"
armies = [
    ["infantry","1"],
    ["artillery","1.5"],
    ["cavalry","1.2"],
    ["motorized","1.5"],
    ["light_armor","2"],
    ["medium_armor","3"]
]
with open("common/scripted_effects/army","w") as f:
    for i in armies:
        f.write(f5+i[0]+"_n = num_battalions_with_type@"+i[0]+f3)
    for i in armies:
        f.write(f1+f2+i[0]+"_a = num_equipment_in_armies_k@"+i[0]+f3)
        f.write(f1+f2+i[0]+"_t = num_target_equipment_in_armies_k@"+i[0]+f3)
        f.write(f5+"suff_"+i[0]+" = temp_"+i[0]+"_a"+f3)
        f.write(f6+"suff_"+i[0]+" = temp_"+i[0]+"_t"+f3)
    f.write(f5+"other = num_battalions"+f3)
    for i in armies:
        f.write(f7+"other = "+i[0]+"_n"+f3)
    f.write(f5+"armies_cost = 0"+f3)
    for i in armies:
        f.write(f5+i[0]+"_cost = "+i[0]+"_n"+f3)
        f.write(f8+i[0]+"_cost = suff_"+i[0]+f3)
        f.write(f8+i[0]+"_cost = "+i[1]+f3)
    f.write(f5+"other_cost = other_n"+f3)
    # f.write(f8+"other_cost = suff_other"+f3)
    f.write(f8+"other_cost = 1"+f3)

    f.write(f9+"armies_cost = other_cost"+f3)
    for i in armies:
        f.write(f9+"armies_cost = "+i[0]+"_cost"+f3)
    
    f.write(f5+"war_ex = 0.1"+f3)
    f.write(f9+"war_ex = EV_war_expenses_var"+f3)
    f.write(f8+"armies_cost = war_ex"+f3)