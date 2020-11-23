# Import Krita
from krita import *
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg, uic
import os.path


# Set Window Title Name
DOCKER_NAME = "Blank"

# Create Docker
class BlankDocker(DockWidget):
    """
    Comments
    """
    # Initialize the Dicker Window
    def __init__(self):
        super(BlankDocker, self).__init__()

        # Window Title
        self.setWindowTitle(DOCKER_NAME)
        # Widget
        self.window = QWidget()
        # self.layout =
        self.layout = uic.loadUi(os.path.dirname(os.path.realpath(__file__)) + '/blank.ui', self.window)
        self.setWidget(self.window)

        # TESTING###################################################################################




        ############################################################################################
    # Change the Canvas
    def canvasChanged(self, canvas):
        pass
