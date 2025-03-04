from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex117.ui.MainWindow117Ext import MainWindow117Ext

app=QApplication([])
mywindow= MainWindow117Ext()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()