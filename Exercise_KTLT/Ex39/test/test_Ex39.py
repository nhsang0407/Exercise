from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex39.ui.MainWindow39Ex import MainWindow39Ex

app=QApplication([])
mywindow= MainWindow39Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


