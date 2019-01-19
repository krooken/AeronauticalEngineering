import StandardAtmosphere as ISA
import numpy as np

nautical_mile = 1852.0
foot = 0.3048

ny = 1.4

def meters_to_miles(meters):
	return meters/nautical_mile

def miles_to_meters(miles):
	return miles*nautical_mile

def knots_to_ms(knots):
	return miles_to_meters(knots)/3600.0

def ms_to_knots(airspeed):
	return meters_to_miles(airspeed)*3600.0

def meters_to_feet(meters):
	return meters/foot

def feet_to_meters(feet):
	return feet*foot

def fpm_to_ms(feet_per_min):
	return feet_to_meters(feet_per_min)/60.0

def ms_to_fpm(airspeed):
	return meters_to_feet(airspeed)*60.0

def speed_of_sound(temperature=ISA.temperature_at_sea_level,
	ny=ny, R=ISA.R):
	return np.sqrt(ny*R*temperature)

def mach_number(speed, altitude):
	(temp, _, _) = ISA.atmospheric_details(altitude)
	a = speed_of_sound(temp, ny, ISA.R)
	return speed/a

def airspeed_true(airspeed_equivalent, density_air):
	return airspeed_equivalent*np.sqrt(ISA.density_air_at_sea_level/density_air)

def airspeed_equivalent(airspeed_true, density_air):
	return airspeed_true*np.sqrt(density_air/ISA.density_air_at_sea_level)