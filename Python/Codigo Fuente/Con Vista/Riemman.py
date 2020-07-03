__author__ = 'Didi'

from PyQt4 import QtCore, QtGui
import sys
from sympy.plotting import *
from sympy import *

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
        MainWindow.resize(441, 344)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 311))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 50, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.FuncRie = QtGui.QLineEdit(self.groupBox)
        self.FuncRie.setGeometry(QtCore.QRect(140, 50, 201, 21))
        self.FuncRie.setObjectName(_fromUtf8("FuncRie"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(240, 110, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.LimSup = QtGui.QLineEdit(self.groupBox)
        self.LimSup.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.LimSup.setObjectName(_fromUtf8("LimSup"))
        self.LimInf = QtGui.QLineEdit(self.groupBox)
        self.LimInf.setGeometry(QtCore.QRect(230, 130, 121, 21))
        self.LimInf.setObjectName(_fromUtf8("LimInf"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 190, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.ResRie = QtGui.QLineEdit(self.groupBox)
        self.ResRie.setGeometry(QtCore.QRect(70, 210, 121, 21))
        self.ResRie.setObjectName(_fromUtf8("ResRie"))
        self.CalcRie = QtGui.QPushButton(self.groupBox)
        self.CalcRie.setGeometry(QtCore.QRect(300, 270, 110, 32))
        self.CalcRie.setObjectName(_fromUtf8("CalcRie"))
        self.PlotRie = QtGui.QPushButton(self.groupBox)
        self.PlotRie.setGeometry(QtCore.QRect(300, 230, 110, 32))
        self.PlotRie.setObjectName(_fromUtf8("PlotRie"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Sumas de Riemman", None))
        self.label.setText(_translate("MainWindow", "Funcion", None))
        self.label_2.setText(_translate("MainWindow", "Limite Superior", None))
        self.label_3.setText(_translate("MainWindow", "Limite Inferior", None))
        self.label_4.setText(_translate("MainWindow", "Area Bajo la Curva", None))
        self.CalcRie.setText(_translate("MainWindow", "Calcular", None))
        self.PlotRie.setText(_translate("MainWindow", "Graph", None))

    @QtCore.pyqtSignature("on_CalcRie_clicked()")
    def CalcRie_clicked(self):
        x, y, z, = symbols("x,y,z")

        func = self.FuncRie.text()
        func = sympify(func)
        func = integrate(func,x)
        lima = self.LimSup.text()
        limb = self.LimInf.text()

        area = float(func.subs(x, lima))-float(func.subs(x,limb))

        self.ResRie.setText(str(area))


    @QtCore.pyqtSignature("on_PlotRie_clicked()")
    def PlotRie_clicked(self):
        x, y, z, = symbols("x,y,z")
        func = self.FuncRie.text()
        func = sympify(func)
        func = integrate(func,x)
        plot(func)




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec())