import os

from PyQt5 import QtWidgets
from tt1 import Ui_MainWindow
import sys
from programm import analise


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку")[0]
        d = analise.genre_distribution(directory)
        for i,j in d.items():
            self.listWidget.addItem(f'{i}: {j}, aboba')



app = QtWidgets.QApplication([])
application = Mywindow()
application.show()

sys.exit(app.exec())

# pyuic5 GUI/untitled.ui -o GUI/tt1.py