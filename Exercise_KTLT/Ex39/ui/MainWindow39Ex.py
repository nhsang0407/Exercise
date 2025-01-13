import functools
import random

from PyQt6.QtWidgets import QPushButton

from Exercise_KTLT.Ex39.ui.MainWindow39 import Ui_MainWindow


class MainWindow39Ex(Ui_MainWindow):
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
        self.pushButtonDelete.clicked.connect(self.delete)
        self.pushButtonUpdate.clicked.connect(self.update)
        self.pushButtonAscSort.clicked.connect(self.asc_sort)
        self.pushButtonDescSort.clicked.connect(self.desc_sort)
        self.pushButtonRemoveAll.clicked.connect(self.remove_all)
    def random(self):
        n=int(self.lineEditNumber.text())
        self.list.clear()
        for i in range(n):
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
        self.lineEditNumber.setText(f"{self.list[i]}")
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
        x=random.randint(0,11)
        self.list.append(x)
        self.draw_button_into_box()
    def delete(self):
        if self.selected_index==-1:
            return
        self.list.pop(self.selected_index)
        self.draw_button_into_box()
    def update(self):
        if self.selected_index == -1:
            return
        x=self.list[self.selected_index]
        x=x//10
        self.list[self.selected_index]=x
        self.draw_button_into_box()
    def asc_sort(self):
        self.list.sort(reverse=False)
        self.draw_button_into_box()
    def desc_sort(self):
        self.list.sort(reverse=True)
        self.draw_button_into_box()
    def remove_all(self):
        self.lineEditNumber.clear()
        self.clearLayout(self.verticalLayout)
