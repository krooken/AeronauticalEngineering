import FlightNavigation as FN
import StandardAtmosphere as ISA
import numpy as np

'''
At an altitude of 24,000 feet a Pitot tube measures a total pressure of 0.5564 bar.
Determine the equivalent airspeed (in metres per second) of the aircraft (assuming ISA
conditions).
'''

altitude_feet = 24000.0
total_pressure_bars = 0.5564

altitude = FN.feet_to_meters(altitude_feet)
total_pressure = total_pressure_bars*100000.0

(_, static_pressure, density_air_alt) = ISA.atmospheric_details(altitude)

speed_equivalent = np.sqrt((total_pressure - static_pressure)*2.0/ISA.density_air_at_sea_level)

print(speed_equivalent)

'''
Consider again the Pitot tube of the previous exercise. What is for this aircraft the true
airspeed (in metres per second)?
What is the Mach number this aircraft flies at?
'''

density_air_sea = ISA.density_air_at_sea_level

speed_true = speed_equivalent*np.sqrt(density_air_sea/density_air_alt)

mach_number = FN.mach_number(speed_true, altitude)

print(speed_true)
print(mach_number)


'''
An aircraft flies with an equivalent airspeed of 300 ft/s at an altitude where the air
density is 0.74 kg/m. Determine its true airspeed, in kilometres per hour.
'''

speed_feet_equivalent = 300.0
density_air = 0.74

speed_equivalent = FN.feet_to_meters(speed_feet_equivalent)
speed_true = FN.airspeed_true(speed_equivalent, density_air)

speed_kph_true = speed_true*3.6

print(speed_kph_true)


'''
A commercial aircraft flies at a Mach number of 0.67 at an altitude where the air
temperature is -19.15 C. Assume ISA conditions.

Determine the altitude (in metres) this aircraft flies at.

Calculate the equivalent airspeed (in feet per second) of this aircraft.
'''

mach_number = 0.67
temperature_air_centigrade = -19.15
temperature = temperature_air_centigrade + ISA.K

lapse_rate = ISA.atmospheric_layers[0][3]

altitude = (temperature-ISA.temperature_at_sea_level)/lapse_rate

print(altitude)

speed_of_sound = FN.speed_of_sound(temperature)
airspeed_true = mach_number*speed_of_sound
(_, _, density_air_alt) = ISA.atmospheric_details(altitude)
airspeed_equivalent = FN.airspeed_equivalent(airspeed_true, density_air_alt)
airspeed_equivalent_feet = FN.meters_to_feet(airspeed_equivalent)

print(airspeed_equivalent_feet)


'''
A Boeing 777 is flying at 8.2 kilometres altitude, with a Mach number of 0.84. Determine
the equivalent airspeed of the aircraft (in kts).
'''

altitude = 8200.0
mach_number = 0.84

(temperature_alt, _, density_alt) = ISA.atmospheric_details(altitude)
speed_of_sound = FN.speed_of_sound(temperature_alt)
airspeed_true = speed_of_sound*mach_number
airspeed_equivalent = FN.airspeed_equivalent(airspeed_true, density_alt)
airspeed_equivalent_knots = FN.ms_to_knots(airspeed_equivalent)

print(airspeed_equivalent_knots)