import math
f1 = "add_to_array = { array = GER_seat_x_position value ="
f2 = " }\nadd_to_array = { array = GER_seat_y_position value ="
f3 = " }\n"
with open("common/scripted_effects/seat.txt", "w") as f:
    for theta in range (0,41):
        for r in range (0,12):
           #z = round"切り捨て"("１アイコンの大きさ"*(r"現在の内側からの距離"+"内側の空白")*math.sin"任意の三角関数"(角度[rad]),3"小数点以下の桁")
            x = round(11*(r+9)*math.cos(math.pi -(theta/40)*math.pi),3)
            y = round(-11*(r+9)*math.sin((theta/40)*math.pi),3)
            f.write(f1+str(x)+f2+str(y)+f3)