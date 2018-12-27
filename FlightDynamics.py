import scipy
import numpy as np

def glide(height, glide_ratio):
	return height*glide_ratio
	
def glide_angle(glide_ratio):
	return np.arctan(1/glide_ratio)
	
def glide_angle_deg(glide_ratio):
	return glide_angle(glide_ratio)*180.0/scipy.pi