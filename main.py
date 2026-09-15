import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout)
from PyQt6.QtGui import QColor, QPalette

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primera aplicacion")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("lightblue"))
        self.setPalette(paleta)




        self.show()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()