import sys
import functools
import platform
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import cv2
import numpy as np
from matplotlib import pyplot as plt

from ui_loading_screen import Ui_Loading
from ui_main import Ui_MainWindow


counter = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Image = None

        self.ui.btn_loadImage.clicked.connect(self.open)
        self.ui.btn_saveImage.clicked.connect(self.save)
        self.ui.btn_process.clicked.connect(self.gas)
        self.ui.btn_close.clicked.connect(self.quit)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.shadow.setGraphicsEffect(self.shadow)

    def eventFilter(self, obj, event):
        if obj is self.w and event.type() == QtCore.QEvent.Close:
            self.quit_app()
            event.ignore()
            return True
        return super(Manager, self).eventFilter(obj, event)

    @QtCore.Slot()
    def quit(self):
        print('CLEAN EXIT')
        self.removeEventFilter(self)
        app.quit()
    
    def open(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        self.Image = cv2.imread(imagePath)
        pixmap = QPixmap(imagePath)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setAlignment(QtCore.Qt.AlignHCenter |
                                QtCore.Qt.AlignVCenter)
        self.ui.label.setScaledContents(True)

    def save(self):
        fname, filter = QFileDialog.getSaveFileName(
            self, 'Save As', 'D:\\', "Image Files (*.jpg)")
        if fname:
            cv2.imwrite(fname, self.Image)
        else:
            print('Error')

    def gas(self):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        img = self.Image

        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.05,minNeighbors=10)
        number_of_edges = 0
        for x,y,w,h in faces : 
            cropped_img = img[y:y+h,x:x+w]
            edges = cv2.Canny(cropped_img,100,1000)
            gbr = cv2.resize(edges, (1080,1920))
            filename = 'pra.jpg'
            cv2.imwrite(filename, gbr)    
            number_of_edges = np.count_nonzero(edges)
            
        if number_of_edges > 1000:
            print("Wrinkle Found ")
            self.ui.label_6.setText("Wrinkle Found")
        else:
            print("No Wrinkle Found ")
            self.ui.label_6.setText("No Wrinkle Found")

        pixmap = QPixmap('pra.jpg')
        self.ui.label_2.setPixmap(pixmap)
        self.ui.label_2.setAlignment(QtCore.Qt.AlignHCenter |
                                QtCore.Qt.AlignVCenter)
        self.ui.label_2.setScaledContents(True)
        




class Loading(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Loading()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.shadow.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        self.ui.label_desc.setText("Hello there!")
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_desc.setText("Preparing..."))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_desc.setText("Nah beres, here you go!"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()
            # self.main.show() del later

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Loading()
    sys.exit(app.exec_())
window.show()
