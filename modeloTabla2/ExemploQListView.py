import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from modeloTabla import ModeloTabla


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fiesta Principal")

        self.setMinimumSize(425, 200)
        self.setMaximumSize(1000, 1000)

        caixaV = QVBoxLayout()

        self.datos = [("Nome","DNI","Xenero","Falecimiento"),
                      ("Ana Perez","1111R","Muller",False),
                      ("Paco Porras","2222T","Home",True),
                      ("Roque Vila","3333H","Home",False)]

        self.modelo = ModeloTabla(self.datos)

        self.tvwTaboa = QTableView()
        self.tvwTaboa.setModel(self.modelo)

        caixaV.addWidget(self.tvwTaboa)

        grid = QGridLayout()


        nuevo = QLabel("Nuevo Usuario")
        grid.addWidget(nuevo,0,0)

        nome = QLabel("Nome")
        grid.addWidget(nome,1,0)
        self.nome_txt = QLineEdit()
        grid.addWidget(self.nome_txt,1,1,1,2)

        dni = QLabel("DNI")
        grid.addWidget(dni,2,0)
        self.dni_txt = QLineEdit()
        grid.addWidget(self.dni_txt,2,1,1,2)

        xenero = QLabel("Xenero")
        grid.addWidget(xenero,3,0)
        self.xeneros = QComboBox()
        self.xeneros.addItems(("Muller","Home","Outro"))
        self.xeneros.setCurrentIndex(-1)
        grid.addWidget(self.xeneros,3,1)
        self.fallecido = QCheckBox("Falecimiento")
        grid.addWidget(self.fallecido,3,2)

        self.aceptar = QPushButton("Aceptar")
        grid.addWidget(self.aceptar,4,1)
        self.cancelar = QPushButton("Cancelar")
        grid.addWidget(self.cancelar,4,2)



        caixaV.addLayout(grid)


        contenedor = QWidget()
        contenedor.setLayout(caixaV)
        self.setCentralWidget(contenedor)

        self.show()

        self.aceptar.clicked.connect(self.btnAceptar_clicked)
        self.cancelar.clicked.connect(self.btnCancelar_clicked)


    def btnAceptar_clicked(self):
        nome = self.nome_txt.text()
        dni = self.dni_txt.text()
        xenero = self.xeneros.currentText()
        fallecido = self.fallecido.isChecked()

        if nome != "" and dni != "" and xenero != "":
            self.datos.append((nome,dni,xenero,fallecido))

            self.nome_txt.clear()
            self.dni_txt.clear()
            self.xeneros.setCurrentIndex(-1)
            self.fallecido.setChecked(fallecido)

            self.modelo.layoutChanged.emit()

    def btnCancelar_clicked(self):
        self.nome_txt.clear()
        self.dni_txt.clear()
        self.xeneros.setCurrentIndex(-1)
        self.fallecido.setChecked(False)

        self.modelo.layoutChanged.emit()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
