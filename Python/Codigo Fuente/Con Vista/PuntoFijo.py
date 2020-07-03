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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(441, 321)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.CalcPF = QtGui.QPushButton(self.groupBox)
        self.CalcPF.setObjectName(_fromUtf8("CalcPF"))
        self.gridLayout_2.addWidget(self.CalcPF, 5, 5, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 5, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 5, 1, 1)
        self.PA = QtGui.QLineEdit(self.groupBox)
        self.PA.setObjectName(_fromUtf8("PA"))
        self.gridLayout_2.addWidget(self.PA, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(183, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 5, 1, 1)
        self.ResPF = QtGui.QLineEdit(self.groupBox)
        self.ResPF.setObjectName(_fromUtf8("ResPF"))
        self.gridLayout_2.addWidget(self.ResPF, 4, 2, 1, 1)
        self.FunPF = QtGui.QLineEdit(self.groupBox)
        self.FunPF.setObjectName(_fromUtf8("FunPF"))
        self.gridLayout_2.addWidget(self.FunPF, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Punto Fijo", None))
        self.CalcPF.setText(_translate("MainWindow", "Calcular", None))
        self.label_3.setText(_translate("MainWindow", "Resultado", None))
        self.label_2.setText(_translate("MainWindow", "Punto A", None))
        self.label.setText(_translate("MainWindow", "Funcion", None))

    @QtCore.pyqtSignature("on_CalcPF_clicked()")
    def CalcPFclicked(self):
        x, y, z = symbols("x,y,z")

        ecuacion = self.FunPF.text()
        pa = float(self.PA.text())
        tol = 0.00001

        ec = sympify(ecuacion)
        eval_a=(ec.subs(x,pa))
        fdiff = diff(ec)
        ev=1
        resu=0
        ite=0
        if (fdiff.subs(x,0.4))<1:

            while ev>0.1:
                ite+=1
                eval_a=(ec.subs(x,pa))
                eu=abs(pa-eval_a)

                if eu<tol:
                    ev=0
                    self.ResPF.setText(str(resu))

                elif ite==100:
                    QtGui.QMessageBox.warning(self, "No PF", "La Funcion no tiene\n\n\nPunto Fijo", "Cerrar")
                    ev=0

                else:
                    pa=eval_a

                resu=pa

        else:
            QtGui.QMessageBox.warning(self, "No Converge", "La Funcion no converge al\n\n\nPunto Fijo", "Cerrar")
            sys.exit(app.exec())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec())
