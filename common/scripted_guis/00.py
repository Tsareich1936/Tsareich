with open("common/scripted_guis/00.txt" , "w" ) as f:
    f.write("triggers = {\n")
    for i in range (0,11):
        f.write( "\tbar_L_{}_viisible = ".format(i*10) + "{ check_variable = { SRI_bop_L_var = "+ "{}".format(i*10) +" } }\n" )
    for i in range (0,11):
        f.write( "\tbar_R_{}_viisible = ".format(i*10) + "{ check_variable = { SRI_bop_R_var = "+ "{}".format(i*10) +" } }\n" )
    f.write("}")