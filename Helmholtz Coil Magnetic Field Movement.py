from _future_ import division
from visual import
from numpy import arange,pi
epsilon 0 = 8.35E-12
eCharge = 1.602E-19
mu_0 = pi*4E-7

sceen.center = (0,0,0)
sceen.width = 800
scene.length = 600
scene.range = (5,5,5)

R - 1 #Radius of loop
Current - 2 #Current of loop

DLS - {}
for theta1 in arange (0,2*pi,2*pi/100)}
position-vector (2,R*cos(theta1)R*sin(theta1))
tangent = position.cross(vector(1,0,0))
dl = (2*pi/100)*(tangent/mag(tangent))
thisdl = arrow(pos*position,axis*dl)
DLS.append(thisdl)

gridRange = arange(-3.5, 3.5+0.5, 0.5)

for x in gridRange;
    for y in gridRange;
        for z in gridRange;
        B-vector(0,0,0)
        for dl in DL.5;
        if neg (x,y,z)-dl.pos) < 0.01;
