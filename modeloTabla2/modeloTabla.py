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

            dato = self.tabla[indice.row() + 1 ][indice.column()]

            if rol == Qt.ItemDataRole.DisplayRole:
                if indice.row() == -1 or indice.column() != 3:
                    return dato

            if rol == Qt.ItemDataRole.CheckStateRole:
                if indice.row() != -1 and indice.column() == 3:
                    if dato == True:
                        return Qt.CheckState.Checked
                    else:
                        return Qt.CheckState.Unchecked
            # COLORES
            if rol == Qt.ItemDataRole.BackgroundRole:
                genero = self.tabla[indice.row() + 1][2]
                fallecido = self.tabla[indice.row() + 1][3]

                if fallecido:
                    return QColor("lightgray")

                if genero == "Home" and fallecido == False:
                    return QColor("pink")
                if genero == "Muller" and fallecido  == False:
                    return QColor("lightblue")
                if genero == "Outro" and fallecido == False:
                    return QColor("darkgreen")






    def setData(self, indice, valor, rol):

        if rol == Qt.ItemDataRole.EditRole:

            if indice.column() == 0:
                if valor != "":
                    fila = list(self.tabla[indice.row() + 1])
                    fila[indice.column()] = valor.capitalize()
                    self.tabla[indice.row() + 1] = tuple(fila)

                    self.dataChanged.emit(indice, indice)
                    return True

            if indice.column() == 2:
                if valor.lower() in ("home", "muller", "outro"):
                    fila = list(self.tabla[indice.row() + 1])
                    fila[indice.column()] = valor.capitalize()
                    self.tabla[indice.row() + 1] = tuple(fila)

                    self.dataChanged.emit(indice, indice)
                    return True

        if rol == Qt.ItemDataRole.CheckStateRole:
            if indice.column() == 3:
                fila = list(self.tabla[indice.row() + 1])
                fila[indice.column()] = valor == Qt.CheckState.Checked.value
                self.tabla[indice.row() + 1] = tuple(fila)

                self.dataChanged.emit(indice, indice)
                return True

        return False


    def headerData(self, seccion, orientacion, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.tabla[0][seccion]
        if rol == Qt.ItemDataRole.BackgroundRole:
            return QColor("lightgray")

    def flags(self, indice):

        condicions = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        if indice.row() != -1 and indice.column() != 1:
            condicions = condicions | Qt.ItemFlag.ItemIsEditable
        if indice.row() != -1 and indice.column() == 3:
            condicions = condicions | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEditable
        return condicions