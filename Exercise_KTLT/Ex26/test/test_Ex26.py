from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex26.ui.MainWindow26Ex import MainWindow26Ex

app=QApplication([])
mywindow= MainWindow26Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


