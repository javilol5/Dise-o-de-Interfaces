import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from modeloHorario import ModeloHorario


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fiesta Principal")

        self.setMinimumSize(600, 300)
        self.setMaximumSize(1000, 1000)

        caixaV = QVBoxLayout()

        datosTop = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        datosSide = ["  8:30 ", "  9:20 ", " 10:10 ", " 11:00 ", " 11:50 ", " 12:20 ", " 13:10 ", " 14:00 "]

        datos = [["PMDP", "PSP", "DI", "AD", "HAB"],
                 ["PMDM", "PSP", "DI", "AD", "HAB"],
                 ["PMDM", "AD", "DI", "SXE", "PMDM"],
                 ["DIX", "AD", "PMDM", "SXE", "PMDM"],
                 ["RECREO", "RECREO", "RECREO", "RECREO", "RECREO"],
                 ["IPE", "AD", "PMDP", "IPE", "AD"],
                 ["DI", "DI", "SXE", "PSP", "AD"],
                 ["DI", "DI", "SXE", "PSP", "ACOP"]]

        self.modelo = ModeloHorario(datos, datosTop, datosSide)

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
