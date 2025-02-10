import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from Exercise_KTLT.Ex63.models.NonOfficialProduct import NonOfficialProduct
from Exercise_KTLT.Ex63.models.OfficialProduct import OfficialProduct
from Exercise_KTLT.Ex63.models.ProductManagement import ProductManagement
from Exercise_KTLT.Ex63.ui.MainWindow63 import Ui_MainWindow


class MainWindow63Ex(Ui_MainWindow):
    def __init__(self):
        self.pm=ProductManagement()
        self.selected_index=-1
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save_product)
        self.pushButtonRemove.clicked.connect(self.process_remove_product)
        self.pushButtonSearchName.clicked.connect(self.process_search_name)
        self.pushButtonFilterPrice.clicked.connect(self.process_filter_price)

    def check_duplicated_id(self,id):
        for product in self.pm.list_product:
            if product.id==id:
                return True
        return False

    def process_save_product(self):
        if self.radioButtonOfficial.isChecked():
            product=OfficialProduct()
        elif self.radioButtonNotOfficial.isChecked():
            product=NonOfficialProduct()
        else:
            QMessageBox.warning(self.MainWindow, "Error", "Please select type of product")
            return
        product.id=self.lineEditId.text()
        product.name=self.lineEditName.text()
        product.price=self.lineEditPrice.text()
        product.discount=self.lineEditDiscount.text()
        if not self.check_duplicated_id(product.id):
            self.pm.addproduct(product)
        else:
            for p in self.pm.list_product:
                if p.id == product.id:
                    p.name = product.name
                    p.price = product.price
                    p.discount = product.discount
                    break
        self.display_product_layout()

    def display_product_layout(self):
        self.clearLayout(self.verticalLayout)
        for i in range(len(self.pm.list_product)):
            x = self.pm.list_product[i]
            title = f"{x.id}-{x.name}-{x.price}"
            btn = QPushButton(text=title)
            if isinstance(x, OfficialProduct):
                btn.setStyleSheet("background-color: rgb(217,124,209)")
            else:
                btn.setStyleSheet("background-color: rgb(188,207,243)")
            self.verticalLayout.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def show_detail(self, i):
        self.selected_index = i
        product = self.pm.list_product[i]
        self.lineEditId.setText(f"{product.id}")
        self.lineEditName.setText(f"{product.name}")
        self.lineEditPrice.setText(f"{product.price}")
        self.lineEditDiscount.setText(f"{product.discount}")

    def process_remove_product(self):
        if self.selected_index==-1:
            return
        self.pm.list_product.pop(self.selected_index)
        self.display_product_layout()

    def process_search_name(self):
        name = self.lineEditName.text()
        if not name:
            QMessageBox.warning(self.MainWindow, "Warning", "Please enter a name.")
            return
        for product in self.pm.list_product:
            if name == product.name:
                self.lineEditName.setText(f"{product.name}")
                self.lineEditId.setText(f"{product.id}")
                self.lineEditPrice.setText(f"{product.price}")
                self.lineEditDiscount.setText(f"{product.discount}")
                return
        QMessageBox.warning(self.MainWindow, "Warning", "Not found name")

    def process_filter_price(self):
        try:
            price = float(self.lineEditPrice.text())
            if not price:
                QMessageBox.warning(self.MainWindow, "Warning", "Please enter a price")
                return
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi nhập liệu", "Enter valid price")
            return
        filtered_products = [p for p in self.pm.list_product if float(p.price) == price]

        self.clearLayout(self.verticalLayout)
        for i in range(len(filtered_products)):
            product = filtered_products[i]
            title = f"{product.id}-{product.name}-{product.price}"
            btn = QPushButton(text=title)
            btn.setStyleSheet("background-color: rgb(217,124,209)" if isinstance(product,
                                                                                 OfficialProduct) else "background-color: rgb(188,207,243)")
            self.verticalLayout.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))
