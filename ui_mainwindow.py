# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Nov 27 01:55:40 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(351, 256)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblLoadedImage = QtGui.QLabel(self.centralwidget)
        self.lblLoadedImage.setGeometry(QtCore.QRect(20, 30, 58, 17))
        self.lblLoadedImage.setText(_fromUtf8(""))
        self.lblLoadedImage.setObjectName(_fromUtf8("lblLoadedImage"))
        self.lblClearedImage = QtGui.QLabel(self.centralwidget)
        self.lblClearedImage.setGeometry(QtCore.QRect(210, 30, 58, 17))
        self.lblClearedImage.setText(_fromUtf8(""))
        self.lblClearedImage.setObjectName(_fromUtf8("lblClearedImage"))
        self.btnLoad = QtGui.QPushButton(self.centralwidget)
        self.btnLoad.setGeometry(QtCore.QRect(10, 180, 87, 27))
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.btnTeach = QtGui.QPushButton(self.centralwidget)
        self.btnTeach.setGeometry(QtCore.QRect(110, 180, 87, 27))
        self.btnTeach.setObjectName(_fromUtf8("btnTeach"))
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(220, 180, 111, 27))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.lblStatus = QtGui.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(140, 150, 58, 17))
        self.lblStatus.setText(_fromUtf8(""))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Нейросеть Хопфилда", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoad.setText(QtGui.QApplication.translate("MainWindow", "Загрузить", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTeach.setText(QtGui.QApplication.translate("MainWindow", "Обучить", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("MainWindow", "Отфильтровать", None, QtGui.QApplication.UnicodeUTF8))

