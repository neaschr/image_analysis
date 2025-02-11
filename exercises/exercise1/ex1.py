import numpy as np
import scipy.ndimage as sc
from PIL import Image
import skimage
import matplotlib.pyplot as plt
import matplotlib.colors as cl

#task 1a

A = np.zeros((7, 8))

#Task 1b

A[:,0] = 1
A[:, 1] = 2
A[:, 2] = 3
A[4, 6] = 5
A[5, 6] = 8
# print (A)

#Task 1c

unique_values = np.unique(A)
# print(unique_values)

#Task 1d

B = np.random.random((8,7)) #Generating a matrix consisting of random values
# print(B)

#task 1e

prod = np.matmul(A,B) #Using numpy matrix multiplication
# print(prod)

#task 1f


A_flipped = np.flip(A, 0)#Flipping the matrix up-down
A_flipped = np.flip(A_flipped, 1) #flipping the matrix sideways
A_flipped = np.rot90(A_flipped, 1, (1,0))


rotated_matrix = sc.rotate(A_flipped, angle=37, reshape=True) #Rotating the matrix by 37 degrees
# print(rotated_matrix)

#Task 1 e


#Task 3a

bilde = Image.open(r"grey.jpeg") #reading the picture
# bilde.show()

print(np.shape(bilde)) #Finding the size of the picture

start = (10, 0) #Defining end and start points for the line across which we will measure intensity
end = (10, 7199)
bild = np.array(bilde) #making an array of the picture

intensitet = skimage.measure.profile_line(bild, start, end) #Using skimage to find the intensities across the defined line

plt.plot(intensitet) #Plotting the intensities
plt.title("Intensity Profile Across Defined Line")
plt.xlabel("Pixel Position")
plt.ylabel("Intensity")
plt.show()

#Task 3b
#We already turned the picture into a numpy array in a), with the shape (2400,7200)

#Task 3c

c = cl.ListedColormap(['green', 'red', 'orange', 'yellow', 'pink', 'black'])

fig, ax = plt.subplots(1, 2, figsize = (10, 6))
ax[0].imshow()