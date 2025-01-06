from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex24.ui.MainWindow24Ex import MainWindow24Ex

app=QApplication([])
mywindow= MainWindow24Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()