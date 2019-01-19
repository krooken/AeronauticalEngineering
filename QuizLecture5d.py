import StandardAtmosphere as ISA
import Structures

'''
A modern jet flies at an altitude of 6,200 metres, during its climb to cruise altitude.
For additional passenger comfort, the cabin pressure is maintained at 80% of the sea level
value.

Given that the fuselage radius is 3.2 metres and that the skin thickness is 2.4 mm,
compute the circumferential stress in the fuselage skin (in MPa or MegaPascal): (Assume
ISA conditions)
 
Additionally, compute the longitudinal stress in the fuselage skin (in MPa or MegaPascal):
'''

altitude = 6200.0
pressure_cabin_ratio = 0.8

fuselage_radius = 3.2
skin_thickness = 0.0024

(_, pressure_alt, _) = ISA.atmospheric_details(altitude)
pressure_cabin = pressure_cabin_ratio*ISA.pressure_at_sea_level
pressure_difference = pressure_cabin-pressure_alt

stress_circumferential = Structures.stress_circumferential(
							pressure_difference,
							fuselage_radius,
							skin_thickness)

stress_circumferential_MPa = stress_circumferential/10.0**6

print(stress_circumferential_MPa)

stress_longitudinal = Structures.stress_longitudinal(
						pressure_difference,
						fuselage_radius,
						skin_thickness)

stress_longitudinal_MPa = stress_longitudinal/10.0**6

print(stress_longitudinal_MPa)


'''
A futuristic Aircraft manufacturer has come up with the idea to build a supersonic
passenger jet, which is supposed to perform cruise flight at 24 kilometres altitude. For
passenger comfort, the cabin pressure should remain at least 72 percent of the sea level
value. To give the aircraft an aerodynamic shape its fuselage is rather long and slender,
meaning the fuselage diameter is 'just' 4.5 metres.

The engineers have asked you, now experts in the field of pressure cabins and fatigue, to
determine the required skin thickness to deal with the circular stress (which may not
exceed 75MPa) in the fuselage skin. To be on the safe side, they ask you to take into
account a safety factor of 1.5.

What will be for this aircraft the skin thickness (in millimetres)?
'''

altitude = 24000.0
pressure_cabin_ratio = 0.72
fuselage_radius = 4.5/2.0

stress_circular_max = 75.0 * 10.0**6
safety_factor = 1.5

pressure_cabin = pressure_cabin_ratio*ISA.pressure_at_sea_level
(_, pressure_alt, _) = ISA.atmospheric_details(altitude)
pressure_difference = pressure_cabin-pressure_alt

thickness_min = Structures.thickness_circumferential(
					pressure_difference,
					fuselage_radius,
					stress_circular_max)
thickness_safe = thickness_min*safety_factor
thickness_safe_mm = thickness_safe*1000.0

print(thickness_safe_mm)