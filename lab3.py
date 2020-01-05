# Rassam Yazdi
# 1006019425
# Section 0102
# ESC180 Lab 3

import utilities

def rotate_90_degrees(image_array, direction = 1):
	""""
	Description: This function is responsible for rotating an image given in 
	nested list form by 90 degrees in a given direction
	
	Type Contract: [nested list][int] -> (nested list)
	
	Example: for counter clockwise...
	1  2  3
	4  5  6
	7  8  9
	 
	turns into:
	3  6  9 
	2  5  8 
	1  4  7 
	"""	
	#1 for clock_wise. -1 for anticlockwise
	output_array = []
	if direction == 1:
		for i in range(len(image_array)):
			temp_list  = []
			for j in reversed(range(len(image_array[0]))):
				temp_list.append(image_array[j][i])
			output_array.append(temp_list)	
			
	if direction == -1:
		for i in reversed(range(len(image_array))):
			temp_list  = []
			for j in range(len(image_array[0])):
				temp_list.append(image_array[j][i])
			output_array.append(temp_list)	
	
	return output_array

def flip_image(image_array, axis = 0):
	""""
	Description: This function is responsible for flipping an image about a given 
	axis by manipulating the pixel information which is taken in as a list
	
	Type Contract: [nested list][int] -> (nested list)
	
	Example: flipping a standing human photo over x-axis will put their feet 
	where their head would be and vice versa
	"""
	#axis = -1 (along x = y), 0 along y, 1 along x
	output_array = []
	if axis == -1:
		for i in reversed(range(len(image_array))):
			temp_list  = []
			for j in reversed(range(len(image_array[0]))):
				temp_list.append(image_array[j][i])
			output_array.append(temp_list)
			
	elif axis == 0:
		for i in range(len(image_array)):
			temp_list  = []
			for j in reversed(range(len(image_array[0]))):
				temp_list.append(image_array[i][j])
			output_array.append(temp_list)
				
	elif axis == 1:
		for i in reversed(range(len(image_array))):
			temp_list  = []
			for j in range(len(image_array[0])):
				temp_list.append(image_array[i][j])
			output_array.append(temp_list)
							
	return output_array

def crop(image_array, direction, n_pixels):
	""""
	Description: This function is responsible for cropping an image starting from
	the given direction and moving n pixels inwards
	
	Type Contract: [nested list][string][int] -> (nested list)
	
	Example: For cropping from up by 1 pixel...
	1  2  3
	4  5  6
	7  8  9
	
	turns into:
	4  5  6
	7  8  9
	"""
	
	output_array = []
	
	if direction == 'down':
		for i in range(len(image_array)-n_pixels):
			temp_list  = []
			for j in range(len(image_array[0])):
				temp_list.append(image_array[i][j])
			output_array.append(temp_list)
	if direction == 'up':
		for i in range(n_pixels,len(image_array)):
			temp_list  = []
			for j in range(len(image_array[0])):
				temp_list.append(image_array[i][j])
			output_array.append(temp_list)
	if direction == 'right':
		for i in range(len(image_array)):
			temp_list  = []
			for j in range(len(image_array[0])-n_pixels):
				temp_list.append(image_array[i][j])
			output_array.append(temp_list)
	if direction == 'left':
		for i in range(len(image_array)):
			temp_list  = []
			for j in range(n_pixels,len(image_array[0])):
				temp_list.append(image_array[i][j])
			output_array.append(temp_list)
	
	return output_array

def invert_grayscale(image_array):
	""""
	Description: This function is responsible for inverting the intensity of the 
	pixels in a white to black range
	
	Type Contract: [nested list] -> (nested list)
	
	Example: A fully white pixel would turn completely black once an image is
	put through this function

	"""
	
	output_array = []
	
	for i in range(len(image_array)):
		temp_list  = []
		for j in range(len(image_array[0])):
			temp_list.append((255 - image_array[i][j]))	
		output_array.append(temp_list)
	
	return output_array			
			

def rgb_to_grayscale(rgb_image_array):
	""""
	Description: This function is responsible for turning a colour image into
	a grayscle image by changing the individual pixels
	
	Type Contract: [nested list] -> (nested list)
	
	Example: Colour image turns into grayscale

	"""
	
	output_array = []
	
	for i in range(len(rgb_image_array)):
		temp_list  = []
		for j in range(len(rgb_image_array[0])):
			temp_list.append(0.2989*rgb_image_array[i][j][0] + 0.5870*rgb_image_array[i][j][1] + 0.1140*rgb_image_array[i][j][2])
		output_array.append(temp_list)

	return output_array

def invert_rgb(image_array):
	""""
	Description: This function is responsible for inverting the intensity of the 
	pixels in a white to black range
	
	Type Contract: [nested list] -> (nested list)
	
	Example: A fully white yellow would turn completely blue once an image is
	put through this function

	"""
	
	output_array = []
	
	for i in range(len(image_array)):
		temp_list  = []
		for j in range(len(image_array[0])):
			very_temp_list = []
			for k in range(3):
				very_temp_list.append((255 - image_array[i][j][k]))
			temp_list.append(very_temp_list)	
		output_array.append(temp_list)
	
	return output_array				


if (__name__ == "__main__"):
	
	
	file = 'surprised_pikachu.png'
	utilities.write_image(crop(utilities.image_to_list(file),'up',299), '2TESTupcrop.png')
	utilities.write_image(crop(utilities.image_to_list(file),'down',299), '2TESTdowncrop.png')
	utilities.write_image(crop(utilities.image_to_list(file),'left',299), '2TESTleftcrop.png')
	utilities.write_image(crop(utilities.image_to_list(file),'right',299), '2TESTrightcrop.png')

	#utilities.write_image(rotate_90_degrees(utilities.image_to_list(file), 1), '2Test90cw.png')
	#utilities.write_image(rotate_90_degrees(utilities.image_to_list(file), -1), '2Test90ccw.png')
	
	#utilities.write_image(flip_image(utilities.image_to_list(file), -1), '2Testflipyx.png')
	#utilities.write_image(flip_image(utilities.image_to_list(file), 0), '2Testflipy.png')
	#utilities.write_image(flip_image(utilities.image_to_list(file), 1), '2Testflipx.png')
	
	#utilities.write_image(rgb_to_grayscale(utilities.image_to_list(file)), '3Testinvrgb.png')
