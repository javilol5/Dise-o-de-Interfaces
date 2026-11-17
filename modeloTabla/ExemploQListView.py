import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from modeloTabla import ModeloTabla


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fiesta Principal")

        self.setMinimumSize(200, 200)
        self.setMaximumSize(1000, 1000)

        caixaV = QVBoxLayout()

        datos = [["Nome","DNI","Xenero","Falecimiento"],
                 ["Ana Perez","1111R","Muller",False],
                 ["Paco Porras","2222T","Home",True],
                 ["Roque Vila","3333H","Home",False]]

        self.modelo = ModeloTabla(datos)

        self.tvwTaboa = QTableView()
        self.tvwTaboa.setModel(self.modelo)

        caixaV.addWidget(self.tvwTaboa)

        contenedor = QWidget()
        contenedor.setLayout(caixaV)
        self.setCentralWidget(contenedor)

        self.show()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
