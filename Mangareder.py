from design import *
from PyQt4 import QtSql as dbase
import design
import sys

class Mangareader(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(Mangareader, self).__init__()
        self.setupUi(self)
        self.searchmanga()
        self.downloadmanga()
        self.preview()
        self.next()

    def searchmanga(self):
        self.pushButton_2.clicked.connect(self.search)

    def search(self):
        print("Searching Manga...")

    def downloadmanga(self):
        self.pushButton.clicked.connect(self.download)

    def download(self):
        print("Downloading Manga...")

    def next(self):
        self.pushButton_4.clicked.connect(self.nextNext)

    def nextNext(self):
        nextImage = "developer/next.png"
        self.label.setPixmap(QtGui.QPixmap(nextImage))
        self.label_2.setText("Page 2")

    def preview(self):
        self.pushButton_3.clicked.connect(self.prevPreview)

    def prevPreview(self):
        previewImage = "developer/preview.jpg"
        self.label.setPixmap(QtGui.QPixmap(previewImage))
        self.label_2.setText("Page 1")

#---------------->> Database Connect Session <<--------------------#

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Application = Mangareader()

    Application.show()
    sys.exit(app.exec_())
