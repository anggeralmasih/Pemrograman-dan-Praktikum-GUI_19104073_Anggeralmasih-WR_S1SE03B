import sys
from DesainGUIDialog import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoQTDesainer2(QDialog) :
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.hallo.clicked.connect(self.halloClicked)

    def halloClicked(self):
        QMessageBox.information(self, 'Demo Qt Desainer',
                                'Halo %s, apa kabar?' %
                                self.ui.namaEdit.text())

if __name__ == "__main__" :
    a = QApplication(sys.argv)
    form = DemoQTDesainer2()
    form.show()
    a.exec()
