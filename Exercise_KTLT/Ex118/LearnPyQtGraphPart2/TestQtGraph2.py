from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex118.LearnPyQtGraphPart2.MainWindowQtGraph2Ext import MainWindowQtGraph2Ext

app=QApplication([])
mywindow= MainWindowQtGraph2Ext()
mywindow.setupUi(QMainWindow())
mywindow.show()
app.exec()