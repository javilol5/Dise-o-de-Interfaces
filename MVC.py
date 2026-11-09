from PyQt6.QtCore import *
from PyQt6.QtGui import *

imagen = QImage("java.png").scaled(16, 16)

class ModeloTarefas (QAbstractListModel):
    def __init__(self, tarefas=None):
        super().__init__()
        self.tarefas = tarefas or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            _, texto = self.tarefas [indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado, _ = self.tarefas [indice.row()]
            if estado:
                return imagen
        if rol == Qt.ItemDataRole.BackgroundRole:
            estado, _ = self.tarefas [indice.row()]
            if not estado:
                return QColor("LightPink")

    def rowCount(self, indice):
        return len(self.tarefas)