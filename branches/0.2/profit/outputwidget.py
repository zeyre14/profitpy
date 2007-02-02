#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2007 Troy Melhase
# Distributed under the terms of the GNU General Public License v2
# Author: Troy Melhase <troy@gci.net>

from PyQt4.QtGui import QWidget
from profit.ui_outputwidget import Ui_OutputWidget

class OutputWidget(QWidget, Ui_OutputWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        editor = self.editor()
        editor.clear()
        editor.setText('')

    def editor(self):
        return self.outputEdit
    
    def write(self, text):
        self.editor().insertPlainText(text)

    def currentCharFormat(self):
        return self.editor().currentCharFormat()

    def setCurrentCharFormat(self, format):
        return self.editor().setCurrentCharFormat(format)

    def flush(self):
        pass
    
