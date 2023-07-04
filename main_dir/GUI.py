import csv
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class VoiceAsistentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Agent Smith')
        self.setGeometry(420, 70, 600, 660)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setCentralWidget(self.scroll_area)

        self.table_widget = QTableWidget(self.scroll_area)
        self.scroll_area.setWidget(self.table_widget)
        self.load_csv_file('commands_data.csv')  # Замените 'data.csv' на путь к вашему CSV-файлу

        # Устанавливаем размеры таблицы и QScrollArea
        self.table_widget.setSizeAdjustPolicy(QTableWidget.AdjustToContents)  # Автоматическое подгонка размера таблицы
        self.scroll_area.setWidgetResizable(True)
        self.resize_table_cells()

    def load_csv_file(self, filename):
        self.table_widget.clear()
        with open(filename, 'r') as file:
            csv_data = csv.reader(file)
            data = list(csv_data)

        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))

        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                self.table_widget.setItem(row_num, col_num, item)

    def resize_table_cells(self):
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()

def application():
    app = QApplication(sys.argv)
    window = VoiceAsistentWindow()
    window.show()
    sys.exit(app.exec_())


application()
