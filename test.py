import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.plusnumb = 1

        self.upgrade = QtWidgets.QPushButton("Upgrade (cost = $10)")
        self.gamble = QtWidgets.QPushButton("Gamble (cost = $100)")
        self.button = QtWidgets.QPushButton("press to get MONEY")
        self.text = QtWidgets.QLabel("$0",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.upgrade)
        self.layout.addWidget(self.gamble)

        self.button.clicked.connect(self.magic)
        self.upgrade.clicked.connect(self.upgradefnc)
        self.gamble.clicked.connect(self.loser)
    
    @QtCore.Slot()
    def upgradefnc(self):
        if self.counter >=10:
            self.counter -= 10
            self.plusnumb += 1
            self.updateCounter()

    @QtCore.Slot()
    def loser(self):
        if self.counter >=100:
            self.counter -= 100
            self.counter += random.randrange(0, 12)**2
            self.updateCounter()

    @QtCore.Slot()
    def magic(self):
        self.counter += self.plusnumb
        self.updateCounter()
    
    def updateCounter(self):
        self.text.setText("$"+str(self.counter))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())