import json
import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from Exercise_KTLT.Ex100.models.Employee import Employee
from Exercise_KTLT.Ex100.ui.MainWindow100 import Ui_MainWindow


class MainWindow100Ext(Ui_MainWindow):
    def __init__(self):
        self.dataset=[]
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonNew.clicked.connect(self.processNew)
        self.readEmployeeFromJson()
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonDelete.clicked.connect(self.processDelete)
        self.pushButtonClose.clicked.connect(self.processClose)
        self.listWidgetEmployee.itemSelectionChanged.connect(self.process_itemSelectionChanged)

    def processNew(self):
        self.lineEditName.clear()
        self.lineEditEmail.clear()
        self.lineEditName.setFocus()
        #Tat che de tu dong loai tru nha
        self.radioButtonWoman.setAutoExclusive(False)
        self.radioButtonMan.setAutoExclusive(False)
        #Chinh button ve unchecked
        self.radioButtonMan.setChecked(False)
        self.radioButtonWoman.setChecked(False)
        #Bat che de tu dong loai tru nha
        self.radioButtonWoman.setAutoExclusive(True)
        self.radioButtonMan.setAutoExclusive(True)

    def writeEmployeeToJson(self):
        dataset = []
        for i in range(0, self.listWidgetEmployee.count()):
            item = self.listWidgetEmployee.item(i)
            emp = item.data(Qt.ItemDataRole.UserRole)
            dataset.append(emp)
        jsonString = json.dumps([emp.__dict__ for emp in dataset])
        jsonFile = open(r"C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex100\database/database.json", "w",encoding='utf-8')
        jsonFile.write(jsonString)
        jsonFile.close()

    def readEmployeeFromJson(self):
        if os.path.isfile(r"C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex100\database/database.json") == False:
            return
        file = open(r"C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex100\database/database.json", "r", encoding='utf-8')
        # Reading from file
        self.dataset = json.loads(file.read(), object_hook=lambda d: Employee(**d))
        file.close()
        for emp in self.dataset:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, emp)
            item.setText(str(emp))
            item.setCheckState(Qt.CheckState.Unchecked)
            if emp.gender == True:
                item.setIcon(QIcon(r"C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex100\images\ic_woman.png"))
            else:
                item.setIcon(QIcon(r"C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex100\images\ic_man.png"))
            self.listWidgetEmployee.addItem(item)

    def processSave(self):
        insertEmployee=Employee(self.lineEditName.text(),self.lineEditEmail.text(),self.radioButtonWoman.isChecked())
        isDuplicated=False
        for i in range(0,self.listWidgetEmployee.count()):
            item=self.listWidgetEmployee.item(i)
            data=item.data(Qt.ItemDataRole.UserRole)
            if insertEmployee.email.lower()==data.email.lower():
                isDuplicated=True
                break
        if not isDuplicated:
            item=QListWidgetItem()
        item.setData(Qt.ItemDataRole.UserRole, insertEmployee)
        item.setText(str(insertEmployee))
        item.setCheckState(Qt.CheckState.Unchecked)
        if self.radioButtonWoman.isChecked():
            item.setIcon(QIcon(r"C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex100\images\ic_woman.png"))
        else:
            item.setIcon(QIcon(r"C:\Users\Hoàng Sang\Documents\TMĐT HK4\1.Kĩ thuật lập trình\Pycharm-KTLT\Exercise_KTLT\Ex100\images\ic_man.png"))
        if not isDuplicated:
            self.listWidgetEmployee.addItem(item)
        self.writeEmployeeToJson()

    def processDelete(self):
        answer=QMessageBox.question(self.MainWindow, "Delete",
                                    "Do you want to delete checked employees?",
                                    QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        if answer==QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidgetEmployee.count()-1,-1,-1):
            item=self.listWidgetEmployee.item(index)
            if item.checkState()==Qt.CheckState.Checked:
                current_item=self.listWidgetEmployee.takeItem(index)
                del current_item
        self.processNew()
        self.writeEmployeeToJson()

    def processClose(self):
        msg=QMessageBox()
        msg.setWindowTitle("Exit Confirmation")
        msg.setText("Are you sure to exit?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        result=msg.exec()
        if result==QMessageBox.StandardButton.Yes:
            self.MainWindow.close()

    def process_itemSelectionChanged(self):
        current_row=self.listWidgetEmployee.currentRow()
        if current_row<0:
            return
        item=self.listWidgetEmployee.item(current_row)
        emp=item.data(Qt.ItemDataRole.UserRole)
        self.lineEditName.setText(emp.name)
        self.lineEditEmail.setText(emp.email)
        if emp.gender==True:
            self.radioButtonWoman.setChecked(True)
        else:
            self.radioButtonMan.setChecked(True)