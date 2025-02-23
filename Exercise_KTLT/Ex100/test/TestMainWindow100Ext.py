from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex100.ui.MainWindow100Ext import MainWindow100Ext

app=QApplication([])
mywindow= MainWindow100Ext()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()