#Frisbee physics, based off of MIT paper:
#  web.mit.ed/womens-lt/www/smite/frisbee_physics.pdf

import math

#xpos, ypos, xvel, yvel

#gravity
g = -9.8
#mass, duh
m = 0.175
#density of air in kg/m3
RHO = 1.23
#area of frisbee
AREA = 0.0558
#life coefficient at alpha = 0
CLO = 0.1
#lift coefficient dependant on alpha
CLA = 1.4
#drag coefficient at aplha = 0
CDO = 0.08
# drag dependant on alpha
CDA = 2.72
# I dunno what this is for, but it's used later
ALPHA0 = -4

#velocity
vel = 14
# angle of attack from horizontal and vector of frisbee
alpha = 7.5


def simulate(y0, alpha, vel, deltaT):
    #call by: initial y height, default 0, alpha, deltaT (0.001), and vel (default 14)
    # this is the life coefficient calclated
    cl = CLO + (CLA * alpha * math.pi / 180)
    cd = CDO + (CDA * math.pow((alpha - ALPHA0) * (math.pi / 180), 2))

    x = 0
    y = y0
    # xcomponent of velocity
    #calculate via cos of alpha times velocity
    vx = vel * math.cos(alpha * (math.pi / 180))
    # ycomponent of velocity
    #calculate via sin of alpha times velocity
    vy = vel * math.sin(alpha * (math.pi / 180))

    #print x, y, vx, vy, vel
    try:

        k = 0

        while (y >= 0):
            # calculate new deltavy
            deltavy = (RHO * math.pow(vx, 2) * (AREA * cl / 2 / m) + g) * deltaT
            deltavx = -1 * RHO * math.pow(vx, 2) * AREA * cd * deltaT

            #recalculate positions and velocities
            vx += deltavx
            vy += deltavy
            x += vx * deltaT
            y += vy * deltaT

            k = k + 1

            #log things here if you want to do so every single calculation
            #end logging
            if (k % 10 == 0):
                # print "xpos: ", x
                # print "ypos: ", y
                # print "\n"
                if ((y > 2.644 and y < 2.9488) and (vy > 0)):
                #if frisbee is at height of 3 pt goal
                    print y, "  - goal height "
                    print vel, "  - original speed"
                    print vx, "  - current horixontal speed"
                    print vy, "  - current vert speed "
                    print "\n"
                #every 10 calculations, log data
                #log data HERE

            # every time through the while loop, increment k

    except Exception, e:
        print "Exception."
        raise e

    return x, y

#begin main program
#simulate(y0, alpha, vel, 0.001)
#simulate(initial height in meters, alpha, velocity along flight vector, time detail)
for v in range(8, 11):
    xpos, ypos = simulate(1, 42, v, 0.001)
