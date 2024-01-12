import cv2 as cv
import os

def WaitEsc(cv):

    key = 0
    while (key != 27):
        key = cv.WaitKey(0)

    cv.destroyAllWindows()



def TransfPic(img, dsize = (500, 500)):

    img0 = cv.resize(img, dsize)
    return img0



if __name__ == '__main__':

    files = os.listdir()
    count = 0
    for file in files:
        if file.endswith('.jpg'):
            count += 1
            img = cv.imread(file)
            img0 = TransfPic(img)
            cv.imwrite(f'Gap_{count}.jpg', img0)

    print("Procedure finished.")
