from Exercise_KTLT.Ex21.libs.function_libs import A, C
from Exercise_KTLT.Ex21.ui.MainWindowEx21 import Ui_MainWindow


class MainWindowEx21Ext(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonExecute.clicked.connect(self.process_result)
    def process_result(self):
        n=int(self.lineEditN.text())
        k=int(self.lineEditK.text())
        a=A(n,k)
        c=C(n,k)
        self.lineEditA.setText(f"{a}")
        self.lineEditC.setText(f"{c}")