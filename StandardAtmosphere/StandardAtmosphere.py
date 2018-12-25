# Constants

R = 287.0
K = 273.15
temperature_at_sea_level = 15.0 + K
pressure_at_sea_level = 101325
air_density_at_sea_level = 1.225

molar_mass_helium = 4.0
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