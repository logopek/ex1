import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.status = None
        self.initUI()
        self.qp = QPainter()
        self.coords = []
        self.flag = False

    def draw(self, status):
        if status == 1:
            self.qp.drawEllipse(*self.coords, 20, 20)
        if status == 2:
            self.qp.drawRect(*self.coords, 20, 20)
        if status == 3:
            x, y = self.coords
            radius = 15
            length = 13
            coord = [(x, y + radius), (x + length, y - radius), (x - length, y - radius)]
            self.qp.drawLine(*coord[0], *coord[1])
            self.qp.drawLine(*coord[1], *coord[2])
            self.qp.drawLine(*coord[2], *coord[0])

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)

            self.qp.end()

    def drawfigure(self):

        self.flag = True
        self.update()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Суперматизм')
        self.show()

    def mousePressEvent(self, event):
        self.coords = [event.x(), event.y()]
        if event.button() == Qt.LeftButton:
            self.status = 1
        elif event.button() == Qt.RightButton:
            self.status = 2

        self.drawfigure()

    def mouseMoveEvent(self, event):
        self.coords = [event.x(), event.y()]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
        self.drawfigure()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
