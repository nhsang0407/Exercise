import functools
import random

from PyQt6.QtWidgets import QPushButton, QMessageBox

from Exercise_KTLT.Ex38.libs.function_38 import check_perfect_number
from Exercise_KTLT.Ex38.ui.MainWindow38 import Ui_MainWindow


class MainWindow38Ex(Ui_MainWindow):
    def __init__(self):
        self.list=[]
        self.selected_index=-1
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonRandom.clicked.connect(self.random)
        self.pushButtonAdd.clicked.connect(self.add)
        self.pushButtonDeleteElement.clicked.connect(self.delete_element)
        self.pushButtonDeleteNegative.clicked.connect(self.delete_negative)
        self.pushButtonDeleteEntire.clicked.connect(self.delete_entire)
        self.pushButtonSortDes.clicked.connect(self.desc_sort)
        self.pushButtonSortAsc.clicked.connect(self.asc_sort)
        self.pushButtonCount.clicked.connect(self.count)
        self.pushButtonCalculate.clicked.connect(self.calculate)
    def random(self):
        self.list.clear()
        for i in range(10):
            x=random.randint(-100,100)
            self.list.append(x)
        self.draw_button_into_box()
    def draw_button_into_box(self):
        self.clearLayout(self.verticalLayout)
        for i in range(len(self.list)):
            x=self.list[i]
            title = f"{x}"
            btn = QPushButton(text=title)
            self.verticalLayout.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail,i))
    def show_detail(self,i):
        self.selected_index=i
        self.lineEditN.setText(f"{self.list[i]}")
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def add(self):
        if self.lineEditN.text()=="":
            msg=QMessageBox(self.MainWindow)
            msg.setWindowTitle("Information")
            msg.setText("You have to enter a number")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
        else:
            n = int(self.lineEditN.text())
            self.list.append(n)
            self.draw_button_into_box()
    def count(self):
        if self.lineEditK.text()=="":
            msg=QMessageBox(self.MainWindow)
            msg.setWindowTitle("Information")
            msg.setText("You have to enter a number")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
        else:
            count = 0
            k=int(self.lineEditK.text())
            for x in self.list:
                if x==k:
                    count=count+1
            self.lineEditK.setText(f"{k} ==> {count}")
    def calculate(self):
        sum=0
        for x in self.list:
            if x>0:
                if check_perfect_number(x):
                    sum=sum+x
        self.lineEditSumPerfect.setText(f"{sum}")
    def delete_element(self):
        if self.selected_index==-1:
            return
        self.list.pop(self.selected_index)
        self.lineEditN.clear()
        self.draw_button_into_box()
    def delete_negative(self):
        for x in self.list[:]:
            if x<0:
                self.list.remove(x)
        self.draw_button_into_box()
    def delete_entire(self):
        self.lineEditN.clear()
        self.lineEditK.clear()
        self.lineEditSumPerfect.clear()
        self.clearLayout(self.verticalLayout)
    def asc_sort(self):
        self.list.sort(reverse=False)
        self.draw_button_into_box()
    def desc_sort(self):
        self.list.sort(reverse=True)
        self.draw_button_into_box()

