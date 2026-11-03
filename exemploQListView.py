import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QListView)
from PyQt6.QtGui import QColor, QPalette

from MVC import ModeloTarefas


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("exemplo QListView")

        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 400)

        listaTarefas = [(True, "Ir o centro DC"), (False, "Ir o ximnasio"), (False, "Ir a compra")]

        self.modelo = ModeloTarefas(listaTarefas)

        caixaV = QVBoxLayout()

        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)
        self.lstTarefas.setSelectionMode(QListView.SelectionMode.MultiSelection)
        caixaV.addWidget(self.lstTarefas)

        caixaBotons = QHBoxLayout()
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.on_btnBorrar_clicked)
        btnFeito = QPushButton("Feito")
        btnFeito.clicked.connect(self.on_btnFeito_clicked)

        caixaBotons.addWidget(btnBorrar)
        caixaBotons.addWidget(btnFeito)

        caixaV.addLayout(caixaBotons)

        contenedor = QWidget()
        contenedor.setLayout(caixaV)
        self.setCentralWidget(contenedor)

        self.show()

        def on_btnBorrar_clicked(self):
            pass
        def on_btnFeito_clicked(self):
            pass

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()