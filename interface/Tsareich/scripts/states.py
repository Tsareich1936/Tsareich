states = [
    "arkansas",
    "iowa",
    "idaho",
    "alabama",
    "arizona",
    "illinois",
    "indiana",
    "wisconsin",
    "west_virginia",
    "oklahoma",
    "ohio",
    "oregon",
    "california",
    "kansas",
    "kentucky",
    "connecticut",
    "colorado",
    "south_carolina",
    "south_dakota",
    "georgia",
    "texas",
    "tennessee",
    "delaware",
    "new_jersey",
    "new_hampshire",
    "new_mexico",
    "new_york",
    "nevada",
    "nebraska",
    "north_carolina",
    "north_dakota",
    "virginia",
    "vermont",
    "florida",
    "pennsylvania",
    "massachusetts",
    "michigan",
    "mississippi",
    "missouri",
    "minnesota",
    "maine",
    "maryland",
    "montana",
    "utah",
    "louisiana",
    "rhode_island",
    "wyoming",
    "washington"
]
ideologies = [
    "com",
    "con",
    "lib"
]
ideologies1 = [
    "1",
    "2",
    "3"
]
first = "spriteType = {"
second = "\n\tname = GFX_TR_USA_"
third = "\n\ttextureFile = \"gfx/interface/UI/usa_election/states/"
forth = ".dds\"\n\t}\n"
# with open("interface/Tsareich/scripts/states.txt","w")as f:
#     for i in range(0,len(states)):
#         for j in range(0,len(ideologies)):
#             f.write(first+second+states[i]+"_"+ideologies[j]+third+states[i]+"_"+ideologies[j]+forth)
# fg = "iconType = {"
# sg = "\n\tname = TR_USA_"
# tg = "_button\n\tquadTextureSprite = GFX_TR_USA_"
# fog = "\n\tpdx_tooltip = TR_USA_"
# fig = "_tt\n\tscale = 0.75\n\talwaystransparent = yes\n}\n"
# with open("interface/Tsareich/scripts/gui.txt","w")as f:
#     for i in range(0,len(states)):
#         for j in range(0,len(ideologies)):
            # f.write(fg+sg+states[i]+"_"+ideologies[j]+tg+states[i]+"_"+ideologies[j]+fog+states[i]+"_"+ideologies[j]+fig)
# fg = "TR_USA_"
# sg = "_button_visible = {"
# tg = "\n\tcheck_variable = {\n\t\tROOT.TR_USA_"
# fog = "\n\t}\n}\n"
# with open("interface/Tsareich/scripts/gui_tr.txt","w")as f:
#     for i in range(0,len(states)):
#         for j in range(0,len(ideologies)):
#             f.write(fg+states[i]+"_"+ideologies[j]+sg+tg+states[i]+"_var = "+ideologies1[j]+fog)
fg = "set_variable = {"
sg = " ROOT.TR_USA_"
tg = "_var = "
fog = " }\n"
with open("interface/Tsareich/scripts/var_set.txt","w")as f:
    for i in range(0,len(states)):
        f.write(fg+sg+states[i]+tg+"3"+fog)