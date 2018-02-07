#symotion-prefix#
#################################
# Imports                       #
#################################
import math
import turtle

###############################################
# Function that builds the structure, ground, #
# slingshot, and draws the (X,Y) locations    #
# until the projectile hit the ground or      #
# structure                                   #
###############################################
def projectile_xy(v, a, dX, dY, hs=5.0, g=9.8):
    '''
    calculate a list of (x, y) projectile motion data points
    where:
    x axis is distance (or range) in meters
    y axis is height in meters
    v is velocity of the projectile (meter/second)
    a is the angle with repsect to ground (radians)
    dX is the distance to the structure
    dY is the height of the structure
    hs is starting height with respect to ground (meters)
    g is the gravitational pull (meters/second_square)
    '''
    vX_int = v*math.cos(math.degrees(a))
    vY_int = v*math.sin(math.degrees(a))
    vX_fin = vX_int

    vY_fin = vY_int - g*t
    dX = vX_int * t
    dY = 5 + vY_int * t -0.5*g*t**2

    t = 1
    t += 1
    #get all the results
    h = 0 + vY_int * t - 0.5*g*t**2
    d = vX_int * t
    
    #Start time at 0
    t = 0.0
    #Setup the Turtle
    turt = turtle.Turtle()
    turt.color("blue", "red")   #You can change colors here
    turt.pensize(5)
    #HINT: Recommend drawing the structure first,
    #then ground and then slingshot
      
    #Draw the structure
    turt.lt(90)
    turt.fd(dY*10)
    turt.rt(90)
    turt.fd(10*10)
    turt.rt(90)
    turt.fd(dY*10)
    turt.rt(90)
    turt.fd(10*10)
    #Draw the ground
    turt.fd(dX*10)
    #Draw the slingshot
    turt.rt(90)
    turt.fd(5*10)
    #Prep for Takeoff
    turt.right(a)
    turt.color("red")
    turt.pensize(4)
    missed = False
    
    while True:
        # Calculate the height y at time t
        y = v*math.sin(math.degrees(a))*t - 0.5*g*t**2
        # Check to see if projectile has hit ground level
            # if projectile hit the ground, use the break command
            # to exit the loop
        if y == 0:
           break
        
        # Calculate the distance x at time t
        x = v*math.cos(math.degrees(a))*t
        # Check if the projectile has hit the structure
        # Hint: check for the following:
        # missed is False and x value is >= distance x and y is > 0

        if y < dY:
            break
        elif x > (dX + 10):
            missed = True

=======
        if missed == False and x >= dX and y > 0:
            if y < dY:
                break
            elif x > (dX + 10):
                missed = True


        # Move the Turtle to the (X, Y) position
        turt.goto(x,y)
        # Use the time in increments of 0.1 seconds
        t += 0.1

##############################
# Main Program               #
##############################
#Insert the code from Task 1 of the program here
import math

v = float(input("The magnitude of the velocity of the Red Bird in m/s:"))
a = float(input("The angle with respect to the horizontal of the velocity vector, in degrees:"))
d = float(input("The horizontal distance to the structure you're trying to knock down with the Red Bird, in m: "))
h = float(input('The height of the structure in m:' ))

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




# Set up the window and its attributes
wn = turtle.Screen()         
wn.bgcolor("white")

#########################################
# Following line calls the function for #
# drawing the results                   #
# Variables used for parameters:        #
# v = Input velocity                    #
# a = Gravity                           #
# d = Distance in X direction           #
# h = Height of the structure           #
#########################################
projectile_xy(v, a, d, h)

# Runs the graphics until they are closed
wn.mainloop()

