def stress_circumferential(pressure_difference, radius, thickness):
	return pressure_difference*radius/thickness

def stress_longitudinal(pressure_difference, radius, thickness):
	return stress_circumferential(pressure_difference, radius, thickness)/2.0

def thickness_circumferential(pressure_difference, radius, max_loading):
	return pressure_difference*radius/max_loading

def thickness_longitudinal(pressure_difference, radius, max_loading):
	return thickness_circumferential(pressure_difference, radius, max_loading)/2.0