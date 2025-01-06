from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex33.ui.MainWindow33Ex import MainWindow33Ex

app=QApplication([])
mywindow= MainWindow33Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


