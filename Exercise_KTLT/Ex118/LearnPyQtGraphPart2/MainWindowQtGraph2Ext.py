from PyQt6.QtCore import Qt

from Exercise_KTLT.Ex118.LearnPyQtGraphPart2.MainWindowQtGraph2 import Ui_MainWindow
import pyqtgraph as pg

class MainWindowQtGraph2Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        # Step 2: call pg.PlotWidget()
        self.graphWidget=pg.PlotWidget()
        #Title
        self.graphWidget.setTitle("Temperature per hour", color="b", size="30pt", bold=True, italic=True)
        #Title axis, style
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
        styles_top_right = {"color": "green", "font-size": "15px"}
        self.graphWidget.setLabel("top", "Learn PyQtGraph", **styles_top_right)
        self.graphWidget.setLabel("right", "Sang", **styles_top_right)
        #Background color
        self.graphWidget.setBackground('#f5dadf')
        #Grid
        self.graphWidget.showGrid(x=True, y=True)
        # Step 3: Create plot data
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        temperature = [20, 21, 20, 32, 33, 31, 29, 31, 32, 35, 37, 45]
        temperature2 = [25, 18, 30, 10, 47, 29, 26, 32, 35, 45, 40, 42]
        # Step 4: call plot method
        # Edit line
        pen = pg.mkPen(color=(255, 0, 0), width=10, style=Qt.PenStyle.SolidLine)
        # Mau duong vien cua marker
        symbolPen = pg.mkPen(color=(196, 196, 196), width=2)
        # Add legend
        self.graphWidget.addLegend()
        #Gioi han cho truc
        #self.graphWidget.setXRange(0, 13, padding=0)
        #self.graphWidget.setYRange(10, 50, padding=0)
        self.graphWidget.plot(hour, temperature, name="Sensor X", pen=pen,
                              symbol='o',
                              symbolSize=10,
                              symbolBrush='b',
                              symbolPen=symbolPen)
        #Second widget
        pen2 = pg.mkPen(color='g', width=8, style=Qt.PenStyle.DotLine)
        symbolPen2 = pg.mkPen(color=(255, 255, 0), width=2)
        plot2=self.graphWidget.plot(hour, temperature2, name="Sensor Y",
                              pen=pen2,
                              symbol='d',
                              symbolSize=8,
                              symbolBrush=('r'),
                              symbolPen=symbolPen2)
        temperature2[3]=100
        plot2.setData(hour,temperature2)
        # Step 5: add graphWidget into Layout:
        self.myLayout.addWidget(self.graphWidget)
    def show(self):
        self.MainWindow.show()