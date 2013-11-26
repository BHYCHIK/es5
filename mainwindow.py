# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow, QListWidgetItem, QMessageBox, QHeaderView
from ui_mainwindow import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QPalette, QColor
from hopfield import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.app = app
        self.btnLoad.clicked.connect(self.onBtnLoad)
        self.hopfield = HopfieldNetwork(320 * 200 * 3)
        self.saved_images = dict()
    def onBtnLoad(self):
        text, ok = QtGui.QFileDialog.getOpenFileNameAndFilter(self, 'Открыть файл bmp', './images', '*.bmp')
        if ok:
            self.openedImagePath = text
            pixmap = QtGui.QPixmap(self.openedImagePath)
            pixmap = pixmap.scaledToHeight(200)
            self.lblLoadedImage.setPixmap(pixmap)
            self.lblLoadedImage.setGeometry(50, 50, 320, 320)
    def onBtnTeach(self):
        with open(self.openedImagePath) as f:
            data = f.read()
        path = self.openedImagePath
        key = self._make_key(data)
        self.saved_images[key] = path
        self.hopfield.learn_vector(key)
        print(key)
    def _make_key(self, data):
        res = []
        for b in data:
            res.append([i for i in self._get_bits(b)])
        return res
    def _get_bits(self, b):
        yield 1 if (b & 1) > 0 else -1
        yield 1 if (b & 2) > 0 else -1
        yield 1 if (b & 4) > 0 else -1
        yield 1 if (b & 8) > 0 else -1
        yield 1 if (b & 16) > 0 else -1
        yield 1 if (b & 32) > 0 else -1
        yield 1 if (b & 64) > 0 else -1
        yield 1 if (b & 128) > 0 else -1
        return
