import scipy
import numpy as np
import StandardAtmosphere as ISA

def glide(height, glide_ratio):
	return height*glide_ratio
	
def glide_angle(glide_ratio):
	return np.arctan(1/glide_ratio)
	
def glide_angle_deg(glide_ratio):
	return glide_angle(glide_ratio)*180.0/scipy.pi

def lift(lift_coefficient, velocity, surface_area,
		density_air=ISA.density_air_at_sea_level):
	return lift_coefficient*(1.0/2*density_air*velocity**2)*surface_area
	
def lift_coefficient(lift, velocity, surface_area,
		density_air=ISA.density_air_at_sea_level):
	return lift/((1.0/2*density_air*velocity**2)*surface_area)