import sys
from GUI import tools_for_output as tools
from PyQt5 import QtWidgets
from GUI.first_qt import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from program import analise
from PyQt5 import QtGui

class PieCanvas(FigureCanvasQTAgg):
    def __init__(self, fig=None):
        super(PieCanvas, self).__init__(fig)



class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)
        self.canvas_p = None
        self.directory = ''

    def browse_folder(self):
        self.directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку")[0]
        if self.directory:
            analise.words_distribution(self.directory)
            self.__draw_pie()
            self.__write_name()
            self.__print_words()

    def __draw_pie(self):
        d = analise.genre_distribution(self.directory)
        self.verticalLayout_1.removeWidget(self.canvas_p)
        self.canvas_p = PieCanvas(tools.circle_plot(d))
        self.verticalLayout_1.addWidget(self.canvas_p)

    def __write_name(self):
        new_name = self.directory.replace('-', ' ').replace('_', ' ')
        new_name = new_name.split('/')[-1]
        new_name = new_name.split('.txt')[0]
        self.label.setText(new_name)

    def __print_words(self):
        for i in tools.get_lines():
            self.listWidget.addItem(i)



def run():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())

# pyuic5 GUI/untitled.ui -o GUI/first_qt.py
