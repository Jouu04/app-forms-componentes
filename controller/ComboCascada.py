from PyQt5 import QtWidgets, uic

class ComboCascada:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])

        self.ventana = uic.loadUi("view/frmcombocascada.ui")
        self.ventana.show()
        app.exec()