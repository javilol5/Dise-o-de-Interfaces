import sys
import math

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QColor, QPalette


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ExamenB")

        self.setMinimumSize(100, 100)
        self.setMaximumSize(1000, 1000)

        maia = QVBoxLayout()




        #CONFIGURACION

        conf = QWidget()
        pantalla_conf = QGridLayout()


        self.activada = QLabel("Activada")
        pantalla_conf.addWidget(self.activada,0,0)

        self.checkbox = QCheckBox()
        pantalla_conf.addWidget(self.checkbox,0,1)


        self.hora_rego = QLabel("Hora de comenzo do rego")
        pantalla_conf.addWidget(self.hora_rego,1,0)

        self.text = QLineEdit()
        pantalla_conf.addWidget(self.text,1,1)

        vertical = QVBoxLayout()

        dias = QLabel("Dias")
        vertical.addWidget(dias)

        verticalGrid = QGridLayout()

        self.checkboxL = QCheckBox("Lunes")
        self.checkboxM = QCheckBox("Martes")
        self.checkboxX = QCheckBox("Miercoles")
        self.checkboxJ = QCheckBox("Jueves")
        self.checkboxV = QCheckBox("Viernes")
        self.checkboxS = QCheckBox("Sabado")
        self.checkboxD = QCheckBox("Domingo")

        verticalGrid.addWidget(self.checkboxL,0,0)
        verticalGrid.addWidget(self.checkboxM,0,1)
        verticalGrid.addWidget(self.checkboxX,1,0)
        verticalGrid.addWidget(self.checkboxJ,1,1)
        verticalGrid.addWidget(self.checkboxV,2,0)
        verticalGrid.addWidget(self.checkboxS,2,1)
        verticalGrid.addWidget(self.checkboxD,3,0)

        vertical.addLayout(verticalGrid)

        self.aceptar = QPushButton("Aceptar")
        vertical.addWidget(self.aceptar)



        pantalla_conf.addLayout(vertical,2,3)


        self.duracion_rego = QLabel("Duracion Rego 0")
        pantalla_conf.addWidget(self.duracion_rego,2,0)

        self.slide = QSlider(Qt.Orientation.Horizontal)
        self.slide.setRange(0,600)
        pantalla_conf.addWidget(self.slide,2,1)

        self.opcions = QLabel("Opcions")
        pantalla_conf.addWidget(self.opcions,3,0)


        horizontal = QHBoxLayout()

        self.antixiada = QCheckBox("Antixiada")
        self.chuvia = QCheckBox("Chuvia")

        self.dropMenu = QComboBox()
        self.dropMenu.addItems(["Semanal","Diario"])
        self.dropMenu.setCurrentIndex(0)


        horizontal.addWidget(self.dropMenu)
        horizontal.addWidget(self.antixiada)
        horizontal.addWidget(self.chuvia)



        pantalla_conf.addLayout(horizontal,4,0,1,3)



        pantalla_conf.addWidget(self.aceptar,5,2)



        conf.setLayout(pantalla_conf)






        #ZOA 2

        zoa = QWidget()
        pantalla_zoa = QGridLayout()


        etiqueta = QLabel("Etiqueta")
        pantalla_zoa.addWidget(etiqueta,0,0)

        zoa.setLayout(pantalla_zoa)



        #CONSOLA
        consola = QWidget()
        pantalla_consola = QGridLayout()

        self.texto = QTextEdit()
        pantalla_consola.addWidget(self.texto,0,0)

        consola.setLayout(pantalla_consola)



        #BOTONES

        botones = QHBoxLayout()
        self.conf1 = QPushButton("Configuracion 1")
        self.conf2 = QPushButton("Configuracion 2")
        self.console = QPushButton("Consola")

        botones.addWidget(self.conf1)
        botones.addWidget(self.conf2)
        botones.addWidget(self.console)

        self.conf1.clicked.connect(self.mostrarConf1)
        self.conf2.clicked.connect(self.mostrarConf2)
        self.console.clicked.connect(self.mostrarConsola)


        #Apilado

        self.tarxetas = QStackedLayout()

        self.tarxetas.addWidget(conf)
        self.tarxetas.addWidget(zoa)
        self.tarxetas.addWidget(consola)

        maia.addLayout(self.tarxetas)
        maia.addLayout(botones)

        contenedor = QWidget()
        contenedor.setLayout(maia)

        self.setCentralWidget(contenedor)


        #ACCIONES

        self.checkbox.stateChanged.connect(self.printActivada)
        self.slide.valueChanged.connect(self.textoRego)
        self.dropMenu.currentIndexChanged.connect(self.bloquear)

    def printActivada(self):
        self.texto.setText(self.texto.toPlainText() + "Zoa activada\n")

    def textoRego(self, estado):
        self.duracion_rego.setText("Duracion Rego " + str(estado))

    def bloquear(self, index):
        if index == 0:


            self.checkboxL.setEnabled(False)
            self.checkboxM.setEnabled(False)
            self.checkboxX.setEnabled(False)
            self.checkboxJ.setEnabled(False)
            self.checkboxV.setEnabled(False)
            self.checkboxS.setEnabled(False)
            self.checkboxD.setEnabled(False)
        else:
            self.checkboxL.setEnabled(True)
            self.checkboxM.setEnabled(True)
            self.checkboxX.setEnabled(True)
            self.checkboxJ.setEnabled(True)
            self.checkboxV.setEnabled(True)
            self.checkboxS.setEnabled(True)
            self.checkboxD.setEnabled(True)



    def mostrarConf1(self):
        self.tarxetas.setCurrentIndex(0)

    def mostrarConf2(self):
        self.tarxetas.setCurrentIndex(1)

    def mostrarConsola(self):
        self.tarxetas.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())