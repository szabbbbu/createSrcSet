import createSrcSet, cv2

#USES ./test_images/test1.webp
def test_main(numTinyCopies: int) -> None:
    img = cv2.imread("./test_images/test1.webp")
    resImgCount = createSrcSet.main(img, numTinyCopies, folderName="tester")
    assert resImgCount == numTinyCopies-1, "SOMETHING WRONG"

if __name__ == "__main__":
    test_main(1)
    test_main(8)
    test_main(25)
    test_main(3)
    # test_main("")
