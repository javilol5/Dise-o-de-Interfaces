import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana")
        self.Qlabel = QLabel("BOBO")
        self.boton = QPushButton("Cerrar")

        layout = QVBoxLayout()
        layout.addWidget(self.Qlabel)
        layout.addWidget(self.boton)
        self.setLayout(layout)

        self.boton.clicked.connect(self.abrir_ventanas)

        self.ventanas = []

    def abrir_ventanas(self):
        for i in range(2):
            ventana = Ventana()
            ventana.showFullScreen()
            self.ventanas.append(ventana)


app = QApplication(sys.argv)

ventana = Ventana()
ventana.showFullScreen()

sys.exit(app.exec())