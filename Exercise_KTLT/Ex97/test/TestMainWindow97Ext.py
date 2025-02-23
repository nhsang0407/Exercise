from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex97.ui.MainWindow97Ext import MainWindow97Ext

app=QApplication([])
mywindow= MainWindow97Ext()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


