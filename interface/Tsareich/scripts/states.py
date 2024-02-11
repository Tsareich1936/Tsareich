states = [
    "arkansas",
    "iowa",
    "idaho",
    "alabama",
    "arizona",
    "illinois",
    "indiana",
    "wisconsin",
    "west Virginia",
    "oklahoma",
    "ohio",
    "oregon",
    "california",
    "kansas",
    "kentucky",
    "connecticut",
    "colorado",
    "south Carolin",
    "south Dakotaa",
    "georgia",
    "texas",
    "tennessee",
    "delaware",
    "new Jersey	",
    "new Hampshire",
    "new Mexico",
    "new York",
    "nevada",
    "nebraska",
    "north Carolina",
    "north Dakota",
    "virginia",
    "vermont",
    "vlorida",
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
    "rhode Island",
    "wyoming",
    "washington"
]
ideologies = [
    "com",
    "con",
    "lib"
]
first = "spriteType = {"
second = "\n\tname = GFX_TR_USA_"
third = "\n\ttextureFile = \"gfx/interface/UI/usa_election/states/"
forth = ".dds\"\n\t}\n"
with open("interface/Tsareich/scripts/states.txt","w")as f:
    for i in range(0,len(states)):
        for j in range(0,len(ideologies)):
            f.write(first+second+states[i]+"_"+ideologies[j]+third+states[i]+"_"+ideologies[j]+forth)