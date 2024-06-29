from PyQt5 import QtWidgets, uic
from service import CalculadoraService

class CalculadoraController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])

        self.ventana = uic.loadUi("view/frmcalculadora.ui")
        self.ventana.lbcalcular.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()

    def onclickbtncalcular(self):
        resultado = 0
        operacion = ""
        try:
            num1 = int(self.ventana.txtnumero1.txt())
            num2 = int(self.ventana.txtnumero2.txt())
            if self.ventana.rbsuma.isChecked():
                resultado = CalculadoraService.suma(num1, num2)
                operacion = "Suma"
            
            elif self.ventana.rbresta.isChecked():
                resultado = CalculadoraService.resta(num1, num2)
                operacion = "Resta"
            elif self.ventana.rbmultiplica.isChecked():
                resultado = CalculadoraService.multiplicar(num1, num2)
                operacion = "Multiplica"
            elif self.ventana.rbdivide.isChecked():
                resultado = CalculadoraService.dividir(num1, num2)
                operacion = "Dividir"
            else:
                resultado = 0
                operacion = "Elegir operacion"
        except:
            operacion = "Ingrese valores numericos"
        finally:
            self.ventana.lbresultado.setText(operacion +" = "+ str(resultado))    