from PyQt4 import QtGui
from sys import exit

class MainWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Renamer")
        
        self.setToolTip("Hello, world!")
        
        
def graphicalmode(args,options):
    app = QtGui.QApplication(args)
    
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())