from PyQt5.QtWidgets import *
# Sesudah perbaikan
app = QApplication([])

button = QPushButton('Click')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
# Error dibagian ini, indentasinya telah diperbaiki
app.exec_()
