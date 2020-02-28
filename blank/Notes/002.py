
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

class Main(QWidget):

    def __init__(self):
        super(Main, self).__init__()

        hbox = QHBoxLayout()

        self.setLayout(hbox)
        self.view = MyView(self)
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        hbox.addWidget(self.view)


class MyView(QGraphicsView):

    def __init__(self, parent):
        super(MyView, self).__init__(parent)
        self.parent = parent

    def mousePressEvent(self, event):
        super(MyView, self).mousePressEvent(event)
        test = MySvg()
        self.parent.scene.addItem(test)


class MySvg(QGraphicsSvgItem):

    def __init__(self):
        super(MySvg, self).__init__('ubuntu.svg')

        self.setFlags(QGraphicsItem.ItemIsSelectable|
                      QGraphicsItem.ItemIsMovable)

        self.setAcceptsHoverEvents(True)

    def hoverEnterEvent(self, event):
        print 'Enter'

    def hoverLeaveEvent(self, event):
        print 'Leave'

    def hoverMoveEvent(self, event):
        print 'Moving'


def runMain():

    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    runMain()
