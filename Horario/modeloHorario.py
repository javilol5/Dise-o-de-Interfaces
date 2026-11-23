from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ModeloHorario(QAbstractTableModel):
    def __init__(self, tabla, datosTop, datosSide):
        super().__init__()
        self.tabla = tabla
        self.datosTop = datosTop
        self.datosSide = datosSide

    def rowCount(self, indice):
        return len(self.tabla)

    def columnCount(self, indice):
        return len(self.tabla[0])

    def data(self, indice, rol):
        if indice.isValid():

            dato = self.tabla[indice.row()][indice.column()]

            if rol == Qt.ItemDataRole.DisplayRole:

                return dato

    def setData(self, indice, valor, rol):



        if rol == Qt.ItemDataRole.EditRole:
            if indice.row() != 4:
                self.tabla[indice.row()][indice.column()] = valor
                self.dataChanged.emit(indice, indice)
                return True

        return False

    def headerData(self, seccion, orientacion, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.datosTop[seccion]
            if orientacion == Qt.Orientation.Vertical:
                return self.datosSide[seccion]

    def flags(self, indice):

        condicions = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        if indice.row() != 4:
            condicions |= Qt.ItemFlag.ItemIsEditable

        return condicions