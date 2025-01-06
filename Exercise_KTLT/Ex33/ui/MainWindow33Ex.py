from Exercise_KTLT.Ex33.libs.function_ex33 import random, sum_of_array, count_odd_element, odd_element, find_smallest, \
    double_value, sort_ascending, sort_descending
from Exercise_KTLT.Ex33.ui.MainWindow33 import Ui_MainWindow


class MainWindow33Ex(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonRandom.clicked.connect(self.random)
        self.pushButtonSumArray.clicked.connect(self.sum_array)
        self.pushButtonCountOdd.clicked.connect(self.count_odd)
        self.pushButtonSumOdd.clicked.connect(self.sum_odd)
        self.pushButtonSmallest.clicked.connect(self.smallest)
        self.pushButtonDouble.clicked.connect(self.double)
        self.pushButtonAscending.clicked.connect(self.ascending)
        self.pushButtonDescending.clicked.connect(self.descending)
    def random(self):
        self.arr=random()
        self.labelArray.setText(f"{self.arr}")
    def sum_array(self):
        self.labelResult.setText(f"Sum of Array = {sum_of_array(self.arr)}")
    def count_odd(self):
        self.odd=odd_element(self.arr)
        self.labelResult.setText(f"Number of odd elements: {count_odd_element(self.odd)}")
    def sum_odd(self):
        self.labelResult.setText(f"Sum of Odd Elements = {sum_of_array(self.odd)}")
    def smallest(self):
        self.labelResult.setText(f"Smallest value: {find_smallest(self.arr)}")
    def double(self):
        self.labelResult.setText(f"Doubled value array:  {double_value(self.arr)}")
    def ascending(self):
        self.labelResult.setText(f"Ascending array: {sort_ascending(self.arr)}")
    def descending(self):
        self.labelResult.setText(f"Descending array: {sort_descending(self.arr)}")