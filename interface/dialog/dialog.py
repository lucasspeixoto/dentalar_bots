# -*- coding: utf-8 -*-
# encoding: utf-8

from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from ui_dialog import Ui_Dialog

"""
Dialogbox class which make the dialogbox when called.
dialog box class : dialogbox containing two buttons,
one maeeage bar, one icon holder, one heading defining
"""


class DialogUi(QDialog):
    def __init__(self, parent=None):

        super(DialogUi, self).__init__(parent)
        self.d = Ui_Dialog()

        self.d.setupUi(self)

        """ 
        Removing windows top bar and making it frameless
        (as we have amde a custome frame in the window itself)
        """
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # * Making the window transparent so that to get a true flat ui

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        """ 
        Since there is no windows topbar, the close min, max button
        are absent and so there is a need for the alternative buttons in our
        ialog box, which is carried out by the below code
        """

        # * MINIMIZE BUTTON OF DIALOGBOX
        self.d.minimize_dialog_button.clicked.connect(lambda: self.showMinimized())

        # * CLOSE APPLICATION FUNCTION BUTTON
        self.d.close_dialog_button.clicked.connect(lambda: self.close())

        # * THIS FUNCTION WILL CHECKT WEATHER THE BUTTON ON THE DIALOGBOX IS CLICKED, AND IF SO DIRECTS TO THE FUNCTINON : diag_return()
        self.d.dialog_ok_button.clicked.connect(lambda: self.close())
        
        self.d.dialog_cancel_button.clicked.connect(lambda: self.close())

        """
        Since there i s no top bar to move the dialogbox over the
        screen we have to define the mouse event that is responsible for the
        movement. this is carried by this function moving the window when
        left mouse pressed and dragged over dialogbox topbar
        """
        self.dragPos = self.pos()

        def move_dialog_window(event):

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        """ 
        Widget to move
        Calling the function to cjange the position of
        the dialogbox during mouse drag
        """
        self.d.frame_top.mouseMoveEvent = move_dialog_window

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    """ 
    The dialog box is designed to be called from any where in the
    ui with able to change the statre of the text shown, button names e.t.c
    this is made by calling this function which takes: heading, message, icon,
    button name 1, button name 2 as argument.
    Embed the given propert to the dialogbox and finally displays it in the window.
    setting the dialogbox configration: text in button, label, heading
    """

    def dialog_construct(
        self,
        heading: str,
        message: str,
        icon: str,
        cancel_button_text: str,
        ok_button_text: str,
    ):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        self.d.dialog_cancel_button.setText(cancel_button_text)
        self.d.dialog_ok_button.setText(ok_button_text)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)
        
        return
