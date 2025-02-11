from matplotlib import pyplot as plt
import cv2 as cv

def gray_image_histogram(image_file):

    image = cv.imread(image_file, cv.IMREAD_GRAYSCALE) #Loading the image in grayscale
    histogram = cv.calcHist([image], [0], None, [256], [0, 256]) #Creating histogram

    #Plotting
    fig, ax = plt.subplots(figsize = (5,5))
    ax.imshow(image, cmap = 'gray', vmin=0, vmax=255)
    ax.set_title('Grayscale image')
    plt.show()
    
    fig, ax = plt.subplots(figsize = (5,5))
    ax.plot(histogram)
    ax.set_title('Histogram of grayscale image')
    plt.show()

def histogram_equalization(image_file):

    image = cv.imread(image_file, cv.IMREAD_GRAYSCALE)  #Loading the image in grayscale
    equalized_image = cv.equalizeHist(image)  #Perform histogram equalization with cv equalizeHist

    #Creating histograms for the original image and for the equalized histogram
    original_histogram = cv.calcHist([image], [0], None, [256], [0, 256])
    equalized_histogram = cv.calcHist([equalized_image], [0], None, [256], [0, 256])

    #Plotting
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Histogram Equalization', fontsize=16) 

    axes[0][0].imshow(image, cmap='gray', vmin=0, vmax=255)
    axes[0][0].set_title('Original Image')
    axes[0][0].axis('off')

    axes[0][1].plot(original_histogram)
    axes[0][1].set_title('Original Histogram')

    axes[1][0].imshow(equalized_image, cmap='gray', vmin=0, vmax=255)
    axes[1][0].set_title('Equalized Image')
    axes[1][0].axis('off')

    axes[1][1].plot(equalized_histogram)
    axes[1][1].set_title('Equalized Histogram')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


if __name__ == '__main__':

    files = ['Fig0316(1)(top_left).tif', 'Fig0316(2)(2nd_from_top).tif', 'Fig0316(3)(third_from_top).tif', 'Fig0316(4)(bottom_left).tif']
    for filename in files:
        
        # histogram_equalization(filename)
        gray_image_histogram(filename)

