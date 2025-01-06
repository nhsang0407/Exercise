from random import randrange
from time import sleep

from PyQt6.QtWidgets import QMessageBox

from Exercise_KTLT.Ex24.ui.MainWindow24 import Ui_MainWindow


class MainWindow24Ex(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonRandom.clicked.connect(self.random)
        self.pushButtonNewGame.clicked.connect(self.new_game)
        self.pushButtonExit.clicked.connect(self.exit)

    def random(self):
        player=float(self.labelPlayer.text())
        machine=float(self.labelMachine.text())
        if player<30:
            msg=QMessageBox(self.MainWindow)
            msg.setWindowTitle("BIP BIP")
            msg.setText("Your money is not enough")
            msg.exec()
        elif machine<0:
            msg2=QMessageBox(self.MainWindow)
            msg2.setWindowTitle("BINGO")
            msg2.setText("You win, machine is out of money")
            msg2.exec()
        else:
            self.label_1.setText(str(randrange(0, 8)))
            self.label_2.setText(str(randrange(0, 9)))
            self.label_3.setText(str(randrange(0, 10)))
            player=player-30
            self.labelPlayer.setText(str(player))
            machine = machine+30
            self.labelMachine.setText(str(machine))
            if float(self.label_1.text())==7:
                player=round(player+100+machine*0.5,2)
                machine=round(machine-machine*0.5,2)
                self.labelPlayer.setText(str(player))
                self.labelMachine.setText(str(machine))
            if float(self.label_2.text())==7:
                player=round(player+30+machine*0.5,2)
                machine=round(machine-machine*0.5,2)
                self.labelPlayer.setText(str(player))
                self.labelMachine.setText(str(machine))
            if float(self.label_1.text())==7:
                player=round(player+10,2)
                machine=round(machine,2)
                self.labelPlayer.setText(str(player))
                self.labelMachine.setText(str(machine))

    def new_game(self):
        self.label_1.clear()
        self.label_2.clear()
        self.label_3.clear()
        money=100
        self.labelMachine.setText(str(money))
        self.labelPlayer.setText(str(money))

    def exit(self):
        self.MainWindow.close()