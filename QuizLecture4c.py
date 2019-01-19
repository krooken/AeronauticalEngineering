import FlightNavigation as FN



'''
An aircraft flies at an altitude of 32,000 ft. Determine its altitude in metres.

If the ground beneath the aircraft is situated 6,000 ft above sea level, what is the
height of the aircraft in feet?
'''

altitude_feet = 32000.0
ground_height_feet = 6000.0

altitude = FN.feet_to_meters(altitude_feet)

print(altitude)

height_feet = altitude_feet-ground_height_feet

print(height_feet)