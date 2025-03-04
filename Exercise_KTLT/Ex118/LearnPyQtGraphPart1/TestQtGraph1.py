from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex118.LearnPyQtGraphPart1.MainWindowQtGraph1Ext import MainWindowQtGraph1Ext

app=QApplication([])
mywindow= MainWindowQtGraph1Ext()
mywindow.setupUi(QMainWindow())
mywindow.show()
app.exec()