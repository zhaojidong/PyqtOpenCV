from HT_PyOpenCV import Ui_MainWindow
from main import HT_PyOpenCV_UI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2,sys,numpy as np
from GlobalVriable import *
from GlobalVriable import globalValue as glv

filePath = r'D:\PythonProject\PythonOpenCV\\'

def file_create(path,name,type):
    full_path = path + name + type
    file = open(full_path,'w')
    #file.close()
    print(name,type,' File Creat Done',sep='')
    return file

def imgPreHandle():
    # get_value('FileInfo')
    # glv().debugPrint(glv.FileInfo)
    fp = file_create(filePath, 'image_Numpy', '.txt')
    try:
        img = cv2.imread(get_value('FileInfo'))# cv2.IMREAD_COLOR/IMREAD_GRAYSCALE/THRESH_BINARY
    except:
        print()
    return fp, img
    pass

def imgGray():
    # glv.shouFlag = True
    # # ShowImage = QLabel()

    fp,img = imgPreHandle()
    img_color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # # # cv2.threshold(img, threshold, maxval,type)图像二值化处理，threshold是设定的阈值，maxval是当灰度值大于（或小于）阈值时将该灰度值赋成的值，type规定的是当前二值化的方式
    # ret, img_threshold = cv2.threshold(img_color, get_value('binProThreshold'), get_value('binProMaxValue'), cv2.THRESH_BINARY)
    # print('Function_imgGray')
    # # # getValObj = glv()
    # print(get_value('binProThreshold'))
    # print(get_value('binProMaxValue'))
    # pixel = img[100, 100]  # 某点的像素
    # # # # self.showInfo(str(pixel))
    # # # # self.showInfo(str(img.shape))  # 返回图像的行数，列数，色彩通道数
    # cv2.namedWindow('BinaryProcess', cv2.WINDOW_AUTOSIZE)
    # # # #cv2.imshow('imag window', img)
    # cv2.imshow('BinaryProcess', img_threshold)
    # cv2.waitKey(0)
    # # # # self.textEdit.append(pixel)
    # cv2.destroyAllWindows()
    # np.set_printoptions(threshold=np.inf)  # show all numpy data
    # fp.write(str(img))
    pass

def dispalyOriginalPicture():
    fp,img = imgPreHandle()
    img_color = cv2.cvtColor(img, cv2.IMREAD_COLOR)
    pass
