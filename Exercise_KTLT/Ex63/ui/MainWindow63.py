# Form implementation generated from reading ui file 'C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex63\ui\MainWindow63.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 485)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 321, 361))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 299, 326))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 331, 41))
        self.label.setStyleSheet("color: rgb(170, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 70, 271, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 47, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditId = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditId.setGeometry(QtCore.QRect(80, 30, 171, 20))
        self.lineEditId.setObjectName("lineEditId")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 47, 21))
        self.label_3.setObjectName("label_3")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditName.setGeometry(QtCore.QRect(80, 70, 171, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 47, 21))
        self.label_4.setObjectName("label_4")
        self.lineEditPrice = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditPrice.setGeometry(QtCore.QRect(80, 110, 171, 20))
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 47, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditDiscount = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditDiscount.setGeometry(QtCore.QRect(80, 150, 171, 20))
        self.lineEditDiscount.setObjectName("lineEditDiscount")
        self.radioButtonOfficial = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonOfficial.setGeometry(QtCore.QRect(80, 190, 61, 21))
        self.radioButtonOfficial.setObjectName("radioButtonOfficial")
        self.radioButtonNotOfficial = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonNotOfficial.setGeometry(QtCore.QRect(170, 190, 81, 21))
        self.radioButtonNotOfficial.setObjectName("radioButtonNotOfficial")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonSave.setGeometry(QtCore.QRect(80, 220, 61, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonRemove.setGeometry(QtCore.QRect(184, 220, 61, 23))
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 340, 271, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonFilterPrice = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilterPrice.setGeometry(QtCore.QRect(150, 30, 81, 23))
        self.pushButtonFilterPrice.setObjectName("pushButtonFilterPrice")
        self.pushButtonSearchName = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearchName.setGeometry(QtCore.QRect(20, 30, 91, 23))
        self.pushButtonSearchName.setObjectName("pushButtonSearchName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 22))
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
        self.groupBox.setTitle(_translate("MainWindow", "Products:"))
        self.label.setText(_translate("MainWindow", "Product Management"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Product Details:"))
        self.label_2.setText(_translate("MainWindow", "Id:"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Price:"))
        self.label_5.setText(_translate("MainWindow", "Discount:"))
        self.radioButtonOfficial.setText(_translate("MainWindow", "Official"))
        self.radioButtonNotOfficial.setText(_translate("MainWindow", "Not Official"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.groupBox_3.setTitle(_translate("MainWindow", "More functions:"))
        self.pushButtonFilterPrice.setText(_translate("MainWindow", "Filter Price"))
        self.pushButtonSearchName.setText(_translate("MainWindow", "Search Name"))
