__author__ = 'Didi'

from sympy import *
from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(423, 301)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 471, 321))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.FuncBis = QtGui.QLineEdit(self.groupBox)
        self.FuncBis.setGeometry(QtCore.QRect(110, 40, 241, 21))
        self.FuncBis.setObjectName(_fromUtf8("FuncBis"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Vala = QtGui.QLineEdit(self.groupBox)
        self.Vala.setGeometry(QtCore.QRect(30, 110, 111, 21))
        self.Vala.setObjectName(_fromUtf8("Vala"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(240, 90, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Valb = QtGui.QLineEdit(self.groupBox)
        self.Valb.setGeometry(QtCore.QRect(240, 110, 111, 21))
        self.Valb.setObjectName(_fromUtf8("Valb"))
        self.ResBis = QtGui.QLineEdit(self.groupBox)
        self.ResBis.setGeometry(QtCore.QRect(130, 190, 111, 21))
        self.ResBis.setObjectName(_fromUtf8("ResBis"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(130, 170, 91, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.CalcBis = QtGui.QPushButton(self.groupBox)
        self.CalcBis.setGeometry(QtCore.QRect(270, 250, 110, 32))
        self.CalcBis.setObjectName(_fromUtf8("CalcBis"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Biseccion", None))
        self.label.setText(_translate("Form", "Función:", None))
        self.label_2.setText(_translate("Form", "Valor Punto A:", None))
        self.label_3.setText(_translate("Form", "Valor Punto B:", None))
        self.label_4.setText(_translate("Form", "Resultado:", None))
        self.CalcBis.setText(_translate("Form", "Calcular", None))

    @QtCore.pyqtSignature("on_CalcPF_clicked()")
    def CalcPFlicked(self):
        x, y, z = symbols("x y z")

        ecuacion = self.FuncBis.text()
        pa = float(self.Vala.text())
        pb = float(self.Valb.text())

        ec = sympify(ecuacion)
        evala = ec.subs(x,pa)
        evalb = ec.subs(x,pb)

        if evala*evalb<0:
            pmedioab = 0.1

            while pmedioab<0.00000001:

                pmedio = (pa+pb)/2
                evala = ec.subs(x,pa)
                evalb = ec.subs(x,pb)
                evalpmedio = ec.subs(x,pmedio)

                if evala*evalpmedio<0:
                    pb = pmedio

                elif evala*evalpmedio<0:
                    pa = pmedio

                pmedioab = abs(evalpmedio)
                resultado = pmedio

            self.ResBis.setText(str(resultado))

        else:
            QtGui.QMessageBox.warning(self,"","No existe Raiz en ese intervalo","Salir")








if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec())