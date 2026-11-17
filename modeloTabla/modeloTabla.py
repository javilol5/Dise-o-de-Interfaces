from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla

    def rowCount(self, indice):
        return len(self.tabla)-1

    def columnCount(self, indice):
        return len(self.tabla[0])

    def data(self, indice, rol):
        if indice.isValid():
            if rol == Qt.ItemDataRole.DisplayRole:
                dato = self.tabla[indice.row() + 1][indice.column()]

                if indice.column() == 3:
                    if dato == True:
                        return "✓"
                    else:
                        return "✗"

                return dato

    def headerData(self, seccion, orientacion, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.tabla[0][seccion]

    def flags(self, indice):
        return Qt.ItemFlag.ItemIsEnabled