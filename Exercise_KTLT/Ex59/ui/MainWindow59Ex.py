from PyQt6.QtWidgets import QMessageBox

from Exercise_KTLT.Ex59.libs.Fraction import Fraction
from Exercise_KTLT.Ex59.ui.MainWindow59 import Ui_MainWindow


class MainWindow59Ex(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonPlus.clicked.connect(self.process_add)
        self.pushButtonMinus.clicked.connect(self.process_minus)
        self.pushButtonMultiplier.clicked.connect(self.process_multiply)
        self.pushButtonDivide.clicked.connect(self.process_divide)
    
    def get_fraction(self):
        tu1=int(self.lineEditTu1.text())
        mau1=int(self.lineEditMau1.text())
        tu2=int(self.lineEditTu2.text())
        mau2=int(self.lineEditMau2.text())
        if mau1!=0 and mau2!=0:
            ps1=Fraction(tu1,mau1)
            ps2=Fraction(tu2,mau2)
            return ps1,ps2
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("ERROR")
        dlg.setText("Denominator can not equal 0")
        dlg.setIcon(QMessageBox.Icon.Warning)
        dlg.exec()
        self.MainWindow.close()
    def process_add(self):
        ps1,ps2=self.get_fraction()
        ps3=ps1.add(ps2)
        self.lineEditTu3.setText(f"{ps3.numerator}")
        self.lineEditMau3.setText(f"{ps3.denominator}")

    def process_minus(self):
        ps1, ps2 = self.get_fraction()
        ps3 = ps1.minus(ps2)
        self.lineEditTu3.setText(f"{ps3.numerator}")
        self.lineEditMau3.setText(f"{ps3.denominator}")

    def process_multiply(self):
        ps1, ps2 = self.get_fraction()
        ps3 = ps1.multiply(ps2)
        self.lineEditTu3.setText(f"{ps3.numerator}")
        self.lineEditMau3.setText(f"{ps3.denominator}")

    def process_divide(self):
        ps1, ps2 = self.get_fraction()
        if ps2.numerator==0:
            dlg = QMessageBox(self.MainWindow)
            dlg.setWindowTitle("ERROR")
            dlg.setText("Fraction 2 can not have 0 in numerator")
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
        else:
            ps3 = ps1.divide(ps2)
            self.lineEditTu3.setText(f"{ps3.numerator}")
            self.lineEditMau3.setText(f"{ps3.denominator}")