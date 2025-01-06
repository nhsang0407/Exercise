from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex22.ui.MainWindow22Ex import MainWindow22Ex

app=QApplication([])
mywindow= MainWindow22Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()