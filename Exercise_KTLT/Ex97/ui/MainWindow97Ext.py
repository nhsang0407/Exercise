from PyQt6.QtWidgets import QInputDialog, QMessageBox

from Exercise_KTLT.Ex97.ui.MainWindow97 import Ui_MainWindow


class MainWindow97Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonAdd.clicked.connect(self.add_item)
        self.pushButtonUpdate.clicked.connect(self.update_item)
        self.pushButtonInsert.clicked.connect(self.insert_item)
        self.pushButtonRemove.clicked.connect(self.remove_item)
        self.pushButtonClear.clicked.connect(self.clear_all)
        self.listWidget.itemClicked.connect(self.processItemClicked)
        self.listWidget.itemSelectionChanged.connect(self.processItemSelectionChanged)
        self.listWidget.itemDoubleClicked.connect(self.processItemDoubleClicked)

    def add_item(self):
        text,ok=QInputDialog.getText(self.MainWindow, "Add new item", "New item: ")
        if text and ok:
            self.listWidget.addItem(text)
    def update_item(self):
        current_row=self.listWidget.currentRow()
        if current_row>=0:
            item=self.listWidget.item(current_row)
            text, ok = QInputDialog.getText(self.MainWindow, "Update the item", "New data: ",
                                            text=item.text())
            if text and ok:
                item.setText(text)
    def insert_item(self):
        current_row=self.listWidget.currentRow()
        if current_row>=0:
            text,ok=QInputDialog.getText(self.MainWindow, "Insert new item", "New item: ")
            if text and ok:
                self.listWidget.insertItem(current_row+1,text)
    def remove_item(self):
        current_row=self.listWidget.currentRow()
        if current_row >= 0:
            item=self.listWidget.item(current_row)
            msg=QMessageBox()
            msg.setWindowTitle("Remove Item")
            msg.setText(f"Do you want to remove {item.text()}?")
            msg.setIcon(QMessageBox.Icon.Question)
            buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
            msg.setStandardButtons(buttons)
            result=msg.exec()
            if result==QMessageBox.StandardButton.Yes:
                current_item=self.listWidget.takeItem(current_row)
                del current_item
    def clear_all(self):
        answer=QMessageBox.question(self.MainWindow, "Clear All", "Are you sure to clear?",
                           QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        if answer==QMessageBox.StandardButton.Yes:
            self.listWidget.clear()

    def processItemSelectionChanged(self):
        current_row = self.listWidget.currentRow()
        item = self.listWidget.item(current_row)
        self.MainWindow.setWindowTitle(item.text())

    def processItemClicked(self):
        current_row = self.listWidget.currentRow()
        data = self.listWidget.item(current_row)
        print("itemClicked=", data.text())

    def processItemDoubleClicked(self):
        self.update_item()