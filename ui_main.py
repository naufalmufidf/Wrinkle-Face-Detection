# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainslOogu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1229, 888)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.shadow = QFrame(self.centralwidget)
        self.shadow.setObjectName(u"shadow")
        self.shadow.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(45, 48, 55);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.shadow.setFrameShape(QFrame.StyledPanel)
        self.shadow.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.shadow)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1211, 141))
        self.widget_2.setStyleSheet(u"border-top-left-radius : 10px;\n"
"border-top-right-radius : 10px;\n"
"background-color: #E7B18E;")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 30, 971, 101))
        font = QFont()
        font.setFamily(u"Casta Thin")
        font.setPointSize(68)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: E7B18E;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.btn_close = QPushButton(self.widget_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(30, 20, 18, 18))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"background: #FF605C;\n"
"border-radius: 9%;")
        self.btn_minimize = QPushButton(self.widget_2)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(60, 20, 18, 18))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"background: #FFBD44;\n"
"border-radius: 9%;")
        self.btn_gtw = QPushButton(self.widget_2)
        self.btn_gtw.setObjectName(u"btn_gtw")
        self.btn_gtw.setGeometry(QRect(90, 20, 18, 18))
        self.btn_gtw.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gtw.setStyleSheet(u"background: #00CA4E;\n"
"border-radius: 9%;")
        self.label = QLabel(self.shadow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 260, 381, 381))
        self.label.setStyleSheet(u"border: 2px solid;\n"
"border-color: rgb(231, 177, 142);")
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(self.shadow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(760, 260, 381, 381))
        self.label_2.setStyleSheet(u"border: 2px solid;\n"
"border-color: rgb(231, 177, 142);")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_4 = QLabel(self.shadow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 180, 101, 61))
        font1 = QFont()
        font1.setFamily(u"Gramatika-Medium")
        font1.setPointSize(24)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #E7B18E;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.shadow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(890, 170, 121, 71))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #E7B18E;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.shadow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(770, 610, 151, 16))
        font2 = QFont()
        font2.setFamily(u"Gramatika-Medium")
        font2.setPointSize(12)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color:rgb(45, 48, 55);\n"
"color: #E7B18E;")
        self.btn_loadImage = QPushButton(self.shadow)
        self.btn_loadImage.setObjectName(u"btn_loadImage")
        self.btn_loadImage.setGeometry(QRect(170, 690, 181, 51))
        font3 = QFont()
        font3.setFamily(u"Gramatika-Medium")
        font3.setPointSize(10)
        self.btn_loadImage.setFont(font3)
        self.btn_loadImage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_loadImage.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 20px;")
        self.btn_saveImage = QPushButton(self.shadow)
        self.btn_saveImage.setObjectName(u"btn_saveImage")
        self.btn_saveImage.setGeometry(QRect(860, 690, 181, 51))
        self.btn_saveImage.setFont(font3)
        self.btn_saveImage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saveImage.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 20px;")
        self.btn_process = QPushButton(self.shadow)
        self.btn_process.setObjectName(u"btn_process")
        self.btn_process.setGeometry(QRect(510, 430, 181, 51))
        self.btn_process.setFont(font3)
        self.btn_process.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_process.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 20px;")

        self.gridLayout.addWidget(self.shadow, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Wrinkles Face Detection", None))
        self.btn_close.setText("")
        self.btn_minimize.setText("")
        self.btn_gtw.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_6.setText("")
        self.btn_loadImage.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.btn_saveImage.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.btn_process.setText(QCoreApplication.translate("MainWindow", u"Process", None))
    # retranslateUi

