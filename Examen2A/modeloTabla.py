from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla, datosTop):
        super().__init__()
        self.tabla = tabla
        self.datosTop = datosTop

    def rowCount(self, indice):
        return len(self.tabla)

    def columnCount(self, indice):
        return len(self.tabla[0])

    def data(self, indice, rol):
        if indice.isValid():

            dato = self.tabla[indice.row()][indice.column()]

            if rol == Qt.ItemDataRole.DisplayRole:

                return dato

            # COLORES
            if rol == Qt.ItemDataRole.BackgroundRole:

                fila = self.tabla[indice.row()][0]

                if int(fila) % 2 == 0:
                    return QColor("lightblue")




    def headerData(self, seccion, orientacion, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.datosTop[seccion]
        if rol == Qt.ItemDataRole.BackgroundRole:
            return QColor("lightgray")

    def flags(self, indice):

        condicions = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        if indice.row() != -1 and indice.column() != 1:
            condicions = condicions | Qt.ItemFlag.ItemIsEditable
        if indice.row() != -1 and indice.column() == 3:
            condicions = condicions | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEditable
        return condicions