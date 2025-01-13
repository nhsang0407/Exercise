from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex45.ui.MainWindow45Ex import MainWindow45Ex

app=QApplication([])
mywindow= MainWindow45Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


