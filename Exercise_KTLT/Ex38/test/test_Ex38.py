from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex38.ui.MainWindow38Ex import MainWindow38Ex

app=QApplication([])
mywindow= MainWindow38Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


