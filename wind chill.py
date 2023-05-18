import math
v=float(input("enter the wind speed in kilometers per hour:"))
t=float(input("enter the temperature in celsius:"))
wci=13.2+0.6215*t-11.37*v*0.16+0.3965*t*v*0.16
print("the wind chill index:",int(round(wci,0)))
