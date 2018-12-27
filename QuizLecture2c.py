import StandardAtmosphere as ISA

'''What is, according to the standard atmosphere, the temperature (in Kelvin) at 38,969
metres altitude?'''

'''What is, according to the standard atmosphere, the air pressure (in Pascal) at 38,969
metres altitude?'''

'''What is, according to the standard atmosphere, the air density (in kilograms per cubic
metre) at 38,969 metres altitude?'''

target_height = 38969.0
(temp, pressure, density) = ISA.atmospheric_details(target_height)
print temp
print pressure
print density