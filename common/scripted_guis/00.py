with open("common/scripted_guis/00.txt" , "w" ) as f:
    f.write("triggers = {\n")
    for i in range (0,11):
        f.write( "\tbar_L_{}_viisible = ".format(i*10) + "{ check_variable = { SRI_bop_L_var = "+ "{:3}".format(float(i*0.1)) +" } }\n" )
    for i in range (0,11):
        f.write( "\tbar_R_{}_viisible = ".format(i*10) + "{ check_variable = { SRI_bop_R_var = "+ "{:3}".format(float(i*0.1)) +" } }\n" )
    f.write("}")