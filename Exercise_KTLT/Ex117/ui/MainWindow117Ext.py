from Exercise_KTLT.Ex117.ui.MainWindow117 import Ui_MainWindow
import numpy as np


class MainWindow117Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonCalculate.clicked.connect(self.process_statistics)
    def process_statistics(self):
        inputdata=self.lineEditData.text()
        arr_input=[int(i) for i in inputdata.split(',')] #tach chuoi phan tu co dau phay xong dua ve int
        arr_numpy=np.asarray(arr_input)
        """arr_result=[]
        arr_result.append(np.min(arr_numpy))  # min value
        arr_result.append(np.argmin(arr_numpy))  # min element index
        arr_result.append(np.max(arr_numpy))  # max value
        arr_result.append(np.argmax(arr_numpy))  # max element index
        arr_result.append(np.mean(arr_numpy))  # mean value
        arr_result.append(np.median(arr_numpy))  # median value
        arr_result.append(np.std(arr_numpy))  # standard deviation
        result='\n'.join(map(str,arr_result))"""
        min_label=f"MIN={np.min(arr_numpy)}"
        argmin_label=f"ARGMIN={np.argmin(arr_numpy)}"
        max_label=f"MAX={np.max(arr_numpy)}"
        argmax_label = f"ARGMAX={np.argmax(arr_numpy)}"
        mean_label=f"MEAN={np.mean(arr_numpy)}"
        median_label=f"MEDIAN={np.median(arr_numpy)}"
        std_label=f"STD={np.std(arr_numpy)}"
        result=min_label+'\n'+argmin_label+'\n'+max_label+'\n'+argmax_label+'\n'+mean_label+'\n'+median_label+'\n'+std_label
        self.labelResult.setText(result)