import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import *

class VoiceAsistentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Agent Smith')
        self.setGeometry(420, 70, 600, 660)







def application():
    app = QApplication(sys.argv)
    window = VoiceAsistentWindow()
    window.show()
    sys.exit(app.exec_())


application()