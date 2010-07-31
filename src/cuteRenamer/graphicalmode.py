from PySide import QtGui, QtCore
from sys import exit
from functions import rename_files, os

class MainWindow(QtGui.QWidget):
    def __init__(self, verbose):
        self.verbose = verbose
        
        QtGui.QWidget.__init__(self)
        
        self.setWindowTitle("cuteRenamer")

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
        
        #Checkbox to conserve file extensions
        self.checkboxConserve = QtGui.QCheckBox("Conserve file extensions")
        checkboxLayout = QtGui.QHBoxLayout()
        checkboxLayout.addStretch(1)
        checkboxLayout.addWidget(self.checkboxConserve)
        
        #The button to start renaming
        renameButton = QtGui.QPushButton('Rename!')
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(renameButton)
        
        vertical = QtGui.QVBoxLayout()
        vertical.addWidget(self.dirView)
        vertical.addSpacing(10)
        vertical.addWidget(listPathLabel)
        vertical.addWidget(self.listPathEdit)
        vertical.addSpacing(10)
        vertical.addWidget(startLabel)
        vertical.addWidget(self.startEdit)
        vertical.addSpacing(10)
        vertical.addWidget(prefixLabel)
        vertical.addWidget(self.prefixEdit)
        vertical.addSpacing(10)
        vertical.addWidget(postfixLabel)
        vertical.addWidget(self.postfixEdit)
        vertical.addSpacing(10)
        vertical.addLayout(checkboxLayout)
        vertical.addSpacing(20)
        vertical.addLayout(buttonsLayout)
        
        self.setLayout(vertical)
        
        #If the button is clicked start the renaming
        self.connect(renameButton, QtCore.SIGNAL('clicked()'), self.rename)
    
    def rename(self):
        selectedIndex = self.dirView.selectedIndexes()
        
        if self.listPathEdit.text() == "":
            if self.verbose:
                print "Read the whole directory"
            
            files = os.listdir(self.dirModel.filePath(selectedIndex[0]))
        
        elif (not self.listPathEdit.text() == "") and os.path.isfile(self.listPathEdit.text()):
            if self.verbose:
                print "Read filenames from %s" % self.listPathEdit.text()
            
            files = [i.rstrip('\n') for i in open(self.listPathEdit.text(), "r")]
        
        else:
            print "Path to list doesn't exist or is not a file!"
        
        if not self.startEdit.text() == "":
            start = int(self.startEdit.text())
        
        else:
            start = 1
        
        prefix = self.prefixEdit.text()
        postfix = self.postfixEdit.text()
        
        if self.checkboxConserve.isChecked():
            conserve = True
        else:
            conserve = False
        
        if self.verbose:
            print "Start: %d\n Prefix: %s\n Postfix: %s\n Conserve: %s" % (start, prefix, postfix, conserve)
            print "Change directory"
        
        os.chdir(self.dirModel.filePath(selectedIndex[0]))
        
        rename_files(start, prefix, postfix, conserve, self.verbose, files)
        
    def closeEvent(self, event):
        exit()
    
def graphicalmode(args, options):
    if options.verbose:
        print "Initialize the application"
    
    app = QtGui.QApplication(args)
    
    if options.verbose:
        print "Create the window"
    
    mainWindow = MainWindow(options.verbose)
    mainWindow.show()
    
    if options.verbose:
        print "Start the application"
    
    exit(app.exec_())
