import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.pushButton = QPushButton("Нарисовать", self)
        self.pushButton.clicked.connect(self.click)
        self.do_paint = False

    def click(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.risuem(qp)
            qp.end()
        self.do_paint = False

    def risuem(self, qp):
        r = random.randint(10, 200)
        cr = random.randint(0, 255)
        cg = random.randint(0, 255)
        cb = random.randint(0, 255)

        qp.setBrush(QColor(cr, cg, cb))
        qp.drawEllipse(50, 50, 50 + r, 50 + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())