import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout)
from PyQt6.QtGui import QColor, QPalette

class CaixaCor (QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)




class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Distintos tamaños")

        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        principal = QHBoxLayout()

        pCol1 = QVBoxLayout()
        pCol1.addWidget(CaixaCor("red"))
        pCol1.addWidget(CaixaCor("yellow"))
        pCol1.addWidget(CaixaCor("purple"))

        pCol2 = QVBoxLayout()
        pCol2.addWidget(CaixaCor("green"))

        pCol3 = QVBoxLayout()
        pCol3.addWidget(CaixaCor("red"))
        pCol3.addWidget(CaixaCor("purple"))

        principal.addLayout(pCol1)
        principal.addLayout(pCol2)
        principal.addLayout(pCol3)

        contenedor = QWidget()
        contenedor.setLayout(principal)
        self.setCentralWidget(contenedor)

        self.show()

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()