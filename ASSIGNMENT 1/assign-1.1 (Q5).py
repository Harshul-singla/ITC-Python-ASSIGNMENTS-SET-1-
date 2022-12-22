import math 
a=0 
#c = round(math.sin(a),4)

while a <= 345:
    b = a * (math.pi/180)
    print ( str(a) + " --- " + str(round(math.sin(b),4)) + " " + str(round(math.cos(b),4)))
    
    a +=15
            