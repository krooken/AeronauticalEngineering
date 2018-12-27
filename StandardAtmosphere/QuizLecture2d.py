import StandardAtmosphere as ISA

'''You are given the following two statements:
1. If an aircraft flies at a geometric altitude of 10,000 metres, its geopotential
altitude is 9,978 metres.
2. If an aircraft flies at a geopotential altitude of 12,000 metres, its geometric
altitude is 12,023 metres.
Which of the following is true?'''

geometric = 10000.0
print ISA.geopotential(geometric)

geopotential = 12000.0
print ISA.geometric(geopotential)


'''A spacecraft flies over Mars at a geopotential altitude of 80 kilometres. Determine its
geometric altitude (in metres).'''

geopotential = 80000.0
radius_mars_mean = 3396200.0
print ISA.geometric(geopotential, radius_mars_mean) # 81929.92