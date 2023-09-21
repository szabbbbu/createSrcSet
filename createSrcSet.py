#!/opt/homebrew/bin/python3
import cv2
import sys, os
import concurrent.futures as cf


USAGE = "USAGE::: \"createSrcSet.py <number of copies> <source img>\" "

def createTinyImg(src, newDim: tuple[int], fileName: str):
    try:
        # print("CREATING TINY IMG", type(newDim[1]))
        src = cv2.resize(src, (newDim[0], newDim[1]))
        # print("!!!!", src)
        cv2.imwrite(fileName, src)
        # print("Saved to:", fileName)
    except Exception as e:
        print(f"Error while processing {fileName}: {e}")



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

    imgH = img.shape[0]
    imgW = img.shape[1]

    imgInterval = imgW // numTinyCopies

    newDir = "./{}_srcSet".format(givenImg)

    if not os.path.exists(newDir):
        os.makedirs(newDir)

    print("MAKING SMALLER COPIES IN SAME FOLDER AS IMAGE... ")
    with cf.ThreadPoolExecutor(max_workers=4) as threads:         
        for i in range(numTinyCopies):
            oldW = imgW
            imgW = imgW - imgInterval
            imgH = int((imgW / oldW) * imgH)
            print("NEW WIDTH!!!", imgW)
            if (imgW <= 36 or imgH <= 36):
                print("reached minimum image size. Ending process.")
                break
            else:
                newImgName = "{0}/new_img_{1}.jpeg".format(newDir, i)
                threads.submit(createTinyImg, img, (imgW, imgH), newImgName)
            

