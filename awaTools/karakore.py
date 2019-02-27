# -*- coding:utf-8 -*-
from maya import cmds,mel
import pymel.core as pm
import imp
from ..lib import qt

try:
    imp.find_module('PySide2')
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *

except ImportError:
    from PySide.QtGui import *
    from PySide.QtCore import *

def karakore():
    pass

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('karakore')
        self.resize(300,100)

        widget = mainButton()
        self.setCentralWidget(widget)

class mainButton(QWidget):
    def __init__(self, *args, **kwargs):
        super(mainButton, self).__init__(*args, **kwargs)

        self.txt = ''

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        button = QPushButton('SelectMat')
        self.layout.addWidget(button)

        self.lineEdit = QLineEdit('lineEdit')
        self.layout.addWidget(self.lineEdit)

        self.buttonA = QPushButton('BaseColor')
        self.buttonA.clicked.connect(self.getTxt)
        self.layout.addWidget(self.buttonA)

        button = QPushButton('Specular')
        self.layout.addWidget(button)

    def getTxt(self):
        self.txt = self.lineEdit.text()
        print self.txt


def main():
    app = MainWindow(qt.getMayaWindow())
    app.show()
