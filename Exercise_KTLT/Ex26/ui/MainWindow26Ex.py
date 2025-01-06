from Exercise_KTLT.Ex26.ui.MainWindow26 import Ui_MainWindow

class MainWindow26Ex(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonInput.clicked.connect(self.input)
        self.pushButtonUpper.clicked.connect(self.upper)
        self.pushButtonLower.clicked.connect(self.lower)
        self.pushButtonCountLow.clicked.connect(self.count_low)
        self.pushButtonCountUp.clicked.connect(self.count_up)
        self.pushButtonPrintNumberWPL.clicked.connect(self.number_words_per_line)
        self.pushButtonWordCount.clicked.connect(self.word_count)
        self.pushButtonVowel_Consonant.clicked.connect(self.vowel_consonant)
        self.pushButtonExit.clicked.connect(self.exit)

    def input(self):
        self.lineEditInput.clear()
        self.lineEditInput.setFocus()
        self.labelOutput.clear()
    def upper(self):
        input=self.lineEditInput.text()
        self.labelOutput.setText(input.upper())
    def lower(self):
        input = self.lineEditInput.text()
        self.labelOutput.setText(input.lower())
    def count_low(self):
        count=0
        input = self.lineEditInput.text()
        for i in input:
            if i.islower():
                count=count+1
        self.labelOutput.setText(str(count))
    def count_up(self):
        count = 0
        input = self.lineEditInput.text()
        for i in input:
            if i.isupper():
                count = count + 1
        self.labelOutput.setText(str(count))
    def number_words_per_line(self):
        output=""
        input = self.lineEditInput.text()
        words_per_line = input.split("\n")
        for i in words_per_line:
            output = output + str(len(i.split())) + "\n"
        self.labelOutput.setText(output)
    def word_count(self):
        input=self.lineEditInput.text()
        word_count=len(input.split())
        self.labelOutput.setText(f"{word_count}")
    def vowel_consonant(self):
        vowel="aăâeêioôơuưyAĂÂEÊIOÔƠUƯY"
        input=self.lineEditInput.text()
        list_vowel=[]
        list_consonant=[]
        for i in input:
            if input.isalpha():
                if i in vowel:
                    list_vowel.append(i)
                else:
                    list_consonant.append(i)
        self.labelOutput.setText("".join(list_vowel)+'\n'+"".join(list_consonant))
    def exit(self):
        self.MainWindow.close()

