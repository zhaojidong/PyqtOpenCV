import cv2,sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from HT_PyOpenCV import Ui_MainWindow
from Function import *
import netifaces
import numpy as  np
from GlobalVriable import *
filePath = r'D:\PythonProject\PythonOpenCV\\'

class HT_PyOpenCV_UI(QMainWindow,Ui_MainWindow):
    global_init()
    def __init__(self,parent=None):#parent=None,so the HaiTu_UI is the topmost window
        super(HT_PyOpenCV_UI,self).__init__(parent)#the super().__init__() excutes the constructor fo father, then we can use the property of father
        self.init()
        print(netifaces.interfaces())

    def init(self):
        self.setupUi(myWindow)
        myWindow.setWindowTitle('海图 PyOpenCV')
        myWindow.setWindowIcon(QIcon('HaiTuLOGO.png'))
        self.buttonORaction()
        self.UI2glv()


    def buttonORaction(self):
        # self.btnDisplayImage.clicked.connect(lambda: self.displayFun())
        self.actionOpen.triggered.connect(lambda: HT_PyOpenCV_UI.openFileEvent(self))
        self.btnDisGray.clicked.connect(lambda: self.UI2glv())
        self.btnDisplayImage.clicked.connect(lambda: self.showImg())

    def showImg(self):
        jpg = QtGui.QPixmap(get_value('FileInfo'))
        self.label.setPixmap(jpg)

    def displayFun(self):
        #ShowImage = QLabel()
        fp = file_create(filePath, 'image_Numpy', '.txt')
        img = cv2.imread("D:/PythonProject/PythonOpenCV/tianzhen.jpeg")#cv2.IMREAD_COLOR/IMREAD_GRAYSCALE/THRESH_BINARY
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #cv2.threshold(img, threshold, maxval,type)图像二值化处理，threshold是设定的阈值，maxval是当灰度值大于（或小于）阈值时将该灰度值赋成的值，type规定的是当前二值化的方式
        ret,img_threshold = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
        pixel = img[100,100]#某点的像素
        self.showInfo(str(pixel))
        self.showInfo(str(img.shape))#返回图像的行数，列数，色彩通道数
        cv2.namedWindow('imag window',cv2.WINDOW_AUTOSIZE)
        cv2.imshow('imag window',img)
        cv2.imshow('other',img_threshold)
        cv2.waitKey(0)
        #self.textEdit.append(pixel)
        cv2.destroyAllWindows()
        np.set_printoptions(threshold=np.inf)#show all numpy data
        fp.write(str(img))
        print(img)

    def UI2glv(self):
        # global_init()
        # setValObj = glv()
        # setValObj.binProThreshold = self.lineEdit_threshold.text()
        # setValObj.binProMaxValue = self.lineEdit_maxVal.text()
        set_value('binProThreshold',self.lineEdit_threshold.text())
        set_value('binProMaxValue',self.lineEdit_maxVal.text())
        print('main_UI2glv')
        # print(setValObj.binProThreshold)
        # print(setValObj.binProMaxValue)
        print(get_value('binProThreshold'))
        print(get_value('binProMaxValue'))
        imgGray()
    def showInfo(self,text):
        self.textEdit.append(text)
        if glv.shouFlag == True:
            self.textEdit.append('Binary Process Threshold:')
            self.textEdit.append(glv.binProThreshold)
            self.textEdit.append('Binary Process Max Value:')
            self.textEdit.append(glv.binProMaxValue)
            glv.shouFlag = False
        # QApplication.processEvents()#reflash the UI to display the message on time
        # cursor = self.textEdit.textCursor()#set the text edit cursor at the end
        # cursor.movePosition(QTextCursor.End)
        # self.textEdit.setTextCursor(cursor)

    def openFileEvent(self):
        FileInfo,_ = QFileDialog.getOpenFileNames(self, 'Open file', 'D:\PythonProject\PythonOpenCV')#return value is tuple type
        FileInfo = ''.join(FileInfo)
        set_value('FileInfo',FileInfo)
        print(get_value('FileInfo'))

class HT_PyOpenCV_subUI(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):#parent=None,so the HaiTu_UI is the topmost window
        super(HT_PyOpenCV_subUI,self).__init__(parent)#the super().__init__() excutes the constructor fo father, then we can use the property of father
        self.init()

    def init(self):
        self.setupUi(myWindow)
        self.btn_grayImg.clicked.connect(lambda:self.textEdit.append('123'))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QMainWindow()
    ht = HT_PyOpenCV_UI()
    myWindow.show()
    sys.exit(app.exec_())

