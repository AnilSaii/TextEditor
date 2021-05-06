from gui import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import sys, os

class logic(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Make a variable to hold FilePath
        self.PathOfFile = None

        # Code Goes Here
        # Create object of the ui class
        self.MyObject = Ui_MainWindow()
        self.MyObject.setupUi(self)


        # NewFile
        self.MyObject.actionNew.triggered.connect(self.NewFile)

        # OpenFile
        self.MyObject.actionOpen.triggered.connect(self.OpenFile)

        # SaveFile
        self.MyObject.actionSave.triggered.connect(self.SaveFile)

        # Quit Application
        self.MyObject.actionQuit.triggered.connect(self.Quit)

        # Cut
        self.MyObject.actionCut.triggered.connect(self.Cut)

        # Copy
        self.MyObject.actionCopy.triggered.connect(self.Copy)

        # Paste
        self.MyObject.actionPaste.triggered.connect(self.Paste)

        # Undo
        self.MyObject.actionUndo.triggered.connect(self.Undo)

        # Redo
        self.MyObject.actionRedo.triggered.connect(self.Redo)

        # Font
        self.MyObject.actionFont.triggered.connect(self.Font)

        # Font Colour
        self.MyObject.actionFont_Colour.triggered.connect(self.FontColour)

        # ZoomIn
        self.MyObject.actionZoom_In.triggered.connect(self.ZoomIn)

        # ZoomOut
        self.MyObject.actionZoom_Out.triggered.connect(self.ZoomOut)

        # Contact
        self.MyObject.actionContact.triggered.connect(self.Contact)

        # About
        self.MyObject.actionAbout.triggered.connect(self.About)

        self.show()

    # New File
    def NewFile(self):
        filepath, _ = qtw.QFileDialog.getSaveFileName(self, "Save File", "/home/anilsaidonga/Documents", "All Files(*)")
        if filepath:
            f = open(filepath, "w")
            self.PathOfFile = filepath
            filename = os.path.basename(filepath)
            self.setWindowTitle("Text Editor - " + filename)
            self.MyObject.statusbar.showMessage(filepath)
        else:
            qtw.QMessageBox.information(self, "File Not Saved!", "File is not saved, save file before quitting")
            self.setWindowTitle("Text Editor - *unnamed")
            self.MyObject.statusbar.showMessage("*New File")

    # Open File
    def OpenFile(self):
        filepath, _ = qtw.QFileDialog.getOpenFileName(self, "Open File", "/home/anilsaidonga/Documents", "All Files(*)")
        if filepath:
            f = open(filepath, "r")
            self.PathOfFile = filepath
            filename = os.path.basename(filepath)
            self.setWindowTitle("Text Editor - " + filename)
            with f:
                FileContent = f.read()
                self.MyObject.textEdit.setText(FileContent)
            self.MyObject.statusbar.showMessage(filepath)
        else:
            qtw.QMessageBox.information(self, "Invalid File Selected!", "No file is selected!")
            if self.PathOfFile == None:
                self.setWindowTitle("Text Editor - *unamed")
            #self.MyObject.statusbar.showMessage("File-Path : *unknown")

    # Save File
    def SaveFile(self):
        if self.PathOfFile != None:
            f = open(self.PathOfFile, "w")
            with f:
                FileContent = self.MyObject.textEdit.toPlainText()
                f.write(FileContent)
            #qtw.QMessageBox.information(self, "File Saved", "File is Saved Successfully")
            self.MyObject.statusbar.showMessage(self.PathOfFile + " (Saved)")
        else:
            filepath, _ = qtw.QFileDialog.getSaveFileName(self, "Save File", "/home/anilsaidonga/Documents", "All Files(*)")
            if filepath:
                f = open(filepath, "w")
                self.PathOfFile = filepath
                filename = os.path.basename(filepath)
                self.setWindowTitle("Text Editor - " + filename)
                with f:
                    FileContent = self.MyObject.textEdit.toPlainText()
                    f.write(FileContent)
                    #qtw.QMessageBox.information(self, "File Saved", "File is Saved Successfully")
                self.MyObject.statusbar.showMessage(filepath + " (Saved)")

    def Quit(self):
        if self.PathOfFile == None:

            if self.MyObject.textEdit.toPlainText() != "":
                messageBox = qtw.QMessageBox()
                title = "Quit Application ?"
                message = "WARNING !!\n\nIf you quit without saving, any changes made to the file will be lost.\n\nSave file before quitting?"
                reply = messageBox.question(self, title, message, messageBox.Yes | messageBox.No | messageBox.Cancel)
                if reply == messageBox.Yes:
                    self.SaveFile()
                    self.close()
                elif reply == messageBox.No:
                    self.close()
                else:
                    pass

            self.close()

        else:
            messageBox = qtw.QMessageBox()
            title = "Quit Application?"
            message = "WARNING !!\n\nIf you quit without saving, any changes made to the file will be lost.\n\nSave file before quitting?"
       
            reply = messageBox.question(self, title, message, messageBox.Yes | messageBox.No |
                    messageBox.Cancel, messageBox.Cancel)
            if reply == messageBox.Yes:
                self.SaveFile()
                self.close()
            elif reply == messageBox.No:
                self.close()
            else:
                pass

    # Cut
    def Cut(self):
        self.MyObject.textEdit.cut()

    # Copy
    def Copy(self):
        self.MyObject.textEdit.copy()

    # Paste
    def Paste(self):
        self.MyObject.textEdit.paste()

    # Undo
    def Undo(self):
        self.MyObject.textEdit.undo()

    # Redo
    def Redo(self):
        self.MyObject.textEdit.redo()

    # Font
    def Font(self):
        Font, valid = qtw.QFontDialog.getFont()
        if valid:
            self.MyObject.textEdit.setFont(Font)

    # Font Colour
    def FontColour(self):
        FontColour = qtw.QColorDialog.getColor()
        if FontColour.isValid():
            self.MyObject.textEdit.setTextColor(FontColour)

    # ZoomIn
    def ZoomIn(self):
        self.MyObject.textEdit.zoomIn()

    # ZoomOut
    def ZoomOut(self):
        self.MyObject.textEdit.zoomOut()

    # Contact
    def Contact(self):
        qtw.QMessageBox.information(self, "Contact", "Contact me at anilsaidonga777@gmail.com")

    # About
    def About(self):
        qtw.QMessageBox.information(self, "About", "Text Editor is a open-source application\n\nHonestly, i don't know what to say\n\nThis Text Editor is built by copying from many sources\n\nOop's that came out wrong\n\nAnyway have a niceday")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    obj = logic()
    sys.exit(app.exec_())