import FlightDynamics as FD

'''Below you see a picture of an aircraft flying at an altitude of 11.5 kilometres.
Suppose that at some point both its engines fail, and the aircraft is forced to glide to
the ground. Given that the glide ratio of the aircraft is 14, what airports is the plane
capable of reaching (neglect the additional distance flown due to turning)?'''

glide_ratio = 14.0
height = 11500.0
print FD.glide(height, glide_ratio) # 161