#!/opt/homebrew/bin/python3
import cv2
import sys, os
from concurrent.futures import ThreadPoolExecutor


USAGE = "USAGE::: \"createSrcSet.py <number of copies> <source img>\" "

def createTinyImg(src, newDim: tuple[int], fileName: str):
    try:
        src = cv2.resize(src, (newDim[0], newDim[1]))
        cv2.imwrite(fileName, src)
        print(f"Successfully wrote to... {fileName}")
    except Exception as e:
        print(f"Error while processing {fileName}: {e}")


def main(givenImg, numTinyCopies, folderName="") -> int:
    imgH = givenImg.shape[0]
    imgW = givenImg.shape[1]

    imgInterval = imgW // numTinyCopies

    ### CREATE NEW DIRECTORY FOR OUTPUT
    newDir = "./tiny_copies_{}".format(folderName)

    if not os.path.exists(newDir):
        os.makedirs(newDir)

    print("MAKING SMALLER COPIES IN SAME FOLDER AS IMAGE... ")
    copiesMade = 0
    with ThreadPoolExecutor(max_workers=4) as threads:         
        for i in range(numTinyCopies):
            oldW = imgW
            imgW = imgW - imgInterval
            imgH = int((imgW / oldW) * imgH)
            # print("NEW WIDTH!!!", imgW)
            if (imgW <= 36 or imgH <= 36):
                print(f"reached minimum image W: {imgW} | H: {imgH} size at copy number {i}.\nEnding process.")
                copiesMade = i
                return copiesMade
            else:
                newImgName = "{0}/new_img_{1}.jpeg".format(newDir, i)
                threads.submit(createTinyImg, givenImg, (imgW, imgH), newImgName)
            copiesMade = i
    return copiesMade

###
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("ERROR: must add one integer argument, your source file path, and destination")
        print(USAGE)
        exit(-1)

    givenImg = sys.argv[2]
    img = cv2.imread(givenImg)

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
    res = main(img, numTinyCopies, sys.argv[2])
    print("COPIES::: ", res)
            
