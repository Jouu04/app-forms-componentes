from PyQt5 import QtWidgets, uic
from service import MayorMenorService

class MayorMenor:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])

        self.ventana = uic.loadUi("view/frmmayormenor.ui")
        self.ventana.lbcalcular.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()
    
    def onclickbtncalcular(self):
        resultado = 0
        try:
            n1 = int(self.ventana.txtnum1.txt())
            n2 = int(self.ventana.txtnum2.txt())
            n3 = int(self.ventana.txtnum3.txt())
            n4 = int(self.ventana.txtnum4.txt())
            if self.ventana.rbmayor.isChecked():
                resultado = MayorMenorService.mayor(n1,n2,n3,n4)
            elif self.ventana.rbmayor.isChecked():
                resultado = MayorMenorService.menor(n1,n2,n3,n4)
            else:
                resultado = 0
        except:
            resultado = 0

        finally:
            self.ventana.asd.setText(str(resultado))