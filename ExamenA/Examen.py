import sys
import math

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QListView, QRadioButton, QComboBox, QGridLayout, QStackedLayout, QCheckBox,
                             QDial, QTextEdit, QAbstractSlider)
from PyQt6.QtGui import QColor, QPalette


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ExamenA")

        self.setMinimumSize(100, 100)
        self.setMaximumSize(1000, 1000)

        maia = QVBoxLayout()

        self.selec = QComboBox()
        self.selec.addItems(["Configuración zoa 1", "Zoa 2", "Consola"])
        self.selec.setCurrentIndex(0)



        maia.addWidget(self.selec)

        #CONFIGURACION

        conf = QWidget()
        pantalla_conf = QGridLayout()


        self.activada = QLabel("Activada")
        pantalla_conf.addWidget(self.activada,0,0)

        self.checkbox = QCheckBox()
        pantalla_conf.addWidget(self.checkbox,0,1)

        self.opcions = QLabel("Opcions")
        pantalla_conf.addWidget(self.opcions,0,2)


        self.hora_rego = QLabel("Hora de comenzo do rego")
        pantalla_conf.addWidget(self.hora_rego,1,0)

        self.text = QLineEdit()
        pantalla_conf.addWidget(self.text,1,1)

        vertical = QVBoxLayout()

        self.diario = QRadioButton("Diario")
        self.semanal = QRadioButton("Semanal")
        self.antixiada = QCheckBox("Antixiada")
        self.chuvia = QCheckBox("Chuvia")

        vertical.addWidget(self.diario)
        vertical.addWidget(self.semanal)
        vertical.addWidget(self.antixiada)
        vertical.addWidget(self.chuvia)

        pantalla_conf.addLayout(vertical,1,2,1,3)


        self.duracion_rego = QLabel("Duracion rego")
        pantalla_conf.addWidget(self.duracion_rego,2,0)

        self.dial = QDial()
        self.dial.setRange(0,400)
        pantalla_conf.addWidget(self.dial,2,1)

        self.dias = QLabel("Dias")
        pantalla_conf.addWidget(self.dias,3,0)


        horizontal = QHBoxLayout()

        self.checkboxL = QCheckBox("Lunes")
        self.checkboxM = QCheckBox("Martes")
        self.checkboxX = QCheckBox("Miercoles")
        self.checkboxJ = QCheckBox("Jueves")
        self.checkboxV = QCheckBox("Viernes")
        self.checkboxS = QCheckBox("Sabado")
        self.checkboxD = QCheckBox("Domingo")



        horizontal.addWidget(self.checkboxL)
        horizontal.addWidget(self.checkboxM)
        horizontal.addWidget(self.checkboxX)
        horizontal.addWidget(self.checkboxJ)
        horizontal.addWidget(self.checkboxV)
        horizontal.addWidget(self.checkboxS)
        horizontal.addWidget(self.checkboxD)

        pantalla_conf.addLayout(horizontal,4,0,1,3)


        self.aceptar = QPushButton("Aceptar")
        pantalla_conf.addWidget(self.aceptar,5,2)






        conf.setLayout(pantalla_conf)


        self.checkbox.stateChanged.connect(self.activarZoa)
        self.activarZoa(0)

        self.dial.valueChanged.connect(self.textoRego)

        self.text.returnPressed.connect(self.comporbarHora)

        self.aceptar.clicked.connect(self.activarAceptar)



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

        #Apilado

        self.tarxetas = QStackedLayout()

        self.tarxetas.addWidget(conf)
        self.tarxetas.addWidget(zoa)
        self.tarxetas.addWidget(consola)

        maia.addLayout(self.tarxetas)

        contenedor = QWidget()
        contenedor.setLayout(maia)

        self.setCentralWidget(contenedor)

        self.selec.currentIndexChanged.connect(self.cambiarFormulario)

        self.tarxetas.setCurrentIndex(0)
        self.tarxetas.currentWidget().hide()

        self.cambiarFormulario(0)

    def cambiarFormulario(self, indice):
        self.tarxetas.currentWidget().show()
        self.tarxetas.setCurrentIndex(indice)
        self.tarxetas.currentWidget().show()


    def activarZoa(self, estado):
        if estado == 2:

            self.hora_rego.setEnabled(True)
            self.text.setEnabled(True)
            self.diario.setEnabled(True)
            self.semanal.setEnabled(True)
            self.antixiada.setEnabled(True)
            self.chuvia.setEnabled(True)
            self.dial.setEnabled(True)
            self.checkboxL.setEnabled(True)
            self.checkboxM.setEnabled(True)
            self.checkboxX.setEnabled(True)
            self.checkboxJ.setEnabled(True)
            self.checkboxV.setEnabled(True)
            self.checkboxS.setEnabled(True)
            self.checkboxD.setEnabled(True)
            self.aceptar.setEnabled(True)

        else:

            self.hora_rego.setEnabled(False)
            self.text.setEnabled(False)
            self.diario.setEnabled(False)
            self.semanal.setEnabled(False)
            self.antixiada.setEnabled(False)
            self.chuvia.setEnabled(False)
            self.dial.setEnabled(False)
            self.checkboxL.setEnabled(False)
            self.checkboxM.setEnabled(False)
            self.checkboxX.setEnabled(False)
            self.checkboxJ.setEnabled(False)
            self.checkboxV.setEnabled(False)
            self.checkboxS.setEnabled(False)
            self.checkboxD.setEnabled(False)
            self.aceptar.setEnabled(False)

    def textoRego(self, estado):
        self.duracion_rego.setText("Duracion Rego " + str(estado))

    def comporbarHora(self):

        hora = self.text.text()

        if len(hora) != 5 or hora[2] != ":":
            self.texto.setText(self.texto.toPlainText() + hora + "\nError, formato invalido\n")
        else:
            try:
                horas = int(hora[0] + hora[1])
                minutos = int(hora[3] + hora[4])

                if horas > 23 or minutos > 59:
                    self.texto.setText(self.texto.toPlainText() + hora + "\nError, formato invalido\n")
                else:
                    self.texto.setText(self.texto.toPlainText() + hora + "\nCorrecto\n")

            except ValueError:
                self.texto.setText(self.texto.toPlainText() + hora + "\nError, formato invalido\n")

    def activarAceptar(self):


        num_zona = "Zona 1"
        hora_comezo = self.text.text()
        duracion = self.duracion_rego.text()
        dias = ""
        if self.checkboxL.isChecked():
            dias += "L "
        if self.checkboxM.isChecked():
            dias += "M "
        if self.checkboxX.isChecked():
            dias += "X "
        if self.checkboxJ.isChecked():
            dias += "J "
        if self.checkboxV.isChecked():
            dias += "V "
        if self.checkboxS.isChecked():
            dias += "S "
        if self.checkboxD.isChecked():
            dias += "D "

        opcions = ""

        if self.diario.isChecked():
            opcions += "Diario "
        if self.semanal.isChecked():
            opcions += "Semana "
        if self.antixiada.isChecked():
            opcions += "Antixiada "
        if self.chuvia.isChecked():
            opcions += "Chuvia "

        self.texto.setText(self.texto.toPlainText() + num_zona + "\n" + hora_comezo + "\n" + duracion + "\n" + dias + "\n" + opcions)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())