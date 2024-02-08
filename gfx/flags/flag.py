import shutil
with open("common/country_tags/00_countries.txt","r")as f:
    lines = f.readlines()
    tags = [line.split(' ')[0] for line in lines]
    for i in range(0,279):
        if tags[i] == "":
            break
        elif tags[i] == "\n":
            break
        else:
            filename = "{}.tga".format(tags[i])
            shutil.copy("gfx/FLAG.tga","gfx/a/{}".format(filename))