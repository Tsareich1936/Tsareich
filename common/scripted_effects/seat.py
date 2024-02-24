import math
f1 = "add_to_array = { array = seat_x_position value ="
f2 = " }\nadd_to_array = { array = seat_y_position value ="
f3 = " }\n"
with open("./seat.txt", "w") as f:
    for theta in range (0,41):
        for r in range (0,12):
            x = round(11*(r+10)*math.cos(math.pi -(theta/40)*math.pi),3)
            y = round(-11*(r+10)*math.sin((theta/40)*math.pi),3)
            f.write(f1+str(x)+f2+str(y)+f3)