from Exercise_KTLT.Ex104.ui.MainWindow104 import Ui_MainWindow


class MainWindow104Ext(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.tableWidgetSong.itemSelectionChanged.connect(self.processSelectedItem)
        self.pushButtonClose.clicked.connect(self.processClose)
    def showWindow(self):
        self.MainWindow.show()
    def processSelectedItem(self):
        row=self.tableWidgetSong.currentRow()
        songId=self.tableWidgetSong.item(row,0)
        songName=self.tableWidgetSong.item(row,1)
        singer=self.tableWidgetSong.item(row,2)
        self.lineEditSongID.setText(songId.text())
        self.lineEditName.setText(songName.text())
        self.lineEditSinger.setText(singer.text())
    def processClose(self):
        self.MainWindow.close()
