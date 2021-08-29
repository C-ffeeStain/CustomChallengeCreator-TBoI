import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QDesktopWidget,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint

from create_challenge_window import CreateNewChallengeWindow

with open("VERSION") as f:
    version = f.read().strip()
    if version.find("-beta") != -1:
        print(
            "WARNING: You are using a beta version of the program. Please report any bugs."
        )
    else:
        pass

xml = "<challenges><challenge name={{NAME}} id={{ID}} startingitems={{ITEMS}} startingtrinkets={{TRINKETS}} startingpill={{PILL}} startingcard={{CARD}} playertype={{PLRTYPE}} endstage={{ENDBOSS}} ></challenge></challenges>"


class Main(QMainWindow):
    def createNewChallengeClicked(self):
        self.createNewChallengeWindow = CreateNewChallengeWindow()
        self.createNewChallengeWindow.move(self.x(), self.y())
        self.createNewChallengeWindow.show()
        self.destroy()

    def loadChallengeClicked(self):
        pass

    def __init__(self, parent=None):
        super(Main, self).__init__(parent=parent)
        self.setWindowTitle("Custom Challenge Generator - TBoI")
        self.setGeometry(300, 300, 450, 300)
        self.setFont(QFont("fonts/Montserrat.ttf", 10))
        self.setFixedSize(300, 200)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.center()

        self.title = QLabel("Custom Challenge Generator\n(TBoI: Repentance)", self)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("fonts/normal.ttf", 12, QFont.Bold))
        self.title.move(30, 20)
        self.title.adjustSize()

        self.createNewChallenge = QPushButton("Create New Challenge", self)
        self.createNewChallenge.clicked.connect(self.createNewChallengeClicked)
        self.createNewChallenge.move(85, 75)
        self.createNewChallenge.adjustSize()

        self.loadChallenge = QPushButton("Load Challenge", self)
        self.loadChallenge.clicked.connect(self.loadChallengeClicked)
        self.loadChallenge.move(105, 110)
        self.loadChallenge.adjustSize()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())
