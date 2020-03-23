import math

v = int(input("The magnitude of the velocity of the Red Bird in m/s:"))
a = int(input("The angle with respect to the horizontal of the velocity vector, in degrees:"))
d = int(input("The horizontal distance to the structure you're trying to knock down with the Red Bird, in m: "))
h = int(input('The height of the structure in m:' ))

vX = v*math.cos(a/180*math.pi)
vY = v*math.sin(a/180*math.pi)
g = 9.8
#defines some of the numbers.

t = d/vX
#t is the time that bird needs to reach the building.

tDec = vY/g
#tdec is the time that the bird fly up.

hhit = 5+vY*t-0.5*g*t**2
#hhit is the height when the bird (maybe) touches the building.

vF = math.sqrt(vX**2 + (g*(t-tDec))**2)
rad = math.atan((g*(t-tDec))/vX)
arc = rad/math.pi*180
#vF is the final velocity of the bird. arc is the angular of the speed.

print('\nthe bird is travelling at a speed of ' + str(vF) + ' meters per second.\n')
print('and the speed is at an angle of ' + str(arc) + ' degrees below the horizontal.\n')

if hhit > 0 and hhit < h:
    print("the bird reaches the building in " + str(t) + ' seconds.\n' )
    print("the bird is at a height of " + str(hhit) + " when it reaches the building.\n" )
    print("so it hits the building.\n")
elif hhit > 0 and hhit > h:
    print("\nthe bird is at a height of " + str(hhit) + " when it reaches the building.\n" )
    print("so it flies over the building.\n")
elif hhit < 0:
    print("\nthe bird stops before it reaches the building.\n" )
    print("so it won't hit the building.\n")


