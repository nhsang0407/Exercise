from PyQt6.QtWidgets import QApplication, QMainWindow

from Exercise_KTLT.Ex85.ui.MainWindowLogin85Ex import MainWindowLogin85Ex

app=QApplication([])
mywindow= MainWindowLogin85Ex()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()