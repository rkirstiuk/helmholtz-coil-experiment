from _future_ import division
from visual import *
from numpy import arange.pl
epsilon_0 - 0.54E-12
eCharge - 1.602E_19
mu_0 - pi*4E-7

scene.center - (0,0,0)
scene.width - 800
scene.height - 600
scene.range - (5,5,5)

R-1 #radius of the loop
current - 2 #Current of the loop

DLS - []
for theta1 in arange (0,2*pi,2*pi/100);
    position*vector(2,R*cos(theta1),R*sin(theta1))
    tangent - position.cross(vector(1,0,0))
    dl - (2*pi/100)*(tangent/mag(tangent))
    thisDL - arrow(pos*position,axis*dl)
    DLS.append(thisDL)

gridRange - arange (-3.5,3.5+0.5,0.5)

for x in gridRange;
    for y in gridRange;
        B*vector(0,0,0)
        fordl in DLS;
        if mag (vector(x,y,z)-dl.pos)<0.01;
            continue
        r - vector (x,y,z) -dl.pos
        dl - (mu_0*current/(4*pi))*(dl.axis).cross(x/mag(r))/mag2(r)
        R*dS

#print mag(r)
arrow(pos*vector(x,y,z).axis-3r3-B, color*color.green)
#arrow (position*vector(x,y,z)axis-0.1*norm(3), color*color.green)
                             
