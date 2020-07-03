# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Suma.ui'
#
# Created: Sun May  3 16:47:24 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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
        MainWindow.resize(417, 303)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Dato1Sum = QtGui.QLineEdit(self.centralwidget)
        self.Dato1Sum.setGeometry(QtCore.QRect(40, 90, 127, 21))
        self.Dato1Sum.setObjectName(_fromUtf8("Dato1Sum"))
        self.Dato2Sum = QtGui.QLineEdit(self.centralwidget)
        self.Dato2Sum.setGeometry(QtCore.QRect(240, 90, 127, 21))
        self.Dato2Sum.setObjectName(_fromUtf8("Dato2Sum"))
        self.ResSum = QtGui.QLineEdit(self.centralwidget)
        self.ResSum.setGeometry(QtCore.QRect(80, 170, 127, 21))
        self.ResSum.setObjectName(_fromUtf8("ResSum"))
        self.CalcSuma = QtGui.QPushButton(self.centralwidget)
        self.CalcSuma.setGeometry(QtCore.QRect(300, 230, 91, 21))
        self.CalcSuma.setObjectName(_fromUtf8("CalcSuma"))
        self.CalcResta = QtGui.QPushButton(self.centralwidget)
        self.CalcResta.setGeometry(QtCore.QRect(210, 230, 91, 21))
        self.CalcResta.setObjectName(_fromUtf8("CalcResta"))
        self.CalcMult = QtGui.QPushButton(self.centralwidget)
        self.CalcMult.setGeometry(QtCore.QRect(120, 230, 91, 21))
        self.CalcMult.setObjectName(_fromUtf8("CalcMult"))
        self.CalcDiv = QtGui.QPushButton(self.centralwidget)
        self.CalcDiv.setGeometry(QtCore.QRect(30, 230, 91, 21))
        self.CalcDiv.setObjectName(_fromUtf8("CalcDiv"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 39, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 70, 39, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 150, 59, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.CalcSuma.setText(_translate("MainWindow", "Sumar", None))
        self.CalcResta.setText(_translate("MainWindow","Restar",None))
        self.CalcMult.setText(_translate("MainWindow","Multiplicar",None))
        self.CalcDiv.setText(_translate("MainWindow","Dividir",None))
        self.label.setText(_translate("MainWindow", "Dato 1", None))
        self.label_2.setText(_translate("MainWindow", "Dato 2", None))
        self.label_3.setText(_translate("MainWindow", "Resultado", None))


    @QtCore.pyqtSignature("on_CalcSuma_clicked()")
    def Suma(self):
        dato1 = float(self.Dato1Sum.text())
        dato2 = float(self.Dato2Sum.text())
        ResSuma = dato1 + dato2
        self.ResSum.setText(str(ResSuma))

    @QtCore.pyqtSignature("on_CalcResta_clicked()")
    def Resta(self):
        dato1 = float(self.Dato1Sum.text())
        dato2 = float(self.Dato2Sum.text())
        ResSuma = dato1 - dato2
        self.ResSum.setText(str(ResSuma))

    @QtCore.pyqtSignature("on_CalcMult_clicked()")
    def Mult(self):
        dato1 = float(self.Dato1Sum.text())
        dato2 = float(self.Dato2Sum.text())
        ResSuma = dato1 * dato2
        self.ResSum.setText(str(ResSuma))

    @QtCore.pyqtSignature("on_CalcDiv_clicked()")
    def Div(self):
        dato1 = float(self.Dato1Sum.text())
        dato2 = float(self.Dato2Sum.text())
        ResSuma = dato1/dato2
        self.ResSum.setText(str(ResSuma))



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec())
