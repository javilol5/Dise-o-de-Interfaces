import math
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QGridLayout)
from PyQt6.QtGui import QColor, QPalette

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Oca")

        self.setMinimumSize(100, 100)
        self.setMaximumSize(1000, 1000)



        vertical =QVBoxLayout()

        horizontal = QHBoxLayout()

        vertical.addLayout(horizontal)

        maia = QGridLayout()







        boton1 = QPushButton("1")
        boton2 = QPushButton("2")
        boton3 = QPushButton("3")
        boton4 = QPushButton("4")
        boton5 = QPushButton("5")
        boton6 = QPushButton("6")
        boton7 = QPushButton("7")
        boton8 = QPushButton("8")
        boton9 = QPushButton("9")
        boton10 = QPushButton("10")
        boton11 = QPushButton("11")
        boton12 = QPushButton("12")
        boton13 = QPushButton("13")
        boton14 = QPushButton("14")
        boton15 = QPushButton("15")
        boton16 = QPushButton("16")
        boton17 = QPushButton("17")
        boton18 = QPushButton("18")
        boton19 = QPushButton("19")
        boton20 = QPushButton("20")
        boton21 = QPushButton("21")
        boton22 = QPushButton("22")
        boton23 = QPushButton("23")
        boton24 = QPushButton("24")
        boton25 = QPushButton("25")
        boton26 = QPushButton("26")
        boton27 = QPushButton("27")
        boton28 = QPushButton("28")
        boton29 = QPushButton("29")
        boton30 = QPushButton("30")
        boton31 = QPushButton("31")
        boton32 = QPushButton("32")
        boton33 = QPushButton("33")
        boton34 = QPushButton("34")
        boton35 = QPushButton("35")
        boton36 = QPushButton("36")
        boton37 = QPushButton("37")
        boton38 = QPushButton("38")
        boton39 = QPushButton("39")
        boton40 = QPushButton("40")
        boton41 = QPushButton("41")
        boton42 = QPushButton("42")
        boton43 = QPushButton("43")
        boton44 = QPushButton("44")
        boton45 = QPushButton("45")
        boton46 = QPushButton("46")
        boton47 = QPushButton("47")
        boton48 = QPushButton("48")
        boton49 = QPushButton("49")
        boton50 = QPushButton("50")
        boton51 = QPushButton("51")
        boton52 = QPushButton("52")
        boton53 = QPushButton("53")
        boton54 = QPushButton("54")
        boton55 = QPushButton("55")
        boton56 = QPushButton("56")
        boton57 = QPushButton("57")
        boton58 = QPushButton("58")
        boton59 = QPushButton("59")
        boton60 = QPushButton("60")
        boton61 = QPushButton("61")
        boton62 = QPushButton("62")
        boton63 = QPushButton("63")

        maia.addWidget(boton29,0,0)
        maia.addWidget(boton28, 0,1)
        maia.addWidget(boton27, 0,2)
        maia.addWidget(boton26, 0,3)
        maia.addWidget(boton25, 0,4)
        maia.addWidget(boton24, 0,5)
        maia.addWidget(boton23, 0,6)
        maia.addWidget(boton22, 0,7)
        maia.addWidget(boton21, 0,8)
        maia.addWidget(boton20, 0,9)
        maia.addWidget(boton19, 0,10)
        maia.addWidget(boton18, 0,11)





        vertical.addLayout(maia)

        contenedor = QWidget()
        contenedor.setLayout(maia)



        self.setCentralWidget(contenedor)

        self.show()







if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()