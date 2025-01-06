from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex21.ui.MainWindowEx21Ext import MainWindowEx21Ext

app=QApplication([])
mywindow= MainWindowEx21Ext()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


