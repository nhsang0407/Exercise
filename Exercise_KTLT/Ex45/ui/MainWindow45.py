# Form implementation generated from reading ui file 'C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex45\ui\MainWindow45.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 528)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 631, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 301, 421))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 281, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutBook = QtWidgets.QVBoxLayout()
        self.verticalLayoutBook.setObjectName("verticalLayoutBook")
        self.verticalLayout_3.addLayout(self.verticalLayoutBook)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 50, 301, 301))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditISBN = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditISBN.setGeometry(QtCore.QRect(80, 30, 201, 20))
        self.lineEditISBN.setObjectName("lineEditISBN")
        self.lineEditTitle = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditTitle.setGeometry(QtCore.QRect(80, 80, 201, 20))
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEditYear = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditYear.setGeometry(QtCore.QRect(80, 180, 201, 20))
        self.lineEditYear.setObjectName("lineEditYear")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditAuthor = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditAuthor.setGeometry(QtCore.QRect(80, 130, 201, 20))
        self.lineEditAuthor.setObjectName("lineEditAuthor")
        self.lineEditPublisher = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditPublisher.setGeometry(QtCore.QRect(80, 230, 201, 20))
        self.lineEditPublisher.setObjectName("lineEditPublisher")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 230, 71, 21))
        self.label_6.setObjectName("label_6")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonSave.setGeometry(QtCore.QRect(90, 270, 75, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonRemove.setGeometry(QtCore.QRect(200, 270, 75, 23))
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 370, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonSearch_Title = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearch_Title.setGeometry(QtCore.QRect(10, 30, 121, 23))
        self.pushButtonSearch_Title.setObjectName("pushButtonSearch_Title")
        self.pushButtonFilter_Year = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilter_Year.setGeometry(QtCore.QRect(160, 30, 121, 23))
        self.pushButtonFilter_Year.setObjectName("pushButtonFilter_Year")
        self.pushButtonSearch_ISBN = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearch_ISBN.setGeometry(QtCore.QRect(10, 70, 121, 23))
        self.pushButtonSearch_ISBN.setObjectName("pushButtonSearch_ISBN")
        self.pushButtonFilter_Publisher = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilter_Publisher.setGeometry(QtCore.QRect(160, 70, 121, 23))
        self.pushButtonFilter_Publisher.setObjectName("pushButtonFilter_Publisher")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 22))
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
        self.label.setText(_translate("MainWindow", "Book managements"))
        self.groupBox.setTitle(_translate("MainWindow", "Books:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Books Details:"))
        self.label_2.setText(_translate("MainWindow", "ISBN:"))
        self.label_3.setText(_translate("MainWindow", "Title:"))
        self.label_4.setText(_translate("MainWindow", "Year:"))
        self.label_5.setText(_translate("MainWindow", "Author:"))
        self.label_6.setText(_translate("MainWindow", "Publisher:"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.groupBox_3.setTitle(_translate("MainWindow", "More functions:"))
        self.pushButtonSearch_Title.setText(_translate("MainWindow", "Search Title"))
        self.pushButtonFilter_Year.setText(_translate("MainWindow", "Filter Years"))
        self.pushButtonSearch_ISBN.setText(_translate("MainWindow", "Search ISBN"))
        self.pushButtonFilter_Publisher.setText(_translate("MainWindow", "Filter Publisher"))
