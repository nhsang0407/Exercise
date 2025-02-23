from PyQt6.QtWidgets import QMessageBox, QMainWindow

from Exercise_KTLT.Ex85.libs.DataConnector import DataConnector
from Exercise_KTLT.Ex85.ui.AssetMainWindowEx import AssetMainWindowEx
from Exercise_KTLT.Ex85.ui.MainWindowLogin85 import Ui_MainWindow


class MainWindowLogin85Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
    def process_login(self):
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        dc = DataConnector()
        emp = dc.login(uid, pwd)
        if emp is None:
            self.msg=QMessageBox(self.MainWindow)
            self.msg.setText("Login Failed!")
            self.msg.exec()
        else:
            self.MainWindow.close() #close man hinh login
            self.mywindow = AssetMainWindowEx()
            self.mywindow.setupUi(QMainWindow())
            self.mywindow.showWindow()
            """
            self.MainWindow.close()
            self.mainwindow=QMainWindow()
            self.myui=AssetMainWindowEx()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()"""
