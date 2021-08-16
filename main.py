import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

MainAttractor_mass = 1000
Attractor_mass = 1

class Attractor:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.G = 1
        self.mass = 1000
        self.speed = int(input("행성의 속도를 입력하세요 : "))

class Pointer:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.G = 1
        self.mass = 10

class Mover(QWidget):

    def __init__(self):
        super().__init__()

        self.attractor = Attractor()
    
        self.pointor = Pointer()

        self.initUI()

    def initUI(self):
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        d=50
        r=d/2

        self.attractor.x = r
        self.attractor.y = self.rect().height()/2

        rect = QRectF(self.attractor.x-r, self.attractor.y-r, d, d)
        qp.setBrush(QColor(0,0,0,128))
        qp.drawEllipse(rect)
        qp.drawText(rect, Qt.AlignCenter, 'speed:{}'.format(self.attractor.speed))
        
        d=20
        r=d/2

        self.pointor.x = self.rect().width()/1.5
        self.pointor.y = self.rect().height()-r

        rect = QRectF(self.pointor.x-r, self.pointor.y-r, d, d)
        qp.setBrush(QColor(0,0,0,128))
        qp.drawEllipse(rect)
        qp.drawText(rect, Qt.AlignCenter, '')
        
        qp.end()

app = QApplication(sys.argv)
w = Mover()
sys.exit(app.exec_())   