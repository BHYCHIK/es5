# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow, QListWidgetItem, QMessageBox, QHeaderView
from ui_mainwindow import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QPalette, QColor
import time
from hopfield import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.app = app
        self.btnLoad.clicked.connect(self.onBtnLoad)
        self.btnTeach.clicked.connect(self.onBtnTeach)
        self.btnClear.clicked.connect(self.onBtnClear)
        self.picSize = 25
        self.hopfield = HopfieldNetwork(1954 * 8)
        self.saved_images = dict()
        self.statusbar.showMessage('Создан')
    def showMessageBox(self, message):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle('Сообщение от нейросети')
        msgBox.setText(message)
        msgBox.exec()
    def onBtnLoad(self):
        text, ok = QtGui.QFileDialog.getOpenFileNameAndFilter(self, 'Открыть файл bmp', './images', '*.bmp')
        if ok:
            self.lblClearedImage.setPixmap(QtGui.QPixmap())
            self.openedImagePath = text
            pixmap = QtGui.QPixmap(self.openedImagePath)
            pixmap = pixmap.scaledToHeight(self.picSize)
            self.lblLoadedImage.setPixmap(pixmap)
            self.lblLoadedImage.setGeometry(50, 50, self.picSize, self.picSize)
    def onBtnTeach(self):
        self.statusbar.showMessage('Идет обучение')
        self.lblClearedImage.setPixmap(QtGui.QPixmap())
        QtGui.QApplication.processEvents()
        with open(self.openedImagePath, 'rb') as f:
            data = f.read()
        path = self.openedImagePath
        key = self._make_key(data)
        self.saved_images[str(key)] = path
        self.hopfield.learn_vector(key)
        self.statusbar.showMessage('')
        self.showMessageBox('Обучение успешно завершено')
    def onBtnClear(self):
        self.lblClearedImage.setPixmap(QtGui.QPixmap())
        self.statusbar.showMessage('Идет фильтрация')
        QtGui.QApplication.processEvents()
        return
        with open(self.openedImagePath, 'rb') as f:
            data = f.read()
        key = self._make_key(data)
        key = self.hopfield.filter_vector(key)
        if str(key) not in self.saved_images:
            self.showMessageBox('Изображение не распознано')
            self.statusbar.showMessage('')
            return
        fpath = self.saved_images[str(key)]
        pixmap = QtGui.QPixmap(fpath)
        pixmap = pixmap.scaledToHeight(self.picSize)
        self.lblClearedImage.setPixmap(pixmap)
        self.lblClearedImage.setGeometry(110, 50, self.picSize, self.picSize)
        self.statusbar.showMessage('')
        self.showMessageBox('Очистка изображения успешно завершена')
    def _make_key(self, data):
        res = []
        for b in data:
            res = res + [i for i in self._get_bits(b)]
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
