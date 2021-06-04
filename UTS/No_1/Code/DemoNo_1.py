import sys
from No_1 import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoNo1(QDialog):
   def __init__(self,parent = None):
        QDialog. __init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.editBttn.clicked.connect(self.editClicked)
        self.ui.tambahBttn.clicked.connect(self.addClicked)
        self.ui.clearBttn.clicked.connect(self.clearClicked)
        self.ui.clearBttn.clicked.connect(self.ui.lineEdit.clear)


   def editClicked(self):
       QMessageBox.information(self, 'Edit', 'Data %s telah diubah!' %self.ui.lineEdit.text())
   def addClicked(self):
       QMessageBox.information(self, 'Add', 'Data %s telah ditambah!' %self.ui.lineEdit.text())
   def clearClicked(self):
       QMessageBox.information(self, 'Clear', 'Data %s telah diclear!' %self.ui.lineEdit.text())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = DemoNo1()
    form.show()
    a.exec_()
