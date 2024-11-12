import math

theta=eval(input("enter theta in degree(between -180 to 180 degree):"))
length=eval(input("enter robot arm length:"))

theta_rad = math.radians(theta)

a=math.cos(theta_rad)
b=math.sin(theta_rad)

x=length*a
y=length*b

print("theta radian is:",theta_rad)
print("length is:",length)
print("coordinate x and y is:",(x , y))

if theta==0 and length>0:
    print("robot arm is horizontal right")
    
elif theta==90 and length>0:
    print("robot arm is vertical upwards")
    
elif theta==-90 and length>0:
   print("robot arm is vertical downward")
   
elif x>0 and y>0:
    print("quadrant 1")
    
elif x<0 and y>0:
    print("quadrant 2")
    
elif x<0 and y<0:
    print("quadrant 3")
    
else:
    print("quadrant 4")
