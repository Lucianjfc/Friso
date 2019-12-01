import numpy as np
import matplotlib.image as mpimg
import sys, os

#lendo a imagem
dir_img = sys.argv[1]
dir_output = sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) == 4 else 5
img = mpimg.imread(dir_img)

# Creating directory if not exists

if not os.path.exists(dir_output):
	os.mkdir(dir_output)

height, width, collor_pattern = img.shape
#figura 4.19

def white_img(height, width, collor_pattern):
	white_img = np.zeros([height,width,collor_pattern], dtype = np.uint8)
	if collor_pattern == 4:
		white_img[:,:height] = [255, 255, 255, 0.3]
		#white_img[:,height] = [0.1,0.1,0.1,0.1]
	else:
		white_img[:,:height] = [1, 1, 0.9]
		#white_img[:,height] = [0,0,0]
	return white_img

def image1(img):
	final_img = np.hstack(tuple(img for i in range(n)))
	#Saving image
	mpimg.imsave(dir_output + 'figura1.png', final_img)

def image2(img, white_img):
	vertical_join = np.vstack((img, white_img))
	rotate_img = np.rot90(vertical_join, 2)
	reflected_img = np.fliplr(rotate_img)
	final_img = np.hstack(tuple(vertical_join if i % 2 == 0 else reflected_img for i in range(n)))
	#saving image
	mpimg.imsave(dir_output + 'figura2.png', final_img)
	

def image3(img):
	reflection = np.fliplr(img)
	final_img = np.hstack(tuple(reflection if i % 2 == 0 else img for i in range(n)))
	#saving image
	mpimg.imsave(dir_output + 'figura3.png', final_img)

def image4(img):
	reflection = np.flipud(img)
	img_stack = np.vstack((img, reflection))
	final_img = np.hstack(tuple(img_stack for i in range(n)))
	#saving image
	mpimg.imsave(dir_output + 'figura4.png', final_img)

def image5(img, white_img): 
	img_stack = np.vstack((img, white_img))
	rotate_img = np.rot90(img_stack, 2)
	final_img = np.hstack(tuple(img_stack if i % 2 == 0 else rotate_img for i in range(n)))
	#saving image
	mpimg.imsave(dir_output + 'figura5.png', final_img)


def image6(img):

	img_reflection = np.fliplr(img)
	img_stack = np.hstack((img_reflection, img))

	# Setting image height, image width and collor pattern
	height, width, collor_pattern = img_stack.shape
	#checking if the collor pattern is rgb or rgba
	img_white = white_img(height, width, collor_pattern)
	
	img_vstack = np.vstack((img_stack, img_white))
	img_rotate = np.rot90(img_vstack, 2)
	final_img = np.hstack(tuple(img_vstack if i % 2 == 0 else img_rotate for i in range(n)))
	#saving image
	mpimg.imsave(dir_output + 'figura6.png', final_img)
	
def image7(img):
	reflection_img = np.flipud(img)
	img_stack = np.vstack((img, reflection_img))
	reflection_img_stack = np.fliplr(img_stack)

	final_img = np.hstack(tuple(img_stack if i % 2 == 0 else reflection_img_stack for i in range(n)))
	#saving image
	mpimg.imsave(dir_output + 'figura7.png', final_img)

image1(img)
image2(img, white_img(height, width, collor_pattern))
image3(img)
image4(img)
image5(img, white_img(height, width, collor_pattern))
image6(img)
image7(img)
