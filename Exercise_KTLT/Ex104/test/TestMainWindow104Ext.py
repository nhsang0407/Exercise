from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex104.ui.MainWindow104Ext import MainWindow104Ext

app=QApplication([])
mywindow= MainWindow104Ext()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()