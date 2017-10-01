import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5 import uic

title = ['A입력','B입력','C입력']

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("list.ui", self)

        title = ['A입력', 'B입력', 'C입력']

        for i in range(len(title)):
           item = QListWidgetItem(title[i])
           self.listWindow.addItem(item)

        self.ui.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())