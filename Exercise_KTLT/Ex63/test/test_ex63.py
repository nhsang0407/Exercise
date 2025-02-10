from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex63.ui.MainWindow63Ex import MainWindow63Ex

app=QApplication([])
mywindow= MainWindow63Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


