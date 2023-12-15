epsilon = 0.001 # very small time interval



x_initial= float(input("Please enter the initial position of the object in the x direction:"))
y_initial= float(input("Please enter the initial position of the object in the y direction:"))
vx_initial= float(input("Please enter the initial velocity of the object in the x direction:"))
vy_initial= float(input("Please enter the initial velocity of the object in the y direction:"))
G= float(input("Please enter the G value you wish to use:"))
M=float(input("Please enter the Mass of the central body you wish to use:"))

Earth = sphere(pos = vec(x_initial,y_initial,0) , texture = textures.earth , radius = 0.1,make_trail = True,axis = vec(0,1,1)) 
Sun = sphere(pos = vec(0,0,0) , radius = 0.1 , color = color.yellow)



Earth.velocity = vec(vx_initial , vy_initial , 0)


r = mag(Earth.pos)



Earth.acceleration = -G*M*Earth.pos/(r**3)

 

Earth.velocity= Earth.velocity +(epsilon/2.0)*Earth.acceleration

scene.autoscale = True
n = 0
while True:
    
   
    rate(500)
    Earth.pos = Earth.pos + epsilon*Earth.velocity
    r = mag(Earth.pos) 
    Earth.acceleration=-G*M*Earth.pos/(r**3)
    Earth.velocity= Earth.velocity + epsilon *Earth.acceleration
    Earth.rotate(angle = n , axis = vec(0,1,1))
    n+=0.00001*pi
