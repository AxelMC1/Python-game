import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

counter = 0

class GeneratorWidget(QtWidgets.QWidget):
    def __init__(self, game):
        super().__init__()

        self.inc = 1
        self.game = game

        self.button = QtWidgets.QPushButton(f"Get $${self.inc})")
        self.button.clicked.connect(self.click)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

    @QtCore.Slot()
    def click(self):
        self.game.counter += self.inc
        self.game.updateCounter()

    def increment(self, amount):
        self.inc += amount

    
    def update(self):
        self.button.setText(f"Get $${self.inc})")

class UpgradeWidget(QtWidgets.QWidget):
    def __init__(self, game, cost, widget):
        super().__init__()

        self.cost = cost
        self.inc = 1
        self.incWidget = widget
        self.game = game

        self.button = QtWidgets.QPushButton(f"Upgrade (cost ${self.cost})")
        self.button.clicked.connect(self.click)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

    @QtCore.Slot()
    def click(self):
        if self.game.counter < self.cost:
            return
        self.game.counter -= self.cost
        self.incWidget.increment(self.inc)
        self.game.updateCounter()

    def increment(self, amount):
        self.inc += amount

    
    def update(self):
        pass

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.counter = 0

        self.generator = GeneratorWidget(self)
        self.upgrade = UpgradeWidget(self, 10, self.generator)
        self.upgrade2 = UpgradeWidget(self, 500, self.upgrade)
        self.gamble = QtWidgets.QPushButton("Gamble (cost = $100)")
        self.text = QtWidgets.QLabel("$0",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.generator)
        self.layout.addWidget(self.upgrade)
        self.layout.addWidget(self.gamble)
        self.layout.addWidget(self.upgrade2)

        self.gamble.clicked.connect(self.loser)
    
    @QtCore.Slot()
    def loser(self):
        if self.counter >=100:
            self.counter -= 100
            self.counter += random.randrange(0, 12)**2
            self.updateCounter()
    
    def updateCounter(self):
        self.text.setText("$"+str(self.counter))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())