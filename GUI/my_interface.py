import sys
from GUI import tools_for_output as tools
from PyQt5 import QtWidgets
from GUI.first_qt import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from program import analise, converting


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
        self.label.clear()
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.label_5.clear()

    def browse_folder(self):

        self.directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл","","Text files(*.txt);; Pdf files(*.pdf)")[0]
        self.directory = converting.choice(self.directory)
        if self.directory:
            analise.words_distribution(self.directory)
            self.__draw_pie(100)
            self.__write_name()
            self.__print_words(100)
            self.__print_difficults()

    def __draw_pie(self, border):
        d = analise.genre_distribution(border)
        self.verticalLayout_1.removeWidget(self.canvas_p)
        self.canvas_p = PieCanvas(tools.circle_plot(d))
        self.verticalLayout_1.addWidget(self.canvas_p)
        self.label_3.setText('Диаграмма распределения жанров:')

    def __write_name(self):
        new_name = self.directory.replace('-', ' ').replace('_', ' ')
        new_name = new_name.split('/')[-1]
        new_name = new_name.split("\\")[-1]
        new_name = new_name.split('.txt')[0]
        self.label.setText(f"Название книги: {new_name}")

    def __print_words(self, n):
        self.listWidget.clear()
        self.label_2.setText(f'Топ {n} самых встречающихся слов:')
        for i in tools.get_lines(n, 5):
            self.listWidget.addItem(i)
        self.listWidget_2.clear()
        self.label_4.setText(f'Топ {n} самых встречающихся "сложных" слов:')
        for i in tools.get_lines(n, 5, True):
            self.listWidget_2.addItem(i)

    def __print_difficults(self):
        self.label_5.setText(analise.difficult())



def run():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())

# pyuic5 GUI/untitled.ui -o GUI/first_qt.py
