import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from Exercise_KTLT.Ex64.models.OfficialEmployee import OfficialEmployee
from Exercise_KTLT.Ex64.models.StaffManagement import StaffManagement
from Exercise_KTLT.Ex64.models.TemporaryEmployee import TemporaryEmployee
from Exercise_KTLT.Ex64.ui.MainWindow64 import Ui_MainWindow


class MainWindow64Ex(Ui_MainWindow):
    def __init__(self):
        self.sm=StaffManagement()
        self.selected_index=-1
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save_employee)
        self.pushButtonRemove.clicked.connect(self.process_remove_employee)
        self.pushButtonSearchIdCard.clicked.connect(self.process_search_id_card)
        self.pushButtonFilterYear.clicked.connect(self.process_filter_year)

    def process_save_employee(self):
        if self.checkBoxOfficial.isChecked():
            emp=OfficialEmployee()
        else:
            emp=TemporaryEmployee()
        emp.id=self.lineEditID.text()
        emp.name=self.lineEditName.text()
        emp.idcard=self.lineEditIdCard.text()
        emp.birthday=self.lineEditBirhtday.text()
        self.sm.add_employee(emp)
        self.display_employee_layout()
    def display_employee_layout(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.sm.database)):
            x=self.sm.database[i]
            title = f"{x.id}-{x.name}-{x.birthday}"
            btn = QPushButton(text=title)
            if isinstance(x,OfficialEmployee):
                btn.setStyleSheet("background-color: rgb(217,124,209)")
            else:
                btn.setStyleSheet("background-color: rgb(188,207,243)")
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail,i))
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def show_detail(self,i):
        self.selected_index=i
        emp=self.sm.database[i]
        self.lineEditID.setText(f"{emp.id}")
        self.lineEditName.setText(f"{emp.name}")
        self.lineEditIdCard.setText(f"{emp.idcard}")
        self.lineEditBirhtday.setText(f"{emp.birthday}")

    def process_remove_employee(self):
        if self.selected_index==-1:
            return
        if self.ask_remove():
            self.sm.database.pop(self.selected_index)
            self.display_employee_layout()

    def ask_remove(self):
        msg=QMessageBox(self.MainWindow)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Do you want to delete the employee?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        button = msg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False

    def process_search_id_card(self):
        id_card = self.lineEditIdCard.text()
        if not id_card:
            QMessageBox.warning(self.MainWindow, "Warning", "Please enter an ID Card number.")
            return
        for emp in self.sm.database:
            if id_card == emp.idcard:
                self.lineEditID.setText(f"{emp.id}")
                self.lineEditName.setText(f"{emp.name}")
                self.lineEditIdCard.setText(f"{emp.idcard}")
                self.lineEditBirhtday.setText(f"{emp.birthday}")
                return
        QMessageBox.warning(self.MainWindow, "Warning", "Not found ID Card")

    def process_filter_year(self):
        year = self.lineEditBirhtday.text()
        if not year.isdigit():
            QMessageBox.warning(self.MainWindow, "Warning", "Please enter a valid year.")
            return
        filtered_employees = []
        for emp in self.sm.database:
            if emp.birthday.endswith(year):
                filtered_employees.append(emp)

        self.clearLayout(self.verticalLayoutButton)

        if not filtered_employees:
            QMessageBox.information(self.MainWindow, "No Results", f"No employees found born in {year}.")
            return

        for i in range(len(filtered_employees)):
            emp = filtered_employees[i]
            title = f"{emp.id} - {emp.name} - {emp.birthday}"
            btn = QPushButton(text=title)
            btn.setStyleSheet("background-color: rgb(217,124,209)" if isinstance(emp,
                                                                                 OfficialEmployee) else "background-color: rgb(188,207,243)")
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))
