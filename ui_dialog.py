# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 235)
        Dialog.setMinimumSize(QSize(450, 235))
        Dialog.setMaximumSize(QSize(450, 235))
        Dialog.setStyleSheet(u"QDialog {\n"
"	background:rgb(51,51,51);\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_top = QFrame(self.frame_2)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 55))
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lab_heading = QLabel(self.frame_top)
        self.lab_heading.setObjectName(u"lab_heading")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.lab_heading.setFont(font)
        self.lab_heading.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_heading.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lab_heading)

        self.minimize_dialog_button = QPushButton(self.frame_top)
        self.minimize_dialog_button.setObjectName(u"minimize_dialog_button")
        self.minimize_dialog_button.setMinimumSize(QSize(55, 55))
        self.minimize_dialog_button.setMaximumSize(QSize(55, 55))
        self.minimize_dialog_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(51,51,51);\n"
"}")
        icon = QIcon()
        icon.addFile(u"assets/images/hide.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_dialog_button.setIcon(icon)
        self.minimize_dialog_button.setIconSize(QSize(22, 12))
        self.minimize_dialog_button.setAutoDefault(False)
        self.minimize_dialog_button.setFlat(True)

        self.horizontalLayout.addWidget(self.minimize_dialog_button)

        self.close_dialog_button = QPushButton(self.frame_top)
        self.close_dialog_button.setObjectName(u"close_dialog_button")
        self.close_dialog_button.setMinimumSize(QSize(55, 55))
        self.close_dialog_button.setMaximumSize(QSize(55, 55))
        self.close_dialog_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(51,51,51);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assets/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_dialog_button.setIcon(icon1)
        self.close_dialog_button.setIconSize(QSize(22, 22))
        self.close_dialog_button.setAutoDefault(False)
        self.close_dialog_button.setFlat(True)

        self.horizontalLayout.addWidget(self.close_dialog_button)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.frame_2)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_bottom.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_bottom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(15, -1, 35, 0)
        self.dialog_ok_button = QPushButton(self.frame_bottom)
        self.dialog_ok_button.setObjectName(u"dialog_ok_button")
        self.dialog_ok_button.setMinimumSize(QSize(85, 30))
        self.dialog_ok_button.setMaximumSize(QSize(85, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.dialog_ok_button.setFont(font1)
        self.dialog_ok_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}")
        self.dialog_ok_button.setAutoDefault(False)

        self.gridLayout.addWidget(self.dialog_ok_button, 1, 3, 1, 1)

        self.lab_icon = QLabel(self.frame_bottom)
        self.lab_icon.setObjectName(u"lab_icon")
        self.lab_icon.setMinimumSize(QSize(40, 40))
        self.lab_icon.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.lab_icon, 0, 0, 1, 1)

        self.dialog_cancel_button = QPushButton(self.frame_bottom)
        self.dialog_cancel_button.setObjectName(u"dialog_cancel_button")
        self.dialog_cancel_button.setMinimumSize(QSize(85, 30))
        self.dialog_cancel_button.setMaximumSize(QSize(85, 30))
        self.dialog_cancel_button.setFont(font1)
        self.dialog_cancel_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}")
        self.dialog_cancel_button.setAutoDefault(False)

        self.gridLayout.addWidget(self.dialog_cancel_button, 1, 2, 1, 1)

        self.lab_message = QLabel(self.frame_bottom)
        self.lab_message.setObjectName(u"lab_message")
        self.lab_message.setFont(font1)
        self.lab_message.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_message.setWordWrap(True)

        self.gridLayout.addWidget(self.lab_message, 0, 1, 1, 3)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lab_heading.setText("")
        self.minimize_dialog_button.setText("")
        self.close_dialog_button.setText("")
        self.dialog_ok_button.setText("")
        self.lab_icon.setText("")
        self.dialog_cancel_button.setText("")
        self.lab_message.setText("")
    # retranslateUi

