import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import Qt



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500)
        self.qp = QPainter()
        self.flag = False
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Create Circle")
        self.btn.setGeometry(200, 400, 100, 50)
        self.btn.clicked.connect(self.drawfigure)

    def draw(self):
        self.colors = [Qt.red, Qt.yellow, Qt.gray, Qt.green]
        self.qp.setBrush(random.choice(self.colors))
        d = random.randint(0,50)
        self.qp.drawEllipse(random.randint(0,500), random.randint(0,500), d, d)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def drawfigure(self):
        self.flag = True
        self.update()

def _except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    exe = Example()
    exe.show()
    sys.excepthook = _except_hook
    sys.exit(app.exec_())

