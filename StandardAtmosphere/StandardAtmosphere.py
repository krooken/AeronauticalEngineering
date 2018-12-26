import scipy

# Constants

R = 287.05
K = 273.15
g = 9.80665

temperature_at_sea_level = 15.0 + K
pressure_at_sea_level = 101325
density_air_at_sea_level = 1.225

molar_mass_helium = 4.002
molar_mass_nitrogen = 28.0
molar_mass_air = 28.97

atmospheric_layers = [
	('troposphere', 0.0, 11000.0, -0.0065),
	('stratosphere', 11000.0, 20000.0, 0.001),
	('stratosphere', 20000.0, 32000.0, 0.0028),
	('stratosphere', 32000.0, 47000.0, 0.0),
	('mesosphere', 47000.0, 51000.0, -0.0028),
	('mesosphere', 51000.0, 71000.0, -0.002)
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
		
def temperature_difference(
	height, lapse_rate=atmospheric_layers[0][-1]):
	return height*lapse_rate
	
def pressure_rate_dyn(
	temperature_target,
	temperature_base=temperature_at_sea_level,
	lapse_rate=atmospheric_layers[0][-1],
	R=R, g=g):
	return (temperature_target/temperature_base)**(-g/(lapse_rate*R))
	
def pressure_rate_stat(
	height_target,
	height_base=atmospheric_layers[0][1],
	temperature_ambient=temperature_at_sea_level,
	R=R, g=g):
	return scipy.exp(-g/(R*temperature_ambient)*(height_target-height_base))
	
def density_rate_dyn(
	temperature_target,
	temperature_base=temperature_at_sea_level,
	lapse_rate=atmospheric_layers[0][-1],
	R=R, g=g):
	return (temperature_target/temperature_base)**(-g/(lapse_rate*R)-1)
	
def density_rate_stat(
	height_target,
	height_base=atmospheric_layers[0][1],
	temperature_ambient=temperature_at_sea_level,
	R=R, g=g):
	return pressure_rate_stat(height_target, height_base, temperature_ambient, R, g)
	
