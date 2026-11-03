from PyQt6.QtCore import *

class ModeloTarefas (QAbstractListModel):
    def __init__(self, tarefas=None):
        super().__init__()
        self.tarefas = tarefas or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            _, texto = self.tarefas [indice.row()]
            return texto

    def rowCount(self, indice):
        return len(self.tarefas)