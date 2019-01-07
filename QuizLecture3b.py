import FlightDynamics as FD
import StandardAtmosphere as ISA

'''A general aviation aircraft, with a wing surface area of 18 square metres, flies at sea
level with a speed of 180 kilometres per hour. Its lift curve is shown below. Given that
lift equals weight for this aircraft and that the aircraft flies at a 8 degree angle of
attack, what is its mass (in kilograms)?'''

speed_air = 180.0/3.6
surface_area = 18.0
lift_coefficient = 0.78
lift_force = FD.lift(lift_coefficient, speed_air, surface_area)
print lift_force/ISA.g # 2191.5


'''An cruising Airbus A320 (m = 58,000 kg) with a wing surface area of 123 m^2 flies at
altitude of 8 kilometres, with an airspeed of 800 kilometres per hour. Determine the lift
coefficient in this flight condition.'''

lift = 58000.0*ISA.g
surface_area = 123.0
velocity = 800.0/3.6
height = 8000.0
(temp, pressure, density) = ISA.atmospheric_details(height)
lift_coefficient = FD.lift_coefficient(lift, velocity, surface_area, density)
print lift_coefficient # 0.36


'''For an aircraft, the 'wing loading' is defined as Wing loading=W/S. You will now
calculate this so-called wing loading for a fully loaded Boeing 747-400.

Using the internet, look up the wing surface area (in square metres) of a Boeing 747-400:'''

surface_area = 525.0

'''In case the aircraft flies with its mass equal to the so-called maximum take-off
weight, determine the wing loading (in Newton per square metre) of this Boeing 747-400:'''

maximum_takeoff_weight = 396890.0
force = maximum_takeoff_weight*ISA.g
wing_loading = force/surface_area
print wing_loading