from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex118.EX118.ui.MainWindow118Ext import MainWindow118Ext

app=QApplication([])
mywindow= MainWindow118Ext()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()