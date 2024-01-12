import cv2 as cv
import os

def WaitEsc(cv):

    key = 0
    while (key != 27):
        key = cv.waitKey(0)

    cv.destroyAllWindows()

    

class DisposePic:

    class Params:

        def __init__(self, pm):
            self.scaleFactor = pm[0]
            self.minNeighbors = pm[1]
            self.flags = pm[2]
            self.minSize = pm[3]
            self.maxSize = pm[4]
            self.color = pm[5]

    def __init__(self, xmlFile, pm):
        self.xmlFile = xmlFile
        self.Param = DisposePic.Params(pm)  
        self.detection = cv.CascadeClassifier(xmlFile)

    def dispose(self, img):
        #print(self.Param.scaleFactor, self.Param.minNeighbors, self.Param.flags, self.Param.minSize, self.Param.maxSize)
        obj = self.detection.detectMultiScale(img, self.Param.scaleFactor, self.Param.minNeighbors, self.Param.flags, self.Param.minSize, self.Param.maxSize)
        for x, y, w, h in obj:
            cv.rectangle(img, (x, y), (x+w, y+h), color = self.Param.color, thickness = 2)
        

    

if __name__ == '__main__':

    infile_dir = input("Input directory:")
    outfile_dir = input("Output directory:")
    if not os.path.exists(outfile_dir):
        os.mkdir(outfile_dir)
    files = os.listdir(infile_dir)
    D1 = DisposePic(r"gap_data\cascade.xml", (1.001, 7, 0, (10, 10), (100, 100),(0, 0, 255)))             # 红色-裂缝
    D2 = DisposePic(r"sunken_data\cascade.xml", (1.001, 12, 0, (10, 10), (100, 100), (0, 255, 255)))      # 黄色-沉降
    D3 = DisposePic(r"web_data\cascade.xml", (1.002, 13, 0, (10, 10), (100, 100), (255, 0, 0)))           # 蓝色-网裂
    disposePics = [D1, D2, D3]

    count = 0
    
    for file in files:
        if file.endswith(".jpg"):
            count += 1
            dir_file = os.path.join(infile_dir, file)
            print(f"{count}:Opening {file}...")
            img = cv.imread(dir_file)
            for dis in disposePics:
                dis.dispose(img)
            cv.imshow(str(count), img)
            WaitEsc(cv)
            cv.imwrite(os.path.join(outfile_dir, file), img)
            print(f"\t{file} Saved.")
            
