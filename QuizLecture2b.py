from .. import StandardAtmosphere
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


'''The rate of climb of an aircraft is generally computed from pressure measurements. 
To illustrate the principle behind this, consider the following question:

Suppose we launch a scientific rocket straight up from sea level (at standard conditions)
with a pressure measuring device attached to it. Given that in the first 12 seconds the
rocket experiences a 25% decrease in air pressure, what is the average speed
(rate of climb) of the rocket in these first 12 seconds (in metres per second)?'''

pressure_ratio_decrease = 0.25
target_pressure = 1-pressure_ratio_decrease
g = StandardAtmosphere.g
R = StandardAtmosphere.R
a = StandardAtmosphere.atmospheric_layers[0][-1]
temperature_base = StandardAtmosphere.temperature_at_sea_level
height_difference = (target_pressure**(-a*R/g)*temperature_base-temperature_base)/a
velocity_mean = height_difference/12.0
print velocity_mean # 196.7


'''The hydrostatic equation holds not just for air, but for other fluids such as water
(air, though it is a gas, is often referred to as a 'fluid') as well. In the case of water
the equation becomes even easier, as water (as opposed to air) can be treated as
incompressible, meaning the density is constant. Use a value of 1000 kilogram per cubic
metre as density.

Using this information, compute the local pressure (in [Pa]) at 2.5 metres depth in a
swimming pool situated at 2400 metres altitude in the mountains. Assume a standard
atmosphere.'''

target_height = 2400.0
target_depth = 2.5
density_water = 1000.0
temperature_difference = StandardAtmosphere.temperature_difference(target_height)
temperature_base = StandardAtmosphere.temperature_at_sea_level
temperature_target = temperature_base+temperature_difference
pressure_base = StandardAtmosphere.pressure_at_sea_level
pressure_ratio = StandardAtmosphere.pressure_rate_dyn(temperature_target, temperature_base)
pressure_target = pressure_ratio*pressure_base
pressure_depth = pressure_target + density_water*g*target_depth
print pressure_depth # 100139