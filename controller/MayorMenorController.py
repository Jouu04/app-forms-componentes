from PyQt5 import QtWidgets, uic

class MayorMenor:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])

        self.ventana = uic.loadUi("view/frmmayormenor.ui")
        self.ventana.show()
        app.exec()