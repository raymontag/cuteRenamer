from PyQt4 import QtGui, QtCore
from sys import exit

class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Renamer")

        #Set Data-Model for showing the directories
        dirModel = QtGui.QFileSystemModel()
        dirModel.setRootPath('/')
        dirModel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)#Show only directories without '.' and '..'
        #Set the view for the directories
        dirView = QtGui.QTreeView()
        dirView.setModel(dirModel)
        #Show only the directories in the view
        dirView.setColumnHidden(1, True)
        dirView.setColumnHidden(2, True)
        dirView.setColumnHidden(3, True)
        #Layout
        dirLayout = QtGui.QVBoxLayout()
        dirLayout.addStretch(1)
        dirLayout.addWidget(dirView)
        
        #The button to start renaming(actually it's a dummy)
        renameButton = QtGui.QPushButton('Rename!')
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(renameButton)
        
        vertical = QtGui.QVBoxLayout()
        vertical.addStretch(1)
        vertical.addLayout(dirLayout)
        vertical.addLayout(buttonsLayout)
        
        self.setLayout(vertical)
        
def graphicalmode(args, options):
    app = QtGui.QApplication(args)
    
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
