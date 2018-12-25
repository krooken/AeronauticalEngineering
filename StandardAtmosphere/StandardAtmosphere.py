# Constants

R = 287.05
K = 273.15
g = 9.800

temperature_at_sea_level = 15.0 + K
pressure_at_sea_level = 101325
density_air_at_sea_level = 1.225

molar_mass_helium = 4.002
molar_mass_nitrogen = 28.0
molar_mass_air = 28.97

atmospheric_layers = [
	('troposphere', 0.0, 11000.0, -6.5),
	('stratosphere', 11000.0, 20000.0, 1),
	('stratosphere', 20000.0, 32000.0, 2.8),
	('stratosphere', 32000.0, 47000.0, 0.0),
	('mesosphere', 47000.0, 51000.0, -2.8),
	('mesosphere', 51000.0, 71000.0, -2.0)
	]

def pressure(
	density=density_air_at_sea_level,
	temperature=temperature_at_sea_level,
	R = R):
	return density*temperature*R
	
def density(
	pressure=pressure_at_sea_level,
	temperature=temperature_at_sea_level,
	R = R):
	return pressure/(temperature*R)
	
def balloon_lift_general(
	volume, density_gas,
	density_ambient=density_air_at_sea_level,
	g=g):
	return volume*g*density_ambient*(1-density_gas/density_ambient)
	
def balloon_lift_hot_air(
	volume, temperature_difference,
	temperature_ambient=temperature_at_sea_level,
	density_ambient=density_air_at_sea_level,
	g=g):
	return volume*g*density_ambient \
		* (temperature_difference/(temperature_difference+temperature_ambient))
		
def balloon_lift_gas(
	volume, molar_mass_gas,
	molar_mass_ambient=molar_mass_air,
	density_ambient=density_air_at_sea_level,
	g=g):
	return volume*g*density_ambient \
		* (1 - molar_mass_gas/molar_mass_ambient)
		
