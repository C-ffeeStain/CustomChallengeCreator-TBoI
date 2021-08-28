import sys

from page_handler import pageHandler
from create_challenge_window import CreateNewChallengeWindow

playertypes = [
    "Isaac",
    "Magdalene",
    "Cain",
    "Judas",
    "???",
    "Eve",
    "Samson",
    "Azazel",
    "Lazarus",
    "Eden",
    "The Lost",
    "Lazarus Risen",
    "Dark Judas",
    "Lilith",
    "Keeper",
    "Apollyon",
    "The Forgotten",
    "The Soul",
    "Bethany",
    "Jacob",
    "Esau",
    "Tainted Isaac",
    "Tainted Magdalene",
    "Tainted Cain",
    "Tainted Judas",
    "Tainted ???",
    "Tainted Eve",
    "Tainted Samson",
    "Tainted Azazel",
    "Tainted Lazarus",
    "Tainted Eden",
    "Tainted Lost",
    "Tainted Lilith",
    "Tainted Keeper",
    "Tainted Apollyon",
    "Tainted Forgotten",
    "Tainted Bethany",
    "Tainted Jacob",
    "Dead Tainted Lazarus",
    "Tainted Jacob 2",
    "Tainted Soul",
]

end_bosses = {
    "Basement 1 Boss": 1,
    "Basement 2 Boss": 2,
    "Caves 1 Boss": 3,
    "Caves 2 Boss": 4,
    "Depths 1 Boss": 5,
    "Mom": 6,
    "Womb 1 Boss": 7,
    "Mom's Heart/It Lives": 8,
    "Hush": 9,
    "Satan": 10,
    "The Lamb": 11,
    "Delirium": 12,
    "The Beast": 13,
    "Mega Satan": 14,
}

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
        self.title.setFont(QFont("fonts/Montserrat-Bold.ttf", 12, QFont.Bold))
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
