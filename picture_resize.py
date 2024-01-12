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

    dire = input("Input directory:")
    name = input("Output name:")
    #dire.replace('\\', '/')
    files = os.listdir(dire)
    count = 0
    for file in files:
        if file.endswith('.jpg'):
            count += 1
            abs_path = os.path.join(dire, file)
            print(abs_path)
            abs_path.replace('\\', '/')
            img = cv.imread(abs_path)
            img0 = TransfPic(img)
            name0 = f'{name}_{count}.jpg'
            name0 = os.path.join(dire, name0)
            cv.imwrite(name0, img0)

    print("Procedure finished.")
