import sys
import os

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QDesktopWidget,
    QMessageBox,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint
import requests

from constants import *
from create_challenge_window import CreateNewChallengeWindow

# with open("VERSION") as f:
#     version = f.read().strip()

#     online_version = requests.get(
#         "https://github.com/C-ffeeStain/CustomChallengeGen-TBoI/raw/main/VERSION"
#     ).text.strip()
#     if online_version != version:
#         outdated = True
#     else:
#         outdated = False

xml = "<challenges><challenge name={{NAME}} id={{ID}} startingitems={{ITEMS}} startingtrinkets={{TRINKETS}} startingpill={{PILL}} startingcard={{CARD}} playertype={{PLRTYPE}} endstage={{ENDBOSS}} ></challenge></challenges>"


class Main(QMainWindow):
    def check_for_update(self):
        if not IS_EXE:
            return
        online_version = requests.get(
            "https://github.com/C-ffeeStain/CustomChallengeGen-TBoI/raw/main/VERSION"
        ).text.strip()
        # if online_version != version:
        #     dialog = QMessageBox(self)
        #     dialog.setWindowTitle("New update!")
        #     dialog.setText(
        #         "There is a new update available. Would you like to download it now?"
        #     )
        #     dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #     dialog.setDefaultButton(QMessageBox.Yes)
        #     if dialog.exec_() == QMessageBox.Yes:
        #         # TODO: finish update code
        #         BASE_DIR / Path("CustomChallengeGen_TBoI.exe")
        #         os.rename(
        #             "CustomChallengeGen_TBoI.exe",
        #             ".".join(["CustomChallengeGen_TBoI", "old"]),
        #         )

    print("base path:", str(BASE_DIR))

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
        self.setFont(QFont(str(BASE_DIR / "resources/main_font.ttf"), 10))
        self.setFixedSize(300, 200)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.center()

        self.check_for_update()

        self.title = QLabel("Custom Challenge Generator\n(TBoI: Repentance)", self)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(
            QFont(str(BASE_DIR / "resources/main_font.ttf"), 12, QFont.Bold)
        )
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
