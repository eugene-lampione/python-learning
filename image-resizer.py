# pip install Pillow
from PIL import Image

# function to resize the image
def resizeImage(inputPath,outputPath,newWidth):
    # error handling
    try:
        # open the image
        # img = Image.open(inputPath)
        with Image.open(inputPath) as img:
            # get the original dimensions
            # print(img.size)
            # img.size == (3024, 4032)
            width,height = img.size

            # print out our dimensions
            print(f"Original Size: {width} x {height}")

            # calculate new height to maintain aspect ratio (H/W)
            aspectRatio = height / width

            # Aspen.jpg: width= 960 | height= 720
            # Aspen aspect ration = .75
            # To calculate new height (newWidth * aspectRatio = newHeight)

            # get the new height
            newHeight = int(newWidth * aspectRatio)

            # resize the image
            resizedImage = img.resize((newWidth,newHeight))

            # save the new image
            resizedImage.save(outputPath)

            # output the results
            print(f"Image was resized and saves as {outputPath}. New Size: {newWidth} x {newHeight}")
        
    except IOError:
        print("Error: Unable to open or save the image. Please check the file path.")


# main function
def imageResizer():
    # /Users/eugene.lampione/Pictures/tilepix/IMG_3290.jpg
    inputPath = input("Enter the path of the image to resize: ")
    outputPath = input("Enter the output path for resized image: ")
    newWidth = int(input("Enter the width for the resized image: "))

    # resize the image
    resizeImage(inputPath,outputPath,newWidth)



# call main function
imageResizer()