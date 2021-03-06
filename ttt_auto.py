from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta
from ttt_ai import ai_player
import random
from time import sleep

class Ui_Dialog(object):
    score={0:0,1:0}
    game=0
    def play(self, index):
        color = lambda player: "green" if self.player else "blue"
        
        if self.flag % 2:
            icon = qta.icon('fa5s.times', scale_factor=2.0, color_disabled=color(self.player))
        else:
            icon = qta.icon('fa5s.dot-circle', scale_factor=1.2, color_disabled=color(self.player))

        self.buttons[index].setIcon(icon)
        self.buttons[index].setEnabled(False)
        self.buttons[index].player = int(self.player)

        if winBoxes := self.checkWin():
            if winBoxes == 1:
                self.gameOver=True
                self.showDialog("Match Draw.")
            else:
                self.gameOver=True
                for i in winBoxes:
                    self.buttons[i].setStyleSheet(f"border:1px solid {color(self.player)}")
                self.score[self.player]+=1
                self.showDialog("AI wins." if self.player else "You win.")
        else:
            self.flag += 1
            self.player = not self.player
        
        if self.gameOver:
            self.resetBoard()
        else:
            if self.player:
                next_move=ai_player(self.grid)
                self.play(next_move)
        

    def checkWin(self):
        grid = []
        for i in self.buttons:
            grid.append((i.player))
        self.grid=grid

        # check horizontal rows
        for i in range(0, 9, 3):
            if grid[i] == grid[i+1] == grid[i+2] != -1:
                return (i, i+1, i+2)
        # check vertical rows
        for i in range(3):
            if grid[i] == grid[i+3] == grid[i+6] != -1:
                return(i, i+3, i+6)
        # check corners
        if grid[0] == grid[4] == grid[8] != -1:
            return (0, 4, 8)
        if grid[2] == grid[4] == grid[6] != -1:
            return (2, 4, 6)
        # if draw return 1
        if -1 not in grid:
            return 1
        return False

    def resetBoard(self):
        self.firstmove = random.choice([0,1])
        self.player=self.firstmove
        self.flag=self.firstmove
        self.P0.setText(str(self.score[0]))
        self.P1.setText(str(self.score[1]))
        self.gameOver=False
        self.showDialog(f"First Move: {'AI' if self.firstmove else 'You'}","Next Move")
        self.game+=1
        self.grid=[-1]*9
        print(f"Game {self.game}")
        color="blue"
        for i in self.buttons:
            i.setIcon(QtGui.QIcon())
            i.setStyleSheet("QPushButton::hover{border:1px solid "+color+";}")
            i.setEnabled(True)
            i.player=-1

        if self.player:
            next_move=ai_player(self.grid)
            self.play(next_move)
       
    def showDialog(self,text,title="Game Over"):
        message = QtWidgets.QMessageBox(self.Dialog)
 
        message.setText(text)
        message.setWindowTitle(title)
        message.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Close)
        message.buttonClicked.connect(self.checkQuit)

        message.exec_()

    def checkQuit(self,button):
        if button.text()=="Close":
            sys.exit()

    def setupUi(self, Dialog):
        self.Dialog=Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 400)

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 40, 350, 350))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.G1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G1.setMinimumSize(QtCore.QSize(100, 100))
        self.G1.setObjectName("G1")
        self.gridLayout.addWidget(self.G1, 0, 0, 1, 1)
        self.G1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G1.clicked.connect(lambda: self.play(0))

        self.G2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G2.setMinimumSize(QtCore.QSize(100, 100))
        self.G2.setObjectName("G2")
        self.gridLayout.addWidget(self.G2, 0, 1, 1, 1)
        self.G2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G2.clicked.connect(lambda: self.play(1))

        self.G3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G3.setMinimumSize(QtCore.QSize(100, 100))
        self.G3.setObjectName("G3")
        self.gridLayout.addWidget(self.G3, 0, 2, 1, 1)
        self.G3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G3.clicked.connect(lambda: self.play(2))

        self.G4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G4.setMinimumSize(QtCore.QSize(100, 100))
        self.G4.setObjectName("G4")
        self.gridLayout.addWidget(self.G4, 1, 0, 1, 1)
        self.G4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G4.clicked.connect(lambda: self.play(3))

        self.G5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G5.setMinimumSize(QtCore.QSize(100, 100))
        self.G5.setObjectName("G5")
        self.gridLayout.addWidget(self.G5, 1, 1, 1, 1)
        self.G5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G5.clicked.connect(lambda: self.play(4))

        self.G6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G6.setMinimumSize(QtCore.QSize(100, 100))
        self.G6.setObjectName("G6")
        self.gridLayout.addWidget(self.G6, 1, 2, 1, 1)
        self.G6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G6.clicked.connect(lambda: self.play(5))

        self.G7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G7.setMinimumSize(QtCore.QSize(100, 100))
        self.G7.setObjectName("G7")
        self.gridLayout.addWidget(self.G7, 2, 0, 1, 1)
        self.G7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G7.clicked.connect(lambda: self.play(6))

        self.G8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G8.setMinimumSize(QtCore.QSize(100, 100))
        self.G8.setObjectName("G8")
        self.gridLayout.addWidget(self.G8, 2, 1, 1, 1)
        self.G8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G8.clicked.connect(lambda: self.play(7))

        self.G9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G9.setMinimumSize(QtCore.QSize(100, 100))
        self.G9.setObjectName("G9")
        self.gridLayout.addWidget(self.G9, 2, 2, 1, 1)
        self.G9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.G9.clicked.connect(lambda: self.play(8))

        self.buttons = [self.G1, self.G2, self.G3,
                        self.G4, self.G5, self.G6,
                        self.G7, self.G8, self.G9]

        font = QtGui.QFont()
        font.setPointSize(12)
        self.Score = QtWidgets.QLabel(Dialog)
        self.Score.setGeometry(QtCore.QRect(5, 5, 50, 20))
        self.Score.setFont(font)
        self.Score.setObjectName("Score")

        self.P0 = QtWidgets.QLabel(Dialog)
        self.P0.setGeometry(QtCore.QRect(110, 5, 50, 20))
        self.P0.setFont(font)
        self.P0.setStyleSheet("color:blue")
        self.P0.setObjectName("P1")

        self.P1 = QtWidgets.QLabel(Dialog)
        self.P1.setGeometry(QtCore.QRect(180, 5, 50, 20))
        self.P1.setFont(font)
        self.P1.setStyleSheet("color:green")
        self.P1.setObjectName("P2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tic Tac Toe"))
        self.Score.setText(_translate("Dialog", "Score: "))
        self.P0.setText(_translate("Dialog", "0"))
        self.P1.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.resetBoard()
    sys.exit(app.exec())
