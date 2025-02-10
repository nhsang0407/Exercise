from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex64.ui.MainWindow64Ex import MainWindow64Ex

app=QApplication([])
mywindow= MainWindow64Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()


