import sys
from threading import Thread
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import math

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

MainAttractor_mass = 1000
Attractor_mass = 1

class Attractor:
    
    def __init__(self):
        self.G = 1
        self.mass = 100000
        self.speed = 10
        # int(input("행성의 속도를 입력하세요 : "))

        self.x = 25
        self.y = 225

class Pointer:
    
    def __init__(self):
        self.G = 1
        self.mass = 1
        self.x = 400
        self.y = 470
        self.a = 0
        self.xspeed = -1
        self.yspeed = 0
        
class CWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.attractor = Attractor()
    
        self.pointor = Pointer()
        

        self.thread = Thread(target=self.threadFunc)
        self.bThread = False     

        self.initUI()

    def initUI(self):
        self.setWindowTitle('swingby')        
        self.bThread = True
        self.thread.start()
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        d=50
        r=d/2

        rect = QRectF(self.attractor.x-r, self.attractor.y-r, d, d)
        qp.setBrush(QColor(0,0,0,128))
        qp.drawEllipse(rect)
        qp.drawText(rect, Qt.AlignCenter, 'speed:{}'.format(self.attractor.speed))
        
        d=20
        r=d/2

        rect = QRectF(self.pointor.x-r, self.pointor.y-r, d, d)
        qp.setBrush(QColor(0,0,0,128))
        qp.drawEllipse(rect)
        qp.drawText(rect, Qt.AlignCenter, '')
        
        qp.end()

    def threadFunc(self):
        while self.bThread:
            
            self.attractor.x += 1

            distance = math.sqrt(((self.attractor.x-self.pointor.x)**2)+((self.attractor.y-self.pointor.y)**2))
            mu = self.attractor.G*self.attractor.mass

            theta = math.atan2(self.attractor.x-self.pointor.x, self.attractor.y-self.pointor.y)
            degree = theta*(180/math.pi)

            force = (self.attractor.G*self.attractor.mass*self.pointor.mass)/(distance**2)
            xa = force*math.sin(degree)
            ya = force*math.cos(degree)

            self.pointor.xspeed -= xa
            self.pointor.yspeed += ya

            self.pointor.x += self.pointor.xspeed/self.attractor.speed
            self.pointor.y += self.pointor.yspeed/self.attractor.speed

            self.update()
            QApplication.processEvents()
            time.sleep(0.1/self.attractor.speed)
             
    def closeEvent(self, e):
        self.bThread = False

app = QApplication(sys.argv)
w = CWidget()
sys.exit(app.exec_())