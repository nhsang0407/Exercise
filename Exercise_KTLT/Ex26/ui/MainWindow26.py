# Form implementation generated from reading ui file 'C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex26\ui\MainWindow26.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 495)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 361, 71))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 291, 121))
        self.groupBox.setObjectName("groupBox")
        self.lineEditInput = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditInput.setGeometry(QtCore.QRect(10, 20, 271, 91))
        self.lineEditInput.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditInput.setObjectName("lineEditInput")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 80, 291, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.labelOutput = QtWidgets.QLabel(parent=self.groupBox_2)
        self.labelOutput.setGeometry(QtCore.QRect(10, 20, 271, 91))
        self.labelOutput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.labelOutput.setText("")
        self.labelOutput.setObjectName("labelOutput")
        self.pushButtonInput = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonInput.setGeometry(QtCore.QRect(90, 220, 151, 21))
        self.pushButtonInput.setObjectName("pushButtonInput")
        self.pushButtonUpper = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonUpper.setGeometry(QtCore.QRect(90, 260, 151, 23))
        self.pushButtonUpper.setObjectName("pushButtonUpper")
        self.pushButtonLower = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLower.setGeometry(QtCore.QRect(90, 300, 151, 23))
        self.pushButtonLower.setObjectName("pushButtonLower")
        self.pushButtonCountLow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCountLow.setGeometry(QtCore.QRect(80, 340, 171, 21))
        self.pushButtonCountLow.setObjectName("pushButtonCountLow")
        self.pushButtonCountUp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCountUp.setGeometry(QtCore.QRect(420, 220, 161, 21))
        self.pushButtonCountUp.setObjectName("pushButtonCountUp")
        self.pushButtonPrintNumberWPL = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPrintNumberWPL.setGeometry(QtCore.QRect(410, 260, 181, 23))
        self.pushButtonPrintNumberWPL.setObjectName("pushButtonPrintNumberWPL")
        self.pushButtonWordCount = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonWordCount.setGeometry(QtCore.QRect(420, 300, 161, 23))
        self.pushButtonWordCount.setObjectName("pushButtonWordCount")
        self.pushButtonVowel_Consonant = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonVowel_Consonant.setGeometry(QtCore.QRect(420, 340, 161, 23))
        self.pushButtonVowel_Consonant.setObjectName("pushButtonVowel_Consonant")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(290, 390, 81, 31))
        self.pushButtonExit.setObjectName("pushButtonExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Using string process functions</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Input data:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output data:"))
        self.pushButtonInput.setText(_translate("MainWindow", "Input data"))
        self.pushButtonUpper.setText(_translate("MainWindow", "Uppercase"))
        self.pushButtonLower.setText(_translate("MainWindow", "Lowercase"))
        self.pushButtonCountLow.setText(_translate("MainWindow", "Count lowercase characters"))
        self.pushButtonCountUp.setText(_translate("MainWindow", "Count uppercase letters"))
        self.pushButtonPrintNumberWPL.setText(_translate("MainWindow", "Print number of words per line"))
        self.pushButtonWordCount.setText(_translate("MainWindow", "Word count"))
        self.pushButtonVowel_Consonant.setText(_translate("MainWindow", "Print vowels, consonants"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
