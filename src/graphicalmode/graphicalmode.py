from PyQt4 import QtGui, QtCore
from sys import exit
from lib.functions import rename_files, os

class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.setWindowTitle("Renamer")

        #Set Data-Model for showing the directories
        self.dirModel = QtGui.QFileSystemModel()
        self.dirModel.setRootPath('/')
        self.dirModel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)#Show only directories without '.' and '..'
        #Set the view for the directories
        self.dirView = QtGui.QTreeView()
        self.dirView.setModel(self.dirModel)
        #Show only the directories in the view
        self.dirView.setColumnHidden(1, True)
        self.dirView.setColumnHidden(2, True)
        self.dirView.setColumnHidden(3, True)
        #Layout
        dirLayout = QtGui.QVBoxLayout()
        dirLayout.addStretch(1)
        dirLayout.addWidget(self.dirView)
        
        #Listedit for the optional listfile
        listPathLabel = QtGui.QLabel("Path to list:")
        self.listPathEdit = QtGui.QLineEdit()
        #Layout
        listPathLayout = QtGui.QVBoxLayout()
        listPathLayout.addStretch(1)
        listPathLayout.addWidget(listPathLabel)
        listPathLayout.addWidget(self.listPathEdit)
        
        #Start renaming with number...
        startLabel = QtGui.QLabel("Start (default is 1)")
        self.startEdit = QtGui.QLineEdit()
        #Layout
        startEditLayout = QtGui.QVBoxLayout()
        startEditLayout.addStretch(1)
        startEditLayout.addWidget(startLabel)
        startEditLayout.addWidget(self.startEdit)
        
        #LineEdit for the prefix
        prefixLabel = QtGui.QLabel("Prefix")
        self.prefixEdit = QtGui.QLineEdit()
        #Layout
        prefixEditLayout = QtGui.QVBoxLayout()
        prefixEditLayout.addStretch(1)
        prefixEditLayout.addWidget(prefixLabel)
        prefixEditLayout.addWidget(self.prefixEdit)
        
        #LineEdit for the postfix
        postfixLabel = QtGui.QLabel("Postfix")
        self.postfixEdit = QtGui.QLineEdit()
        #Layout
        postfixEditLayout = QtGui.QVBoxLayout()
        prefixEditLayout.addStretch(1)
        prefixEditLayout.addWidget(postfixLabel)
        prefixEditLayout.addWidget(self.postfixEdit)
        
        #The button to start renaming(actually it's a dummy)
        renameButton = QtGui.QPushButton('Rename!')
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(renameButton)
        
        vertical = QtGui.QVBoxLayout()
        vertical.addStretch(1)
        vertical.addLayout(dirLayout)
        vertical.addLayout(listPathLayout)
        vertical.addLayout(startEditLayout)
        vertical.addLayout(prefixEditLayout)
        vertical.addLayout(postfixEditLayout)
        vertical.addLayout(buttonsLayout)
        
        self.setLayout(vertical)
        
        self.connect(renameButton, QtCore.SIGNAL('clicked()'), self.rename)
        
    def rename(self):
        selectedIndex = self.dirView.selectedIndexes()
        if self.listPath.text() == "":
            files = os.listdir(self.dirModel.filePath(selectedIndex[0]))
        elif (not self.listPath.text() == "") and os.path.isFile(self.listPath.text()):
            files = [i.rstrip('\n') for i in open(self.listPath.text, "r")]
        else:
            print "Path to list doesn't exist or is not a file!"
        
        os.chdir(self.dirModel.filePath(selectedIndex[0]))
        
        rename_files(1, "pre_", "_post", False, files)
        
def graphicalmode(args, options):
    app = QtGui.QApplication(args)
    
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
