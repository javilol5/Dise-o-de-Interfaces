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

        caixaV = QVBoxLayout()

        boton = QPushButton("Saudar")
        etiqueta = QLabel("Ola a todos")
        cadroTexto = QLineEdit()
        cadroTexto.setPlaceholderText("Escribe o teu nome")

        etiqueta.setText("Otro texto")
        cadroTexto.setPlaceholderText("Tamen o podo modificar con outro texto")
        print(etiqueta.text())
        print(cadroTexto.text())

        caixaV.addWidget(etiqueta)
        caixaV.addWidget(cadroTexto)
        caixaV.addWidget(boton)

        def on_button_clicked(self):
            nome = cadroTexto.text()
            if len(nome) != 0:
                etiqueta.setText("Ola " + cadroTexto.text())
            else:
                etiqueta.setText("Introduce un nombre valido")

        boton.clicked.connect(on_button_clicked)

        contedor = QWidget()
        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)

        self.show()

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()