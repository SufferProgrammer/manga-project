from design import *
from PyQt4 import QtSql as dbase
import design
import sys

class Mangareader(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(Mangareader, self).__init__()
        self.setupUi(self)
        self.viewerSetting()
        self.actionMenu()

    def zoomSetting(self, sizeSize):
        self.label.resize(self.scaleFactor * self.label.pixmap().size())
        self.scaleFactor *= sizeSize

    def viewerSetting(self):
        self.label.setScaledContents(True)
        self.scaleFactor = 1.0
        self.label.setPixmap(QtGui.QPixmap('developer/preview.jpg'))

    def actionMenu(self):
        self.actionZoom_In.triggered.connect(self.zoomin)
        self.actionExit.triggered.connect(self.exit)
        #self.actionFull_Screen.triggeredc.connect(self.fullscreen)

    def zoomin(self):
        self.zoomSetting(0.25)

    def exit(self):
        sys.exit()

#---------------->> Database Connect Session <<--------------------#

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Application = Mangareader()

    Application.show()
    sys.exit(app.exec_())
