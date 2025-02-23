import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from Exercise_KTLT.Ex85.ui.AssetMainWindow import Ui_MainWindow
from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.asset import Asset


class AssetMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.assets = None
        self.selected_asset= None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
        self.load_assets()
        self.display_asset_layout()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save_asset)
        self.pushButtonRemove.clicked.connect(self.process_remove_asset)

    def load_assets(self):
        filename = "assets.json"
        path = f"../dataset/{filename}"
        jff = JsonFileFactory()
        self.assets = jff.read_data(path, Asset)

    def process_save_asset(self):
        id = self.lineEditID.text()
        name = self.lineEditName.text()
        year = int(self.lineEditYear.text())
        value = int(self.lineEditValue.text())
        a = Asset(id, name, year, value)
        self.assets.append(a)
        # cần lưu lại cơ sở dữ liệu:
        jff = JsonFileFactory()
        filename = "../dataset/assets.json"
        jff.write_data(self.assets, filename)
        self.display_asset_layout()

    def display_asset_layout(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.assets)):
            x=self.assets[i]
            title = f"{x.AssetId}-{x.AssetName}-{x.ImportYear}-{x.Value}"
            btn = QPushButton(text=title)
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
        self.selected_asset=i
        asset=self.assets[i]
        self.lineEditID.setText(f"{asset.AssetId}")
        self.lineEditName.setText(f"{asset.AssetName}")
        self.lineEditYear.setText(f"{asset.ImportYear}")
        self.lineEditValue.setText(f"{asset.Value}")


    def process_remove_asset(self):
        msp = self.lineEditID.text()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Remove confirmation")
        dlg.setText(f"Are you sure to delete {msp}?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.No:
            return  # ngừng hàm xóa, ko làm gì cả
        if self.selected_asset is not None:
            self.assets.pop(self.selected_asset)
            # cập nhật lại CSDL sau khi xóa:
            # cần lưu lại cơ sở dữ liệu:
            jff = JsonFileFactory()
            filename = "../dataset/assets.json"
            jff.write_data(self.assets, filename)
            self.display_asset_layout()




