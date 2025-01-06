from PyQt6.QtWidgets import QMessageBox

from Exercise_KTLT.Ex23.ui.MainWindow23 import Ui_MainWindow


class MainWindow23Ex(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
        self.revenue=0
        self.total_cus=0
        self.total_stu=0
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSell.clicked.connect(self.new_selling)
        self.pushButtonCalculate.clicked.connect(self.calculate)
        self.pushButtonStatistic.clicked.connect(self.statistic)
        self.pushButtonExit.clicked.connect(self.exit)

    def check_name(self):
        msg = QMessageBox(self.MainWindow)
        msg.setWindowTitle("Warning")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Customer name cannot be entered empty")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def check_positive(self):
        msg = QMessageBox(self.MainWindow)
        msg.setWindowTitle("Warning")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("The number of books is a positive integer")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def new_selling(self):
        self.lineEditName.clear()
        self.lineEditQuantity.clear()
        self.lineEditPayment.clear()
        self.checkBoxStudent.setChecked(False)
        self.lineEditName.setFocus()

    def calculate(self):
        if self.lineEditName.text()=="":
            self.check_name()
        else:
            Q=int(self.lineEditQuantity.text())
            if Q < 0:
                self.check_positive()
            else:
                P = 20000
                payment = Q * P
                if self.checkBoxStudent.isChecked():
                    payment = payment * 0.95
                    self.total_stu=self.total_stu+1
                self.lineEditPayment.setText(f"{payment}")
                self.revenue=self.revenue+payment
                self.total_cus=self.total_cus+1
    def statistic(self):
        self.lineEditRevenue.setText(f"{self.revenue}")
        self.lineEditTotalNumber.setText(f"{self.total_cus}")
        self.lineEditStudentCustom.setText(f"{self.total_stu}")
    def exit(self):
        self.MainWindow.close()