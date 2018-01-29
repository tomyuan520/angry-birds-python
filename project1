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
    #Start time at 0
    t = 0.0
    
    #Setup the Turtle
    turt = turtle.Turtle()
    turt.color("blue", "red")   #You can change colors here
    turt.pensize(5)
    #HINT: Recommend drawing the structure first,
    #then ground and then slingshot
    
    #Draw the structure
    
    #Draw the ground

    #Draw the slingshot

    #Prep for Takeoff
    turt.right(a)
    turt.color("red")
    turt.pensize(4)
    missed = False
    
    while True:
        # Calculate the height y at time t
        #DELETE ME AND PUT EQUATION TO SOLVE FOR Y
        
        # Check to see if projectile has hit ground level
        #DELETE ME AND PUT IN THE IF STATEMENT
            # if projectile hit the ground, use the break command
            # to exit the loop
        
        # Calculate the distance x at time t
        #DELETE ME AND PUT EQUATION TO SOLVE FOR X
        
        # Check if the projectile has hit the structure
        # Hint: check for the following:
        # missed is False and x value is >= distance x and y is > 0
        #DELETE ME AND PUT IN THE IF STATEMENT
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

