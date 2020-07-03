__author__ = 'Didi'

from PyQt4 import QtCore, QtGui
from sympy import *
import sys
import math


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
        MainWindow.resize(445, 344)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 7, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 5, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 2, 1, 1)
        self.FuncMul = QtGui.QLineEdit(self.groupBox)
        self.FuncMul.setObjectName(_fromUtf8("FuncMul"))
        self.gridLayout_2.addWidget(self.FuncMul, 0, 2, 1, 3)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 5, 2, 1, 1)
        self.x0 = QtGui.QLineEdit(self.groupBox)
        self.x0.setObjectName(_fromUtf8("x0"))
        self.gridLayout_2.addWidget(self.x0, 1, 2, 1, 1)
        self.x1 = QtGui.QLineEdit(self.groupBox)
        self.x1.setObjectName(_fromUtf8("x1"))
        self.gridLayout_2.addWidget(self.x1, 2, 2, 1, 1)
        self.x2 = QtGui.QLineEdit(self.groupBox)
        self.x2.setObjectName(_fromUtf8("x2"))
        self.gridLayout_2.addWidget(self.x2, 3, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.ResMul = QtGui.QLineEdit(self.groupBox)
        self.ResMul.setObjectName(_fromUtf8("ResMul"))
        self.gridLayout_2.addWidget(self.ResMul, 6, 2, 1, 2)
        self.CalcMul = QtGui.QPushButton(self.groupBox)
        self.CalcMul.setObjectName(_fromUtf8("CalcMul"))
        self.gridLayout_2.addWidget(self.CalcMul, 6, 5, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.FuncMul, self.x1)
        MainWindow.setTabOrder(self.x1, self.x0)
        MainWindow.setTabOrder(self.x0, self.x2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Muller", None))
        self.label_4.setText(_translate("MainWindow", "X2", None))
        self.label_5.setText(_translate("MainWindow", "Raiz", None))
        self.label.setText(_translate("MainWindow", "Funcion", None))
        self.label_3.setText(_translate("MainWindow", "X1", None))
        self.label_2.setText(_translate("MainWindow", "X0", None))
        self.CalcMul.setText(_translate("MainWindow", "Calcular", None))


    @QtCore.pyqtSignature("on_CalcMul_clicked()")
    def CalcMul_clicked(self):

        x, y, z = symbols("x,y,z")

        func = self.FuncMul.text()
        func = sympify(func)

        x0 = float(self.x0.text())
        x1 = float(self.x1.text())
        x2 = float(self.x2.text())

        h0 = x1 - x0
        h1 = x2 - x1

        feval0 = func.subs(x, x0)
        feval1 = func.subs(x, x1)
        feval2 = func.subs(x, x2)

        t0 = (feval1 - feval2)/h0
        t1 = (feval2 - feval1)/h1

        a = (t1-t0)/(h1+h0)
        b = (a*h1)+t0
        c = feval2

        rz = b**2-4*a*c
        if rz < 0:
            QtGui.QMessageBox.warning(self, "Raiz Compleja", "Raiz Compleja\n\n\nLa Funcion NO Converge", "Cerrar")
            sys.exit(app.exec())

            


        x3plus = x2 + ((-2*c)/(b+math.sqrt(b**2-4*a*c)))
        x3min = x2 + ((-2*c)/(b-math.sqrt(b**2-4*a*c)))

        ifxplus = b+math.sqrt(b**2-4*a*c)
        ifxmin = b-math.sqrt(b**2-4*a*c)

        muller = 0

        if ifxplus>ifxmin:
            muller = x3plus
            self.ResMul.setText(str(muller))
        else:
            muller = x3min
            self.ResMul.setText(str(muller))




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec())