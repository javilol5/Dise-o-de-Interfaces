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

        self.setWindowTitle("Calculadora")

        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 400)

        self.etiqueta = QLabel("")


        principal = QVBoxLayout()

        pPrin = QHBoxLayout()
        #pPrin.addWidget(CaixaCor("gray"))
        pPrin.addWidget(self.etiqueta)

        pRow1 = QHBoxLayout()
        #pRow1.addWidget(QPushButton("⌫"))
        botonDelet = QPushButton("⌫")
        botonDelet.clicked.connect(self.delet)
        pRow1.addWidget(botonDelet)
        pRow1.addWidget(QPushButton("("))
        pRow1.addWidget(QPushButton(")"))
        pRow1.addWidget(QPushButton("mod"))
        pRow1.addWidget(QPushButton("π"))

        pRow2 = QHBoxLayout()
        #pRow2.addWidget(QPushButton("7"))
        boton7 = QPushButton("7")
        boton7.clicked.connect(self.pulsar_boton)
        pRow2.addWidget(boton7)
        #pRow2.addWidget(QPushButton("8"))
        boton8 = QPushButton("8")
        boton8.clicked.connect(self.pulsar_boton)
        pRow2.addWidget(boton8)
        #pRow2.addWidget(QPushButton("9"))
        boton9 = QPushButton("9")
        boton9.clicked.connect(self.pulsar_boton)
        pRow2.addWidget(boton9)
        #pRow2.addWidget(QPushButton("÷"))
        botonDiv = QPushButton("÷")
        botonDiv.clicked.connect(self.pulsar_boton)
        pRow2.addWidget(botonDiv)
        pRow2.addWidget(QPushButton("√"))

        pRow3 = QHBoxLayout()
        #pRow3.addWidget(QPushButton("4"))
        boton4 = QPushButton("4")
        boton4.clicked.connect(self.pulsar_boton)
        pRow3.addWidget(boton4)
        #pRow3.addWidget(QPushButton("5"))
        boton5 = QPushButton("5")
        boton5.clicked.connect(self.pulsar_boton)
        pRow3.addWidget(boton5)
        #pRow3.addWidget(QPushButton("6"))
        boton6 = QPushButton("6")
        boton6.clicked.connect(self.pulsar_boton)
        pRow3.addWidget(boton6)
        #pRow3.addWidget(QPushButton("×"))
        botonPor = QPushButton("×")
        botonPor.clicked.connect(self.pulsar_boton)
        pRow3.addWidget(botonPor)
        pRow3.addWidget(QPushButton("x²"))

        pRow4 = QHBoxLayout()
        #pRow4.addWidget(QPushButton("1"))
        boton1 = QPushButton("1")
        boton1.clicked.connect(self.pulsar_boton)
        pRow4.addWidget(boton1)
        #pRow4.addWidget(QPushButton("2"))
        boton2 = QPushButton("2")
        boton2.clicked.connect(self.pulsar_boton)
        pRow4.addWidget(boton2)
        #pRow4.addWidget(QPushButton("3"))
        boton3 = QPushButton("3")
        boton3.clicked.connect(self.pulsar_boton)
        pRow4.addWidget(boton3)
        #pRow4.addWidget(QPushButton("-"))
        botonMenos = QPushButton("-")
        botonMenos.clicked.connect(self.pulsar_boton)
        pRow4.addWidget(botonMenos)
        #pRow4.addWidget(QPushButton("AC"))
        botonAC = QPushButton("AC")
        botonAC.clicked.connect(self.ac)
        pRow4.addWidget(botonAC)

        pRow5 = QHBoxLayout()
        #pRow5.addWidget(QPushButton("0"))
        boton0 = QPushButton("0")
        boton0.clicked.connect(self.pulsar_boton)
        pRow5.addWidget(boton0)
        pRow5.addWidget(QPushButton("."))
        pRow5.addWidget(QPushButton("%"))
        #pRow5.addWidget(QPushButton("+"))
        botonMas = QPushButton("+")
        botonMas.clicked.connect(self.pulsar_boton)
        pRow5.addWidget(botonMas)
        #pRow5.addWidget(QPushButton("="))
        botonMas = QPushButton("=")
        botonMas.clicked.connect(self.igual)
        pRow5.addWidget(botonMas)

        principal.addLayout(pPrin)
        principal.addLayout(pRow1)
        principal.addLayout(pRow2)
        principal.addLayout(pRow3)
        principal.addLayout(pRow4)
        principal.addLayout(pRow5)

        contenedor = QWidget()
        contenedor.setLayout(principal)
        self.setCentralWidget(contenedor)

        self.show()

    def pulsar_boton(self):
        boton = self.sender()
        self.etiqueta.setText(self.etiqueta.text() + boton.text())
        print(boton.text())

    def ac(self):
        self.etiqueta.setText("")

    def delet(self):
        self.etiqueta.setText(self.etiqueta.text()[0][-1])

    def igual(self):
        num1 = int(self.etiqueta.text()[0])
        num2 = int(self.etiqueta.text()[2])

        if self.etiqueta.text()[1] == "+":
            sol = str(num1 + num2)

        elif self.etiqueta.text()[1] == "-":
            sol = str(num1 - num2)

        elif self.etiqueta.text()[1] == "×":
            sol = str(num1 * num2)

        elif self.etiqueta.text()[1] == "÷":
            sol = str(num1 / num2)

        self.etiqueta.setText(sol)




if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()