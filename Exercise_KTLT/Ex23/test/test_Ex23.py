from PyQt6.QtWidgets import QApplication, QMainWindow
from Exercise_KTLT.Ex23.ui.MainWindow23Ex import MainWindow23Ex

app=QApplication([])
mywindow= MainWindow23Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


