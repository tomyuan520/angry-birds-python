import math

v = int(input("The magnitude of the velocity of the Red Bird in m/s:"))
a = int(input("The angle with respect to the horizontal of the velocity vector, in degrees:"))
d = int(input("The horizontal distance to the structure you're trying to knock down with the Red Bird, in m: "))
h = int(input('The height of the structure in m:' ))

t = d/(v*math.cos(a/180*math.pi))
#t is the time that bird needs to reach the building.

tdec = (v*math.sin(a/180*math.pi))/9.8
#tdec is the time that the bird fly up.

hhit = 5+(v*math.sin(a/180*math.pi))*t-0.5*9.8*t*t
#hhit is the height when the bird (maybe) touches the building.



if hhit > 0 and hhit < h:
    print("\nthe bird reaches the building in " + str(t) + ' seconds.\n' )
    
    print("the bird is at a height of " + str(hhit) + " when it reaches the building.\n" )
    
    print("so it hits the building")
elif hhit > 0 and hhit > h:
    
    print("\nthe bird is at a height of " + str(hhit) + " when it reaches the building.\n" )
    
    print("so it flies over the building.")
elif hhit < 0:
    
    print("\nthe bird stops before it reaches the building.\n" )
    
    print("so it won't hit the building.")


