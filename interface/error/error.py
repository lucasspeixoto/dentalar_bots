# -*- coding: utf-8 -*-
# encoding: utf-8


from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from ui_error import Ui_Error

"""
Errorbox creates a samll window to display that something that the
user performed has went wrong.
This class also has the same property as the dialogbox class
with the exception that both have different ui interface
ans different application.
Error box giving the error occured in the process:
takes the heading, icon and button name
"""


class ErrorUi(QDialog):
    def __init__(self, parent=None):

        super(ErrorUi, self).__init__(parent)
        self.e = Ui_Error()
        self.e.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.e.bn_ok.clicked.connect(lambda: self.close())

        """
        Moving the window when left mouse pressed and
        dragged over errorbox topbar
        """
        self.dragPos = self.pos()

        def move_error_window(event):

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.e.frame_top.mouseMoveEvent = move_error_window

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    """
    Setting the errorbox configration: text in button, label, heading
    """

    def error_construct(self, heading: str, icon: str, button_ok_text: str):

        self.e.lab_heading.setText(heading)
        self.e.bn_ok.setText(button_ok_text)
        pixmap2 = QtGui.QPixmap(icon)
        self.e.lab_icon.setPixmap(pixmap2)

        return
