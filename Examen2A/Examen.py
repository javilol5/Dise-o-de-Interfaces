import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from modeloTabla import ModeloTabla


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen")

        self.setMinimumSize(622, 200)
        self.setMaximumSize(1000, 1000)

        self.datosTop = ["Num Cliente", "Nome", "Apelidos", "Direccion", "Cidade", "Provincia"]

        self.datos = [("1", "Ana", "Perez Diz", "dir1", "Vigo", "Pontevedra"),
                      ("2", "Luis", "Xil Novas", "dir2", "Tui", "Pontevedra"),
                      ("3", "Anxo", "Rois Chan", "dir3", "Pontevedra", "Pontevedra")]

        caixaV = QVBoxLayout()



        grid = QGridLayout()


        cliente = QLabel("Cliente")
        grid.addWidget(cliente,0,0)

        novo_cliente = QLabel("Novo Cliente")
        grid.addWidget(novo_cliente,1,0)
        self.novo_cliente_txt = (QComboBox())

        for n in self.datos:
            self.novo_cliente_txt.addItem(n[0])

        self.novo_cliente_txt.setCurrentIndex(-1)
        grid.addWidget(self.novo_cliente_txt,1,1)
        nome = QLabel("Nome")
        grid.addWidget(nome,1,2)
        self.nome_txt = QLineEdit()
        grid.addWidget(self.nome_txt,1,3)

        #apelidos = QLabel("Apelidos")
        #grid.addWidget(apelidos,2,0)
        #self.apelido1 = QLineEdit()
        #grid.addWidget(self.apelido1,2,1)
        #self.apelido2 = QLineEdit()
        #grid.addWidget(self.apelido2,2,3)

        apellidoGeneral = QLabel("Apelidos")
        grid.addWidget(apellidoGeneral,2,0)
        self.apellidoGeneral_txt = QLineEdit()
        grid.addWidget(apellidoGeneral,2,1,1,3)

        direccion = QLabel("Direccion")
        grid.addWidget(direccion,3,0)
        self.direccion_txt = QLineEdit()
        grid.addWidget(self.direccion_txt,3,1,1,3)

        cidade = QLabel("Cidade")
        grid.addWidget(cidade, 4, 0)
        self.cidade_txt = QLineEdit()
        grid.addWidget(self.cidade_txt, 4, 1)
        provincia = QLabel("Provincia")
        grid.addWidget(provincia, 4, 2)
        self.provincia_txt = QLineEdit()
        grid.addWidget(self.provincia_txt,4,3)

        self.engadir = QPushButton("Engadir")
        grid.addWidget(self.engadir,2,4)
        self.editar = QPushButton("Editar")
        grid.addWidget(self.editar, 3,4)
        self.editar.setEnabled(False)
        self.borrar = QPushButton("Borrar")
        grid.addWidget(self.borrar, 4,4)
        self.borrar.setEnabled(False)



        caixaV.addLayout(grid)



        self.modelo = ModeloTabla(self.datos, self.datosTop)

        self.tvwTaboa = QTableView()
        self.tvwTaboa.setModel(self.modelo)

        caixaV.addWidget(self.tvwTaboa)

        gridButton = QGridLayout()
        espacio = QLabel("")
        gridButton.addWidget(espacio,0,0,1,4)

        self.cancelar = QPushButton("Cancelar")
        gridButton.addWidget(self.cancelar,0,4)
        self.aceptar = QPushButton("Aceptar")
        gridButton.addWidget(self.aceptar,0,5)

        caixaV.addLayout(gridButton)


        contenedor = QWidget()
        contenedor.setLayout(caixaV)
        self.setCentralWidget(contenedor)

        self.show()

        self.novo_cliente_txt.currentIndexChanged.connect(self.cargar_usuario)
        self.aceptar.clicked.connect(self.btnAceptar_clicked)


    def cargar_usuario(self):
        index = self.novo_cliente_txt.currentIndex()
        nome = self.datos[index][1]
        #apelidos = self.datos[index][2]

        #apelido1,apelido2 = apelidos.split(' ')

        apelidoGeneral = self.datos[index][2]

        direccion = self.datos[index][3]
        cidade = self.datos[index][4]
        provincia = self.datos[index][5]

        self.nome_txt.setText(nome)
        #self.apelido1.setText(apelido1)
        #self.apelido2.setText(apelido2)

        self.apellidoGeneral_txt.setText(apelidoGeneral)

        self.direccion_txt.setText(direccion)
        self.cidade_txt.setText(cidade)
        self.provincia_txt.setText(provincia)

        self.modelo.layoutChanged.emit()

    def btnAceptar_clicked(self):


        id = len(self.datos)+1
        nome = self.nome_txt.text()
        #apelido1 = self.apelido1.text()
        #apelido2 = self.apelido2.text()
        #apelido = (self.apelido1.text() + " " + self.apelido2.text())

        apelidoGeneral = self.apellidoGeneral_txt.text()

        direccion = self.direccion_txt.text()
        cidade = self.cidade_txt.text()
        provincia = self.provincia_txt.text()

        if nome == "" or nome == "ERROR":
            self.nome_txt.setText("ERROR")
        #elif apelido1 == "" or apelido == "ERROR":
            #self.apelido1.setText("ERROR")
        #elif apelido2 == "" or apelido == "ERROR":
            #self.apelido2.setText("ERROR")

        elif apelidoGeneral == "" or apelidoGeneral == "ERROR":
            self.apellidoGeneral_txt.setText("ERROR")
        elif direccion == "" or direccion == "ERROR":
            self.direccion_txt.setText("ERROR")
        elif cidade == "" or cidade == "ERROR":
            self.cidade_txt.setText("ERROR")
        elif provincia == "" or provincia == "ERROR":
            self.provincia_txt.setText("ERROR")
        else:
            #self.datos.append((id, nome, apelido, direccion, cidade, provincia))

            self.datos.append((id, nome, apelidoGeneral, direccion, cidade, provincia))

            self.nome_txt.clear()
            #self.apelido1.clear()
            #self.apelido2.clear()

            self.apellidoGeneral_txt.clear()

            self.direccion_txt.clear()
            self.cidade_txt.clear()
            self.provincia_txt.clear()

            self.novo_cliente_txt.addItem(str(id))

            self.modelo.layoutChanged.emit()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
