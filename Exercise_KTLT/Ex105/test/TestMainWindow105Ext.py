from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex105.ui.MainWindow105Ext import MainWindow105Ext

app=QApplication([])
mywindow= MainWindow105Ext()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()