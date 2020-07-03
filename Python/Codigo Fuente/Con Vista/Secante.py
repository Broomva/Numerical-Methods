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
        MainWindow.resize(397, 297)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.CalcSec = QtGui.QPushButton(self.groupBox)
        self.CalcSec.setObjectName(_fromUtf8("CalcSec"))
        self.gridLayout_3.addWidget(self.CalcSec, 6, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 6, 0, 1, 1)
        self.FunSec = QtGui.QLineEdit(self.groupBox)
        self.FunSec.setObjectName(_fromUtf8("FunSec"))
        self.gridLayout_3.addWidget(self.FunSec, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.X0Sec = QtGui.QLineEdit(self.groupBox)
        self.X0Sec.setObjectName(_fromUtf8("X0Sec"))
        self.gridLayout_3.addWidget(self.X0Sec, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.X1Sec = QtGui.QLineEdit(self.groupBox)
        self.X1Sec.setObjectName(_fromUtf8("X1Sec"))
        self.gridLayout_3.addWidget(self.X1Sec, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.TolSec = QtGui.QLineEdit(self.groupBox)
        self.TolSec.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TolSec.setReadOnly(True)
        self.TolSec.setObjectName(_fromUtf8("TolSec"))
        self.gridLayout_3.addWidget(self.TolSec, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)
        self.ResSec = QtGui.QLineEdit(self.groupBox)
        self.ResSec.setText(_fromUtf8(""))
        self.ResSec.setObjectName(_fromUtf8("ResSec"))
        self.gridLayout_3.addWidget(self.ResSec, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.label.setText(_translate("MainWindow", "Funcion", None))
        self.CalcSec.setText(_translate("MainWindow", "Calcular", None))
        self.label_2.setText(_translate("MainWindow", "   X0", None))
        self.label_3.setText(_translate("MainWindow", "   X1", None))
        self.label_4.setText(_translate("MainWindow", "Tolerancia", None))
        self.TolSec.setText(_translate("MainWindow", "0.0001", None))
        self.label_5.setText(_translate("MainWindow", "La Raiz es:", None))

    @QtCore.pyqtSignature("on_CalcSec_clicked()")
    def CalcSec_clicked(self):
        x, y, z = symbols("x,y,z,")

        func = self.FunSec.text()
        a = float(self.X0Sec.text())
        b = float(self.X1Sec.text())
        tol = 0.00000001

        func = sympify(func)
        evala = func.subs(x, a)
        evalb = func.subs(x, b)

        while abs(evalb) > tol:
            xm = b - ((b - a) / (evalb - evala) * evalb)
            pb = xm
            evalb = func.subs(x, pb)

        xm = str(xm)[:6]
        self.ResSec.setText(str(xm))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.setWindowTitle("Secante")
    ex.show()
    sys.exit(app.exec())