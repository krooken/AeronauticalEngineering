import FlightDynamics as FD
import numpy as np

'''Below you see a picture of an aircraft flying at an altitude of 11.5 kilometres.
Suppose that at some point both its engines fail, and the aircraft is forced to glide to
the ground. Given that the glide ratio of the aircraft is 14, what airports is the plane
capable of reaching (neglect the additional distance flown due to turning)?'''

glide_ratio = 14.0
height = 11500.0
print FD.glide(height, glide_ratio) # 161


'''Again consider the aircraft of the previous problem, which had a glide ratio of 14.
What will be for this aircraft the glide angle (in degrees)?'''

glide_ratio = 14.0
print FD.glide_angle_deg(glide_ratio)


'''An aircraft flies with a groundspeed of 80 metres per second, whilst experiencing a 54
kilometre per hour headwind. What is its airspeed (in metres per second)?'''

speed_ground = 80.0
speed_headwind = 54.0/3.6
print speed_ground+speed_headwind


'''A pilot wants to fly to the North with a ground speed of 120 m/s, so he flies with an
airspeed of 120 m/s. Unfortunately, he forgets about the wind: he experiences a 20 m/s
wind from the North-West (so at an angle of 45 with respect to the intended heading). For
this situation, compute the aircraft's ground speed (in kilometres per hour).'''

speed_air = 120.0
speed_northwest = 20.0
angle_wind = 45.0*np.pi/180.0
speed_ground_north = speed_air-speed_northwest*np.cos(angle_wind)
speed_ground_east = speed_northwest*np.sin(angle_wind)
speed_ground = np.sqrt(speed_ground_north**2 + speed_ground_east**2)
print speed_ground*3.6