__author__ = 'Didi'

from PyQt4 import QtCore, QtGui
from sympy import *
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
        MainWindow.resize(483, 305)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.FuncionNew = QtGui.QLineEdit(self.centralwidget)
        self.FuncionNew.setGeometry(QtCore.QRect(110, 40, 291, 21))
        self.FuncionNew.setObjectName(_fromUtf8("FuncionNew"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.XnNew = QtGui.QLineEdit(self.centralwidget)
        self.XnNew.setGeometry(QtCore.QRect(70, 110, 111, 21))
        self.XnNew.setObjectName(_fromUtf8("XnNew"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 56, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ResNew = QtGui.QLineEdit(self.centralwidget)
        self.ResNew.setGeometry(QtCore.QRect(140, 180, 171, 21))
        self.ResNew.setObjectName(_fromUtf8("ResNew"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 160, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 40, 41, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.CalcNew = QtGui.QPushButton(self.centralwidget)
        self.CalcNew.setGeometry(QtCore.QRect(339, 250, 101, 21))
        self.CalcNew.setObjectName(_fromUtf8("CalcNew"))
        self.Print = QtGui.QPushButton(self.centralwidget)
        self.Print.setGeometry(QtCore.QRect(230, 240, 101, 41))
        self.Print.setObjectName(_fromUtf8("Print"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Función", None))
        self.label_2.setText(_translate("MainWindow", "Valor Xn", None))
        self.label_3.setText(_translate("MainWindow", "Resultado", None))
        self.label_4.setText(_translate("MainWindow", "F(x) =", None))
        self.CalcNew.setText(_translate("MainWindow", "Calcular", None))
        self.Print.setText(_translate("MainWindow", "Print", None))






    @QtCore.pyqtSignature("on_CalcNew_clicked()")
    def CalcNew_clicked(self):
        x, y, z = symbols("x y z")

        func = self.FuncionNew.text()
        func = sympify(func)
        p1 = plot(func)

        xn = self.XnNew.text()
        func = func.subs(x, xn)
        funcdff = diff(func,x)
        funcdff = funcdff.subs(x, xn)
        if funcdff == 0:
            funcdff += 0.01

        res = float(xn) - (float(func)/float(funcdff))
        self.ResNew.setText(str(res))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec())