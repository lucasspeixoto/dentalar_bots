# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(916, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setFont(font)
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        font1.setPointSize(24)
        self.lab_appname.setFont(font1)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_appname.setMargin(2)
        self.lab_appname.setIndent(5)

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font1)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lab_person = QLabel(self.frame_person)
        self.lab_person.setObjectName(u"lab_person")
        self.lab_person.setMaximumSize(QSize(55, 55))
        self.lab_person.setPixmap(QPixmap(u"icons/1x/people.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_person)


        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setAcceptDrops(False)
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_whatsapp = QFrame(self.frame_bottom_west)
        self.frame_whatsapp.setObjectName(u"frame_whatsapp")
        self.frame_whatsapp.setMinimumSize(QSize(80, 55))
        self.frame_whatsapp.setMaximumSize(QSize(160, 55))
        self.frame_whatsapp.setFrameShape(QFrame.NoFrame)
        self.frame_whatsapp.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_whatsapp)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.menu_whatsapp_button = QPushButton(self.frame_whatsapp)
        self.menu_whatsapp_button.setObjectName(u"menu_whatsapp_button")
        self.menu_whatsapp_button.setMinimumSize(QSize(80, 55))
        self.menu_whatsapp_button.setMaximumSize(QSize(160, 55))
        self.menu_whatsapp_button.setFont(font)
        self.menu_whatsapp_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/whatsappAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_whatsapp_button.setIcon(icon4)
        self.menu_whatsapp_button.setIconSize(QSize(22, 22))
        self.menu_whatsapp_button.setFlat(True)

        self.horizontalLayout_15.addWidget(self.menu_whatsapp_button)


        self.verticalLayout_3.addWidget(self.frame_whatsapp)

        self.frame_bug = QFrame(self.frame_bottom_west)
        self.frame_bug.setObjectName(u"frame_bug")
        self.frame_bug.setMinimumSize(QSize(80, 55))
        self.frame_bug.setMaximumSize(QSize(160, 55))
        self.frame_bug.setFrameShape(QFrame.NoFrame)
        self.frame_bug.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_bug)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.menu_email_button = QPushButton(self.frame_bug)
        self.menu_email_button.setObjectName(u"menu_email_button")
        self.menu_email_button.setMinimumSize(QSize(80, 55))
        self.menu_email_button.setMaximumSize(QSize(160, 55))
        self.menu_email_button.setFont(font)
        self.menu_email_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/emailsAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_email_button.setIcon(icon5)
        self.menu_email_button.setIconSize(QSize(22, 22))
        self.menu_email_button.setFlat(True)

        self.horizontalLayout_16.addWidget(self.menu_email_button)


        self.verticalLayout_3.addWidget(self.frame_bug)

        self.frame_cloud = QFrame(self.frame_bottom_west)
        self.frame_cloud.setObjectName(u"frame_cloud")
        self.frame_cloud.setMinimumSize(QSize(80, 55))
        self.frame_cloud.setMaximumSize(QSize(160, 55))
        self.frame_cloud.setFrameShape(QFrame.NoFrame)
        self.frame_cloud.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_cloud = QPushButton(self.frame_cloud)
        self.bn_cloud.setObjectName(u"bn_cloud")
        self.bn_cloud.setMinimumSize(QSize(80, 55))
        self.bn_cloud.setMaximumSize(QSize(160, 55))
        self.bn_cloud.setFont(font)
        self.bn_cloud.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/cloudAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_cloud.setIcon(icon6)
        self.bn_cloud.setIconSize(QSize(22, 22))
        self.bn_cloud.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_cloud)


        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_android = QFrame(self.frame_bottom_west)
        self.frame_android.setObjectName(u"frame_android")
        self.frame_android.setMinimumSize(QSize(80, 55))
        self.frame_android.setMaximumSize(QSize(160, 55))
        self.frame_android.setFrameShape(QFrame.NoFrame)
        self.frame_android.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.menu_user_button = QPushButton(self.frame_android)
        self.menu_user_button.setObjectName(u"menu_user_button")
        self.menu_user_button.setMinimumSize(QSize(80, 55))
        self.menu_user_button.setMaximumSize(QSize(160, 55))
        self.menu_user_button.setFont(font)
        self.menu_user_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/userAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_user_button.setIcon(icon7)
        self.menu_user_button.setIconSize(QSize(20, 22))
        self.menu_user_button.setFlat(True)

        self.horizontalLayout_18.addWidget(self.menu_user_button)


        self.verticalLayout_3.addWidget(self.frame_android)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setKerning(True)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setStyleSheet(u"")
        self.page_whatsapp = QWidget()
        self.page_whatsapp.setObjectName(u"page_whatsapp")
        self.page_whatsapp.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_whatsapp)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_whatsapp_main = QFrame(self.page_whatsapp)
        self.frame_whatsapp_main.setObjectName(u"frame_whatsapp_main")
        self.frame_whatsapp_main.setEnabled(True)
        self.frame_whatsapp_main.setMinimumSize(QSize(0, 0))
        self.frame_whatsapp_main.setBaseSize(QSize(0, 0))
        self.frame_whatsapp_main.setFont(font)
        self.frame_whatsapp_main.setFrameShape(QFrame.NoFrame)
        self.frame_whatsapp_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_whatsapp_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.whatsapp_page_messages_frame_text = QLabel(self.frame_whatsapp_main)
        self.whatsapp_page_messages_frame_text.setObjectName(u"whatsapp_page_messages_frame_text")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(22)
        self.whatsapp_page_messages_frame_text.setFont(font3)
        self.whatsapp_page_messages_frame_text.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.whatsapp_page_messages_frame_text.setTextFormat(Qt.RichText)

        self.verticalLayout_5.addWidget(self.whatsapp_page_messages_frame_text)

        self.whatsapp_message_input = QTextEdit(self.frame_whatsapp_main)
        self.whatsapp_message_input.setObjectName(u"whatsapp_message_input")
        self.whatsapp_message_input.setEnabled(True)
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        self.whatsapp_message_input.setFont(font4)

        self.verticalLayout_5.addWidget(self.whatsapp_message_input)

        self.attachments_groupbox = QGroupBox(self.frame_whatsapp_main)
        self.attachments_groupbox.setObjectName(u"attachments_groupbox")
        self.attachments_groupbox.setMinimumSize(QSize(0, 90))
        self.attachments_groupbox.setFont(font)
        self.attachments_groupbox.setStyleSheet(u"QGroupBox {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.load_image_button = QPushButton(self.attachments_groupbox)
        self.load_image_button.setObjectName(u"load_image_button")
        self.load_image_button.setGeometry(QRect(10, 40, 75, 30))
        self.load_image_button.setMinimumSize(QSize(0, 30))
        self.load_image_button.setFont(font)
        self.load_image_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.load_file_button = QPushButton(self.attachments_groupbox)
        self.load_file_button.setObjectName(u"load_file_button")
        self.load_file_button.setEnabled(False)
        self.load_file_button.setGeometry(QRect(100, 40, 75, 30))
        self.load_file_button.setMinimumSize(QSize(0, 30))
        self.load_file_button.setFont(font)
        self.load_file_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.selected_whatsapp_image_path_text = QLabel(self.attachments_groupbox)
        self.selected_whatsapp_image_path_text.setObjectName(u"selected_whatsapp_image_path_text")
        self.selected_whatsapp_image_path_text.setGeometry(QRect(180, 20, 271, 61))
        self.selected_whatsapp_image_path_text.setMinimumSize(QSize(200, 0))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(True)
        font5.setWeight(75)
        self.selected_whatsapp_image_path_text.setFont(font5)
        self.selected_whatsapp_image_path_text.setLayoutDirection(Qt.LeftToRight)
        self.selected_whatsapp_image_path_text.setAutoFillBackground(False)
        self.selected_whatsapp_image_path_text.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"	\n"
"}")
        self.selected_whatsapp_image_path_text.setTextFormat(Qt.RichText)
        self.selected_whatsapp_image_path_text.setScaledContents(False)
        self.selected_whatsapp_image_path_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.selected_whatsapp_image_path_text.setWordWrap(True)
        self.selected_whatsapp_image_path_text.setMargin(1)
        self.selected_whatsapp_image_path_text.setIndent(1)
        self.selected_whatsapp_image_path_text.setOpenExternalLinks(False)

        self.verticalLayout_5.addWidget(self.attachments_groupbox)


        self.horizontalLayout_19.addWidget(self.frame_whatsapp_main)

        self.vert_divide = QFrame(self.page_whatsapp)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFont(font)
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_whatsapp_contacts = QFrame(self.page_whatsapp)
        self.frame_whatsapp_contacts.setObjectName(u"frame_whatsapp_contacts")
        self.frame_whatsapp_contacts.setMinimumSize(QSize(350, 0))
        self.frame_whatsapp_contacts.setMaximumSize(QSize(220, 16777215))
        self.frame_whatsapp_contacts.setFrameShape(QFrame.NoFrame)
        self.frame_whatsapp_contacts.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_whatsapp_contacts)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.whatsapp_page_contacts_frame_text = QLabel(self.frame_whatsapp_contacts)
        self.whatsapp_page_contacts_frame_text.setObjectName(u"whatsapp_page_contacts_frame_text")
        self.whatsapp_page_contacts_frame_text.setMinimumSize(QSize(0, 40))
        self.whatsapp_page_contacts_frame_text.setMaximumSize(QSize(16777215, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semilight")
        font6.setPointSize(22)
        self.whatsapp_page_contacts_frame_text.setFont(font6)
        self.whatsapp_page_contacts_frame_text.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.whatsapp_page_contacts_frame_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.whatsapp_page_contacts_frame_text)

        self.load_contacts_button = QPushButton(self.frame_whatsapp_contacts)
        self.load_contacts_button.setObjectName(u"load_contacts_button")
        self.load_contacts_button.setEnabled(True)
        self.load_contacts_button.setMinimumSize(QSize(0, 30))
        self.load_contacts_button.setMaximumSize(QSize(16777215, 16777215))
        self.load_contacts_button.setFont(font)
        self.load_contacts_button.setMouseTracking(False)
        self.load_contacts_button.setToolTipDuration(-1)
        self.load_contacts_button.setAutoFillBackground(False)
        self.load_contacts_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.load_contacts_button.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.load_contacts_button.setAutoDefault(False)
        self.load_contacts_button.setFlat(False)

        self.verticalLayout_6.addWidget(self.load_contacts_button)

        self.contacts_list = QListWidget(self.frame_whatsapp_contacts)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        __qlistwidgetitem = QListWidgetItem(self.contacts_list)
        __qlistwidgetitem.setFont(font7);
        __qlistwidgetitem.setBackground(brush1);
        __qlistwidgetitem.setForeground(brush);
        self.contacts_list.setObjectName(u"contacts_list")
        self.contacts_list.setEnabled(True)
        self.contacts_list.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setPointSize(12)
        self.contacts_list.setFont(font8)
        self.contacts_list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.contacts_list.setSelectionRectVisible(False)

        self.verticalLayout_6.addWidget(self.contacts_list)

        self.contacts_groupbox = QGroupBox(self.frame_whatsapp_contacts)
        self.contacts_groupbox.setObjectName(u"contacts_groupbox")
        self.contacts_groupbox.setMinimumSize(QSize(0, 70))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setWeight(50)
        self.contacts_groupbox.setFont(font9)
        self.contacts_groupbox.setStyleSheet(u"QGroupBox {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.clear_contacts_list_button = QPushButton(self.contacts_groupbox)
        self.clear_contacts_list_button.setObjectName(u"clear_contacts_list_button")
        self.clear_contacts_list_button.setEnabled(False)
        self.clear_contacts_list_button.setGeometry(QRect(100, 30, 85, 30))
        self.clear_contacts_list_button.setFont(font)
        self.clear_contacts_list_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.send_to_all_contacts_checkbox = QCheckBox(self.contacts_groupbox)
        self.send_to_all_contacts_checkbox.setObjectName(u"send_to_all_contacts_checkbox")
        self.send_to_all_contacts_checkbox.setGeometry(QRect(10, 30, 85, 30))
        self.send_to_all_contacts_checkbox.setFont(font)
        self.send_to_all_contacts_checkbox.setStyleSheet(u"QCheckBox {\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QCheckBox:hover {\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_6.addWidget(self.contacts_groupbox)

        self.whatsapp_send_messages_groupbox = QGroupBox(self.frame_whatsapp_contacts)
        self.whatsapp_send_messages_groupbox.setObjectName(u"whatsapp_send_messages_groupbox")
        self.whatsapp_send_messages_groupbox.setMinimumSize(QSize(0, 70))
        self.whatsapp_send_messages_groupbox.setFont(font)
        self.whatsapp_send_messages_groupbox.setStyleSheet(u"QGroupBox {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.send_whatsapp_messages_button = QPushButton(self.whatsapp_send_messages_groupbox)
        self.send_whatsapp_messages_button.setObjectName(u"send_whatsapp_messages_button")
        self.send_whatsapp_messages_button.setEnabled(False)
        self.send_whatsapp_messages_button.setGeometry(QRect(240, 30, 85, 30))
        self.send_whatsapp_messages_button.setFont(font)
        self.send_whatsapp_messages_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.validate_whatsapp_sending_button = QPushButton(self.whatsapp_send_messages_groupbox)
        self.validate_whatsapp_sending_button.setObjectName(u"validate_whatsapp_sending_button")
        self.validate_whatsapp_sending_button.setGeometry(QRect(20, 30, 85, 30))
        self.validate_whatsapp_sending_button.setFont(font)
        self.validate_whatsapp_sending_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.reset_validations_whatsapp_sending_button = QPushButton(self.whatsapp_send_messages_groupbox)
        self.reset_validations_whatsapp_sending_button.setObjectName(u"reset_validations_whatsapp_sending_button")
        self.reset_validations_whatsapp_sending_button.setGeometry(QRect(130, 30, 85, 30))
        self.reset_validations_whatsapp_sending_button.setFont(font)
        self.reset_validations_whatsapp_sending_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_6.addWidget(self.whatsapp_send_messages_groupbox)


        self.horizontalLayout_19.addWidget(self.frame_whatsapp_contacts)

        self.stackedWidget.addWidget(self.page_whatsapp)
        self.page_whatsapp_help = QWidget()
        self.page_whatsapp_help.setObjectName(u"page_whatsapp_help")
        self.page_whatsapp_help.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_13 = QVBoxLayout(self.page_whatsapp_help)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_whatsapp_help)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(24)
        self.lab_about_home.setFont(font10)
        self.lab_about_home.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_whatsapp_help = QFrame(self.page_whatsapp_help)
        self.frame_whatsapp_help.setObjectName(u"frame_whatsapp_help")
        self.frame_whatsapp_help.setFrameShape(QFrame.StyledPanel)
        self.frame_whatsapp_help.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_whatsapp_help)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_whatsapp_page_help = QTextEdit(self.frame_whatsapp_help)
        self.text_whatsapp_page_help.setObjectName(u"text_whatsapp_page_help")
        self.text_whatsapp_page_help.setEnabled(True)
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(10)
        self.text_whatsapp_page_help.setFont(font11)
        self.text_whatsapp_page_help.setStyleSheet(u"color:rgb(255,255,255);")
        self.text_whatsapp_page_help.setFrameShape(QFrame.NoFrame)
        self.text_whatsapp_page_help.setFrameShadow(QFrame.Plain)
        self.text_whatsapp_page_help.setReadOnly(True)
        self.text_whatsapp_page_help.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_whatsapp_page_help)

        self.vsb_whatsapp_page_help = QScrollBar(self.frame_whatsapp_help)
        self.vsb_whatsapp_page_help.setObjectName(u"vsb_whatsapp_page_help")
        self.vsb_whatsapp_page_help.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_whatsapp_page_help.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.vsb_whatsapp_page_help)


        self.verticalLayout_13.addWidget(self.frame_whatsapp_help)

        self.stackedWidget.addWidget(self.page_whatsapp_help)
        self.page_about_cloud = QWidget()
        self.page_about_cloud.setObjectName(u"page_about_cloud")
        self.page_about_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cloud)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_10 = QLabel(self.page_about_cloud)
        self.label_10.setObjectName(u"label_10")
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(30)
        self.label_10.setFont(font12)
        self.label_10.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.page_about_cloud)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName(u"page_about_android")
        self.page_about_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName(u"page_about_bug")
        self.page_about_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_bug)
        self.page_bug = QWidget()
        self.page_bug.setObjectName(u"page_bug")
        self.page_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_7 = QVBoxLayout(self.page_bug)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.lab_Bug = QLabel(self.page_bug)
        self.lab_Bug.setObjectName(u"lab_Bug")
        self.lab_Bug.setMinimumSize(QSize(0, 55))
        self.lab_Bug.setMaximumSize(QSize(16777215, 55))
        font13 = QFont()
        font13.setFamily(u"Segoe UI Semilight")
        font13.setPointSize(24)
        self.lab_Bug.setFont(font13)
        self.lab_Bug.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_7.addWidget(self.lab_Bug)

        self.verticalSpacer = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_bug)
        self.page_cloud = QWidget()
        self.page_cloud.setObjectName(u"page_cloud")
        self.page_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cloud)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.lab_cloud_main = QLabel(self.page_cloud)
        self.lab_cloud_main.setObjectName(u"lab_cloud_main")
        self.lab_cloud_main.setMinimumSize(QSize(0, 55))
        self.lab_cloud_main.setMaximumSize(QSize(16777215, 55))
        self.lab_cloud_main.setFont(font10)
        self.lab_cloud_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.lab_cloud_main)

        self.frame_2 = QFrame(self.page_cloud)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 235))
        self.frame_2.setMaximumSize(QSize(16777215, 235))
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.line_cloud_adress = QLineEdit(self.frame_2)
        self.line_cloud_adress.setObjectName(u"line_cloud_adress")
        self.line_cloud_adress.setMinimumSize(QSize(400, 25))
        self.line_cloud_adress.setMaximumSize(QSize(500, 25))
        self.line_cloud_adress.setFont(font)
        self.line_cloud_adress.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_cloud_adress, 1, 1, 1, 3)

        self.line_cloud_id = QLineEdit(self.frame_2)
        self.line_cloud_id.setObjectName(u"line_cloud_id")
        self.line_cloud_id.setEnabled(True)
        self.line_cloud_id.setMinimumSize(QSize(400, 25))
        self.line_cloud_id.setMaximumSize(QSize(500, 25))
        self.line_cloud_id.setFont(font)
        self.line_cloud_id.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_cloud_id, 0, 1, 1, 3)

        self.bn_cloud_connect = QPushButton(self.frame_2)
        self.bn_cloud_connect.setObjectName(u"bn_cloud_connect")
        self.bn_cloud_connect.setMinimumSize(QSize(85, 30))
        self.bn_cloud_connect.setMaximumSize(QSize(85, 30))
        self.bn_cloud_connect.setFont(font)
        self.bn_cloud_connect.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_cloud_connect, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 2)

        self.bn_cloud_clear = QPushButton(self.frame_2)
        self.bn_cloud_clear.setObjectName(u"bn_cloud_clear")
        self.bn_cloud_clear.setEnabled(True)
        self.bn_cloud_clear.setMinimumSize(QSize(85, 30))
        self.bn_cloud_clear.setMaximumSize(QSize(85, 30))
        self.bn_cloud_clear.setFont(font)
        self.bn_cloud_clear.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_cloud_clear, 2, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_cloud)
        self.page_android = QWidget()
        self.page_android.setObjectName(u"page_android")
        self.page_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_android)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_android_menu = QFrame(self.page_android)
        self.frame_android_menu.setObjectName(u"frame_android_menu")
        self.frame_android_menu.setMinimumSize(QSize(0, 30))
        self.frame_android_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_android_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_android_menu.setFrameShape(QFrame.NoFrame)
        self.frame_android_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_android_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_android_contact = QFrame(self.frame_android_menu)
        self.frame_android_contact.setObjectName(u"frame_android_contact")
        self.frame_android_contact.setMinimumSize(QSize(80, 30))
        self.frame_android_contact.setMaximumSize(QSize(80, 30))
        self.frame_android_contact.setFrameShape(QFrame.NoFrame)
        self.frame_android_contact.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_android_contact)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.menu_user_button_contact = QPushButton(self.frame_android_contact)
        self.menu_user_button_contact.setObjectName(u"menu_user_button_contact")
        self.menu_user_button_contact.setMinimumSize(QSize(80, 30))
        self.menu_user_button_contact.setMaximumSize(QSize(80, 30))
        self.menu_user_button_contact.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/1x/userInfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_user_button_contact.setIcon(icon8)
        self.menu_user_button_contact.setIconSize(QSize(13, 16))
        self.menu_user_button_contact.setFlat(True)

        self.horizontalLayout_21.addWidget(self.menu_user_button_contact)


        self.horizontalLayout_20.addWidget(self.frame_android_contact)

        self.frame_android_game = QFrame(self.frame_android_menu)
        self.frame_android_game.setObjectName(u"frame_android_game")
        self.frame_android_game.setMinimumSize(QSize(80, 30))
        self.frame_android_game.setMaximumSize(QSize(80, 30))
        self.frame_android_game.setFrameShape(QFrame.NoFrame)
        self.frame_android_game.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_android_game)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.menu_user_button_game = QPushButton(self.frame_android_game)
        self.menu_user_button_game.setObjectName(u"menu_user_button_game")
        self.menu_user_button_game.setMinimumSize(QSize(80, 30))
        self.menu_user_button_game.setMaximumSize(QSize(80, 30))
        self.menu_user_button_game.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"icons/1x/notations.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_user_button_game.setIcon(icon9)
        self.menu_user_button_game.setIconSize(QSize(20, 13))
        self.menu_user_button_game.setFlat(True)

        self.horizontalLayout_22.addWidget(self.menu_user_button_game)


        self.horizontalLayout_20.addWidget(self.frame_android_game)

        self.frame_android_clean = QFrame(self.frame_android_menu)
        self.frame_android_clean.setObjectName(u"frame_android_clean")
        self.frame_android_clean.setMinimumSize(QSize(80, 30))
        self.frame_android_clean.setMaximumSize(QSize(80, 30))
        self.frame_android_clean.setFrameShape(QFrame.NoFrame)
        self.frame_android_clean.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_android_clean)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.menu_user_button_clean = QPushButton(self.frame_android_clean)
        self.menu_user_button_clean.setObjectName(u"menu_user_button_clean")
        self.menu_user_button_clean.setMinimumSize(QSize(80, 30))
        self.menu_user_button_clean.setMaximumSize(QSize(80, 30))
        self.menu_user_button_clean.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"icons/1x/cleanAsset 59.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_user_button_clean.setIcon(icon10)
        self.menu_user_button_clean.setFlat(True)

        self.horizontalLayout_23.addWidget(self.menu_user_button_clean)


        self.horizontalLayout_20.addWidget(self.frame_android_clean)

        self.frame_android_world = QFrame(self.frame_android_menu)
        self.frame_android_world.setObjectName(u"frame_android_world")
        self.frame_android_world.setMinimumSize(QSize(80, 30))
        self.frame_android_world.setMaximumSize(QSize(80, 30))
        self.frame_android_world.setFrameShape(QFrame.NoFrame)
        self.frame_android_world.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_android_world)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.menu_user_button_world = QPushButton(self.frame_android_world)
        self.menu_user_button_world.setObjectName(u"menu_user_button_world")
        self.menu_user_button_world.setMinimumSize(QSize(80, 30))
        self.menu_user_button_world.setMaximumSize(QSize(80, 30))
        self.menu_user_button_world.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"icons/1x/worldAsset 60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_user_button_world.setIcon(icon11)
        self.menu_user_button_world.setFlat(True)

        self.horizontalLayout_24.addWidget(self.menu_user_button_world)


        self.horizontalLayout_20.addWidget(self.frame_android_world)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_android_menu)

        self.stackedWidget_android = QStackedWidget(self.page_android)
        self.stackedWidget_android.setObjectName(u"stackedWidget_android")
        self.stackedWidget_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_android_contact = QWidget()
        self.page_android_contact.setObjectName(u"page_android_contact")
        self.page_android_contact.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_android_contact)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.lab_android_contact = QLabel(self.page_android_contact)
        self.lab_android_contact.setObjectName(u"lab_android_contact")
        self.lab_android_contact.setMinimumSize(QSize(0, 55))
        self.lab_android_contact.setMaximumSize(QSize(16777215, 55))
        self.lab_android_contact.setFont(font10)
        self.lab_android_contact.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.lab_android_contact)

        self.frame_android_bottom = QFrame(self.page_android_contact)
        self.frame_android_bottom.setObjectName(u"frame_android_bottom")
        self.frame_android_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_android_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_android_bottom)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lab_person_icon = QLabel(self.frame_android_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 130))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setLayoutDirection(Qt.LeftToRight)
        self.lab_person_icon.setFrameShape(QFrame.NoFrame)
        self.lab_person_icon.setFrameShadow(QFrame.Plain)
        self.lab_person_icon.setPixmap(QPixmap(u"icons/1x/userAsset512.png"))
        self.lab_person_icon.setScaledContents(True)
        self.lab_person_icon.setIndent(0)

        self.gridLayout_3.addWidget(self.lab_person_icon, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_android_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.frame_android_field)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

        self.label_7 = QLabel(self.frame_android_field)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_7, 5, 0, 1, 1)

        self.line_android_name = QLineEdit(self.frame_android_field)
        self.line_android_name.setObjectName(u"line_android_name")
        self.line_android_name.setEnabled(False)
        self.line_android_name.setMinimumSize(QSize(300, 25))
        self.line_android_name.setMaximumSize(QSize(400, 25))
        self.line_android_name.setFont(font)
        self.line_android_name.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_name, 1, 3, 1, 1)

        self.label_6 = QLabel(self.frame_android_field)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.line_android_adress = QLineEdit(self.frame_android_field)
        self.line_android_adress.setObjectName(u"line_android_adress")
        self.line_android_adress.setEnabled(False)
        self.line_android_adress.setMinimumSize(QSize(300, 25))
        self.line_android_adress.setMaximumSize(QSize(400, 25))
        self.line_android_adress.setFont(font)
        self.line_android_adress.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_adress, 3, 3, 1, 1)

        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 3)

        self.line_android_email = QLineEdit(self.frame_android_field)
        self.line_android_email.setObjectName(u"line_android_email")
        self.line_android_email.setEnabled(False)
        self.line_android_email.setMinimumSize(QSize(300, 25))
        self.line_android_email.setMaximumSize(QSize(400, 25))
        self.line_android_email.setFont(font)
        self.line_android_email.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_email, 5, 3, 1, 1)

        self.line_android_org = QLineEdit(self.frame_android_field)
        self.line_android_org.setObjectName(u"line_android_org")
        self.line_android_org.setEnabled(False)
        self.line_android_org.setMinimumSize(QSize(300, 25))
        self.line_android_org.setMaximumSize(QSize(400, 25))
        self.line_android_org.setFont(font)
        self.line_android_org.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_org, 4, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 4, 8, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 7, 8, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 8, 3, 1, 1)

        self.frame_3 = QFrame(self.frame_android_field)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(100, 0, 0, 0)
        self.user_contact_edit_button = QPushButton(self.frame_3)
        self.user_contact_edit_button.setObjectName(u"user_contact_edit_button")
        self.user_contact_edit_button.setMinimumSize(QSize(85, 30))
        self.user_contact_edit_button.setMaximumSize(QSize(85, 30))
        self.user_contact_edit_button.setFont(font)
        self.user_contact_edit_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.user_contact_edit_button)

        self.user_contact_delete_button = QPushButton(self.frame_3)
        self.user_contact_delete_button.setObjectName(u"user_contact_delete_button")
        self.user_contact_delete_button.setMinimumSize(QSize(85, 30))
        self.user_contact_delete_button.setMaximumSize(QSize(85, 30))
        self.user_contact_delete_button.setFont(font)
        self.user_contact_delete_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.user_contact_delete_button)

        self.user_contact_save_button = QPushButton(self.frame_3)
        self.user_contact_save_button.setObjectName(u"user_contact_save_button")
        self.user_contact_save_button.setEnabled(False)
        self.user_contact_save_button.setMinimumSize(QSize(85, 30))
        self.user_contact_save_button.setMaximumSize(QSize(85, 30))
        self.user_contact_save_button.setFont(font)
        self.user_contact_save_button.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.user_contact_save_button)


        self.gridLayout_4.addWidget(self.frame_3, 7, 0, 1, 7)


        self.gridLayout_3.addWidget(self.frame_android_field, 0, 1, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_android.addWidget(self.page_android_contact)
        self.page_android_game = QWidget()
        self.page_android_game.setObjectName(u"page_android_game")
        self.page_android_game.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_game)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.lab_gamepad = QLabel(self.page_android_game)
        self.lab_gamepad.setObjectName(u"lab_gamepad")
        self.lab_gamepad.setMinimumSize(QSize(0, 55))
        self.lab_gamepad.setMaximumSize(QSize(16777215, 55))
        self.lab_gamepad.setFont(font10)
        self.lab_gamepad.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_11.addWidget(self.lab_gamepad)

        self.frame_textbar = QFrame(self.page_android_game)
        self.frame_textbar.setObjectName(u"frame_textbar")
        self.frame_textbar.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_textbar)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.user_notations_input = QTextEdit(self.frame_textbar)
        self.user_notations_input.setObjectName(u"user_notations_input")
        self.user_notations_input.setFont(font)
        self.user_notations_input.setStyleSheet(u"color:rgb(255,255,255);")
        self.user_notations_input.setFrameShape(QFrame.NoFrame)
        self.user_notations_input.setFrameShadow(QFrame.Plain)
        self.user_notations_input.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.user_notations_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_26.addWidget(self.user_notations_input)

        self.vsb_gamepad = QScrollBar(self.frame_textbar)
        self.vsb_gamepad.setObjectName(u"vsb_gamepad")
        self.vsb_gamepad.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_gamepad.setOrientation(Qt.Vertical)
        self.vsb_gamepad.setInvertedControls(True)

        self.horizontalLayout_26.addWidget(self.vsb_gamepad)


        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.stackedWidget_android.addWidget(self.page_android_game)
        self.page_android_clean = QWidget()
        self.page_android_clean.setObjectName(u"page_android_clean")
        self.page_android_clean.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_android_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 5, 1, 1)

        self.groupBox_clean = QGroupBox(self.page_android_clean)
        self.groupBox_clean.setObjectName(u"groupBox_clean")
        self.groupBox_clean.setMinimumSize(QSize(250, 300))
        self.groupBox_clean.setMaximumSize(QSize(250, 300))
        self.groupBox_clean.setSizeIncrement(QSize(0, 0))
        self.groupBox_clean.setFont(font11)
        self.groupBox_clean.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.groupBox_clean.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_clean.setFlat(False)
        self.groupBox_clean.setCheckable(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_clean)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton = QRadioButton(self.groupBox_clean)
        self.radioButton.setObjectName(u"radioButton")
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(9)
        self.radioButton.setFont(font14)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_clean)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font14)
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_2.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_clean)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font14)
        self.radioButton_3.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_3.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_clean)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font14)
        self.radioButton_4.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_4.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_4)

        self.checkBox = QCheckBox(self.groupBox_clean)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font14)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.checkBox.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox)

        self.checkBox_4 = QCheckBox(self.groupBox_clean)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font14)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.checkBox_4.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox_4)

        self.checkBox_2 = QCheckBox(self.groupBox_clean)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font14)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_clean)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font14)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.checkBox_3)


        self.gridLayout_5.addWidget(self.groupBox_clean, 0, 0, 1, 1)

        self.lab_clean = QLabel(self.page_android_clean)
        self.lab_clean.setObjectName(u"lab_clean")
        self.lab_clean.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lab_clean, 0, 1, 2, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 2, 1)

        self.groupBox = QGroupBox(self.page_android_clean)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 300))
        self.groupBox.setMaximumSize(QSize(250, 300))
        self.groupBox.setFont(font14)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSlider_2 = QSlider(self.groupBox)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:rgb(0,143,170);\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_2, 0, 0, 1, 1)

        self.verticalSlider = QSlider(self.groupBox)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: red;\n"
"    width:5px\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background:rgb(0,143,170);\n"
"	margin:0 -8px\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.verticalSlider.setTracking(True)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_6.addWidget(self.verticalSlider, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 3, 1, 1)

        self.stackedWidget_android.addWidget(self.page_android_clean)
        self.page_android_world = QWidget()
        self.page_android_world.setObjectName(u"page_android_world")
        self.page_android_world.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_27 = QHBoxLayout(self.page_android_world)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_9 = QLabel(self.page_android_world)
        self.label_9.setObjectName(u"label_9")
        font15 = QFont()
        font15.setFamily(u"Segoe UI Light")
        font15.setPointSize(30)
        self.label_9.setFont(font15)
        self.label_9.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_9)

        self.stackedWidget_android.addWidget(self.page_android_world)

        self.verticalLayout_9.addWidget(self.stackedWidget_android)

        self.stackedWidget.addWidget(self.page_android)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        self.frame_tab.setMinimumSize(QSize(0, 0))
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font16)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        self.lab_tab.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_tab.setTextFormat(Qt.RichText)
        self.lab_tab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lab_tab.setWordWrap(True)
        self.lab_tab.setMargin(0)
        self.lab_tab.setIndent(-1)

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)
        self.load_contacts_button.setDefault(False)
        self.stackedWidget_android.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Automa\u00e7\u00f5es</p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">User</span></p></body></html>", None))
        self.lab_person.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.menu_whatsapp_button.setToolTip(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
#endif // QT_CONFIG(tooltip)
        self.menu_whatsapp_button.setText("")
#if QT_CONFIG(tooltip)
        self.menu_email_button.setToolTip(QCoreApplication.translate("MainWindow", u"E-mails", None))
#endif // QT_CONFIG(tooltip)
        self.menu_email_button.setText("")
#if QT_CONFIG(tooltip)
        self.bn_cloud.setToolTip(QCoreApplication.translate("MainWindow", u"Conex\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.bn_cloud.setText("")
#if QT_CONFIG(tooltip)
        self.menu_user_button.setToolTip(QCoreApplication.translate("MainWindow", u"Android", None))
#endif // QT_CONFIG(tooltip)
        self.menu_user_button.setText("")
        self.whatsapp_page_messages_frame_text.setText(QCoreApplication.translate("MainWindow", u"Mensagem de Texto", None))
        self.attachments_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Anexos", None))
        self.load_image_button.setText(QCoreApplication.translate("MainWindow", u"Imagem", None))
        self.load_file_button.setText(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.selected_whatsapp_image_path_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.whatsapp_page_contacts_frame_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Contatos</p></body></html>", None))
        self.load_contacts_button.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))

        __sortingEnabled = self.contacts_list.isSortingEnabled()
        self.contacts_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.contacts_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Carregue Contatos...", None));
        self.contacts_list.setSortingEnabled(__sortingEnabled)

        self.contacts_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o", None))
        self.clear_contacts_list_button.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.send_to_all_contacts_checkbox.setText(QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.whatsapp_send_messages_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Envio", None))
        self.send_whatsapp_messages_button.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.validate_whatsapp_sending_button.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.reset_validations_whatsapp_sending_button.setText(QCoreApplication.translate("MainWindow", u"Resetar", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"Ajuda: Bots", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.lab_Bug.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">E-mails</span></p></body></html>", None))
        self.lab_cloud_main.setText(QCoreApplication.translate("MainWindow", u"Conex\u00e3o E-mail", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.bn_cloud_connect.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.bn_cloud_clear.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
#if QT_CONFIG(tooltip)
        self.menu_user_button_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Contact", None))
#endif // QT_CONFIG(tooltip)
        self.menu_user_button_contact.setText("")
#if QT_CONFIG(tooltip)
        self.menu_user_button_game.setToolTip(QCoreApplication.translate("MainWindow", u"GamePad", None))
#endif // QT_CONFIG(tooltip)
        self.menu_user_button_game.setText("")
#if QT_CONFIG(tooltip)
        self.menu_user_button_clean.setToolTip(QCoreApplication.translate("MainWindow", u"Clean", None))
#endif // QT_CONFIG(tooltip)
        self.menu_user_button_clean.setText("")
#if QT_CONFIG(tooltip)
        self.menu_user_button_world.setToolTip(QCoreApplication.translate("MainWindow", u"World", None))
#endif // QT_CONFIG(tooltip)
        self.menu_user_button_world.setText("")
        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.lab_person_icon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.line_android_name.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Organiza\u00e7\u00e3o:", None))
        self.line_android_adress.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.line_android_email.setText("")
        self.line_android_org.setText("")
        self.user_contact_edit_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.user_contact_delete_button.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.user_contact_save_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.lab_gamepad.setText(QCoreApplication.translate("MainWindow", u"Anota\u00e7\u00f5es", None))
        self.groupBox_clean.setTitle(QCoreApplication.translate("MainWindow", u"Review", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Clean History", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Clean Password", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Clean Chache", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Clean Bookmarks", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Did you liked the UI", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Did you like the Color Scheme", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Did you like Custome Buttons", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Did you like the Stacked Window", None))
        self.lab_clean.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sliders", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lab_tab.setText("")
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

