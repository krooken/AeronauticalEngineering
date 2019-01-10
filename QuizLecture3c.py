import StandardAtmosphere as ISA
import FlightDynamics as FD


'''Aircraft drag

Suppose that the lift-drag polar of the previous problem belongs to a 32,000 kilogram
aircraft with an average wing chord of 3.5 metres and a wingspan of 30 metres. At a
certain moment this aircraft flies in cruise at a speed of 300 ft/s, with an air density
of 1.0 kilogram per cubic metre. For this flight condition, determine the aircraft drag
(in Newton).

Hint: use the fact that: D = L*D/L = W*Cd/Cl
'''

mass = 32000.0
wingspan = 30.0
wingchord = 3.5
surface_area = wingspan*wingchord
density_air = 1.0
speed_feet = 300.0
speed_si = speed_feet*0.3048

lift = ISA.g*mass

lift_coefficient = FD.lift_coefficient(lift, speed_si, surface_area, density_air)

print(lift_coefficient)

drag_coefficient = 0.06

drag = lift * drag_coefficient/lift_coefficient

print(drag)