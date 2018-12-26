import StandardAtmosphere
import scipy

'''An aircraft flies at an altitude of 30,000 feet. Determine the air temperature (in [K]),
air pressure (in [Pa]) and air density (in [kg/m^3]) at this altitude, according to the
standard atmosphere.'''

height_feet = 30000.0
feet = 0.3048
height = height_feet*feet

temperature_difference = StandardAtmosphere.temperature_difference(height)
temperature_base = StandardAtmosphere.temperature_at_sea_level
temperature_target = temperature_base+temperature_difference
print temperature_target # 228.714

pressure_base = StandardAtmosphere.pressure_at_sea_level
pressure_ratio = StandardAtmosphere.pressure_rate_dyn(temperature_target, temperature_base)
pressure_target = pressure_ratio*pressure_base
print pressure_target # 30,082.8

density_target = StandardAtmosphere.density(pressure_target, temperature_target)
print density_target # 0.4583