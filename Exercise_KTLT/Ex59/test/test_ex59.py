from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex59.ui.MainWindow59Ex import MainWindow59Ex

app=QApplication([])
mywindow= MainWindow59Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()