import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QComboBox, QStackedLayout, QGridLayout, QRadioButton)
from PyQt6.QtGui import QColor, QPalette

from time import sleep

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStakedLayout")

        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        maia = QGridLayout()


        self.ciclo = QLabel("Ciclo")

        self.cmbTipo = QComboBox()
        self.cmbTipo.addItems(["DAM","DAW","ASIR","SMR"])
        self.cmbTipo.setCurrentIndex(-1) #-1 para q no empiece con ninguno seleccionado

        self.radioButton1 = QRadioButton()
        self.radioButton1.setText("Primero")
        self.radioButton2 = QRadioButton()
        self.radioButton2.setText("Segundo")

        self.anoMatricula = QLabel("Ano Matricula")

        self.ano = QComboBox()
        self.ano.addItems(["20-21","21-22","22-23","23-24","24-25","25-26","26-27"])
        self.ano.setCurrentIndex(-1)  # -1 para q no empiece con ninguno seleccionado

        self.nai = QLabel("Nome Nai")

        self.nomeNai = QLineEdit()

        self.pai = QLabel("Nome Pai")

        self.nomePai = QLineEdit()

        maia.addWidget(self.ciclo,0,1)
        maia.addWidget(self.cmbTipo,0,2)
        maia.addWidget(self.radioButton1,1,1)
        maia.addWidget(self.radioButton2,1,2)
        maia.addWidget(self.anoMatricula,2,1)
        maia.addWidget(self.ano,2,2)
        maia.addWidget(self.nai,3,1)
        maia.addWidget(self.nomeNai,3,2)
        maia.addWidget(self.pai,4,1)
        maia.addWidget(self.nomePai,4,2)

        tarxetas = QStackedLayout()

        maia.addLayout(tarxetas,1,2)

        contenedor = QWidget()
        contenedor.setLayout(maia)

        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()