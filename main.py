import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication



if '__main__' == __name__:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())