import sys
from GUI import diagrams
from PyQt5 import QtWidgets
from GUI.first_qt import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from programm import analise


class PieCanvas(FigureCanvasQTAgg):
    def __init__(self, fig):
        super(PieCanvas, self).__init__(fig)



class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        # self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку")[0]
        d = analise.genre_distribution(directory)
        canvas_p = PieCanvas(diagrams.circle_plot(d))
        self.verticalLayout_1.addWidget(canvas_p)





def run():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())

# pyuic5 GUI/untitled.ui -o GUI/first_qt.py
