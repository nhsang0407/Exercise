from PyQt6.QtCore import Qt

from Exercise_KTLT.Ex118.EX118.ui.MainWindow118 import Ui_MainWindow
import numpy as np
import pyqtgraph as pg

class MainWindow118Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonPlotData.clicked.connect(self.process_draw_plot)
    def process_draw_plot(self):
        self.graphWidget = pg.PlotWidget()
        inputdata=self.lineEditInput.text()
        arr_input = [int(i) for i in inputdata.split(',')]
        arr_numpy = np.asarray(arr_input)
        pen = pg.mkPen(color='g', width=10, style=Qt.PenStyle.SolidLine)
        symbolPen = pg.mkPen(color=(196, 196, 196), width=2)
        self.graphWidget.plot(arr_numpy,
                              pen=pen,
                              symbol='o',
                              symbolSize=10,
                              symbolBrush='b',
                              symbolPen=symbolPen)
        self.verticalLayout.addWidget(self.graphWidget)