import cv2
import sys, os


USAGE = "USAGE::: python3 createSet <number of copies> <source img> "

if (len(sys.argv) != 3):
    print("ERROR: must add one integer argument, your source file path, and destination")
    print(USAGE)
    exit(-1)

img = cv2.imread(sys.argv[2])

if img is None:
    print("ERROR opening your image\nPlease make sure the filepath is correct")
    print(USAGE)
    exit(-1)

try:
    numTinyCopies = int(sys.argv[1])
except ValueError as ex:
    print("ERROR! Use an integer")
    print(ex)
    print(USAGE)
    exit(-1)

imgH = img.shape[0]
imgW = img.shape[1]

newDir = "./{}_srcSet".format(sys.argv[2])

if not os.path.exists(newDir):
    os.makedirs(newDir)

print("MAKING SMALLER COPIES IN SAME FOLDER AS IMAGE... ")
for i in range(numTinyCopies):
    imgH = imgH // 2
    imgW = imgW // 2
    if (imgW <= 36 or imgH <= 36):
        print("reached minimum image size. Ending process.")
        break
    else:
        newImg = cv2.resize(img, (imgW, imgH))
        newImgName = "{0}/new_img_{1}.jpeg".format(newDir, i)
        cv2.imwrite(newImgName, newImg)

