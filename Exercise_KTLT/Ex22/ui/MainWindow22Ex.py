from Exercise_KTLT.Ex22.libs.Ex22_function import H
from Exercise_KTLT.Ex22.ui.MainWindow22 import Ui_MainWindow


class MainWindow22Ex(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalculate.clicked.connect(self.process_result)
    def process_result(self):
        N=int(self.lineEditTotalBulb.text())
        D=int(self.lineEditDamaged.text())
        M=int(self.lineEditPicked.text())
        p=H(N,D,M)
        self.lineEditProbability.setText(f"{p}")