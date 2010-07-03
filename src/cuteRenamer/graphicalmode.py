from PyQt4 import QtGui, QtCore
from sys import exit
from functions import rename_files, os

class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
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
        
        self.dirView.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        
        #Listedit for the optional listfile
        listPathLabel = QtGui.QLabel("Path to list:")
        self.listPathEdit = QtGui.QLineEdit()
        
        #Start renaming with number...
        startLabel = QtGui.QLabel("Start (default is 1)")
        self.startEdit = QtGui.QLineEdit()
        
        #LineEdit for the prefix
        prefixLabel = QtGui.QLabel("Prefix")
        self.prefixEdit = QtGui.QLineEdit()
        
        #LineEdit for the postfix
        postfixLabel = QtGui.QLabel("Postfix")
        self.postfixEdit = QtGui.QLineEdit()
        
        
        #The button to start renaming
        renameButton = QtGui.QPushButton('Rename!')
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(renameButton)
        
        vertical = QtGui.QVBoxLayout()
        vertical.addWidget(self.dirView)
        vertical.addStretch(1)
        vertical.addWidget(listPathLabel)
        vertical.addWidget(self.listPathEdit)
        vertical.addStretch(1)
        vertical.addWidget(startLabel)
        vertical.addWidget(self.startEdit)
        vertical.addStretch(1)
        vertical.addWidget(prefixLabel)
        vertical.addWidget(self.prefixEdit)
        vertical.addStretch(1)
        vertical.addWidget(postfixLabel)
        vertical.addWidget(self.postfixEdit)
        vertical.addStretch(1)
        vertical.addLayout(buttonsLayout)
        vertical.setSpacing(0)
        
        self.setLayout(vertical)
        
        #If the button is clicked start the renaming
        self.connect(renameButton, QtCore.SIGNAL('clicked()'), self.rename)
        
    def rename(self):
        selectedIndex = self.dirView.selectedIndexes()
        
        if self.listPathEdit.text() == "":
            files = os.listdir(self.dirModel.filePath(selectedIndex[0]))
        elif (not self.listPathEdit.text() == "") and os.path.isfile(self.listPathEdit.text()):
            files = [i.rstrip('\n') for i in open(self.listPathEdit.text(), "r")]
        else:
            print "Path to list doesn't exist or is not a file!"
        
        if not self.startEdit.text() == "":
            start = int(self.startEdit.text())
        else:
            start = 1
        
        prefix = self.prefixEdit.text()
        postfix = self.postfixEdit.text()
        
        os.chdir(self.dirModel.filePath(selectedIndex[0]))
        
        rename_files(start, prefix, postfix, False, files)
        
    def closeEvent(self, event):
        exit()
    
def graphicalmode(args, options):
    app = QtGui.QApplication(args)
    
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
