# -*- coding: utf-8 -*-
# encoding: utf-8

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPropertyAnimation
from PySide2.QtWidgets import QFrame
from core.user.user import User

from main import *

from help import *

# * Necessery for checking weather the windown is full screen or not
GLOBAL_STATE = 0

# * Necessery for checking weather the windown is full screen or not
GLOBAL_TITLE_BAR = True

# * Necessery for initittion of the window.
init = False

"""
This class houses all function necessery for our programme to run


"""


class UIFunction:

    """
    Initial function to load the front stack widget
    and tab button i.e. whatsapp page.

    Initialising the welcome page to: whatsapp page in
    the stackedwidget, setting the bottom label as the
    page name, setting the button style.

    """

    def init_stack_tab(self):
        global init
        if init == False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_whatsapp)
            self.ui.footer_page_title.setText("WhatsApp")
            self.ui.frame_whatsapp.setStyleSheet("background:rgb(91,90,90)")
            init = True

    """
    Initial function to load the front stack widget
    and tab button i.e. whatsapp page.
    
    Initialising the welcome page to: whatsapp page in
    the stackedwidget, setting the bottom label as the
    page name, setting the button style.
        
    """

    def label_title(self, app_name: str):
        self.ui.app_name.setText(app_name)

    """
    This function maximises our mainwindow when the maximise
    button is pressed or if double mouse left press is doen
    over the topframa. This make the application to
    occupy the whole monitor.
        
    """

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.maximize_main_windown_button.setToolTip("Restaurar")
            self.ui.maximize_main_windown_button.setIcon(
                QtGui.QIcon("assets/images/restore.png")
            )
            self.ui.frame_drag.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.maximize_main_windown_button.setToolTip("Maximizar")
            self.ui.maximize_main_windown_button.setIcon(
                QtGui.QIcon("assets/images/max.png")
            )
            self.ui.frame_drag.show()

    """
    Return status max or restore necessery of 
    the maximise function to work.
        
    """

    def return_status():
        return GLOBAL_STATE

    """
    Set a new GLOBAL_STATE
        
    """

    def set_status(status: int):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    """
    Toodle menu function that toodles the menu bar to double
    the length opening a new are of about tab in front.
    also it sets the whatsapp as the first page.
    if the page is in the about page then pressing again will
    result in undoing the process and comming back to the
    whatsapp page
        
    """

    def toodle_menu(self, max_width: int, clicked: bool):
        """
        this line clears the bg of previous tabs : i.e
        making then normal color than lighter color.

        """

        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if clicked:
            # * Reads the current width of the frame
            current_width = self.ui.frame_bottom_west.width()

            # * Minimun width of the bottom_west frame
            min_width = 80
            if current_width == 80:
                extend = max_width
                # * Make the stacked widget page to ajuda > whatsapp page
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_whatsapp_help)
                self.ui.footer_page_title.setText("Ajuda > WhatsApp")
                self.ui.frame_whatsapp.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = min_width
                # * revert the Ajuda > WhatsApp page to normal WhatsApp page
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_whatsapp)
                self.ui.footer_page_title.setText("WhatsApp")
                self.ui.frame_whatsapp.setStyleSheet("background:rgb(91,90,90)")
            # * This animation is responsible for the toodle to move in a some fixed state.
            self.animation = QPropertyAnimation(
                self.ui.frame_bottom_west, b"minimumWidth"
            )
            self.animation.setDuration(300)
            self.animation.setStartValue(min_width)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def constant_function(self):
        # * Double click result in maximise of window
        def max_double_click(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        # * Remove normal title bar
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = max_double_click
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        """
        Since there is no windows topbar, the close min, max button
        are absent and so there is a need for the alternative
        buttons in our dialog box, which is carried out by the below code
        """
        # * Minimize button function
        self.ui.minimize_main_windown_button.clicked.connect(
            lambda: self.showMinimized()
        )

        # * Maximize/restore button function
        self.ui.maximize_main_windown_button.clicked.connect(
            lambda: UIFunction.maximize_restore(self)
        )

        # * Close application function button
        self.ui.close_main_windown_button.clicked.connect(lambda: self.close())

    """ 
    Button in tab pressed executes the corresponding page
    in stackedwidget pages
    """

    def change_user_page(self, button_name: str):

        index = self.ui.stackedWidget.currentIndex()

        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if button_name == "menu_whatsapp_button":
            if self.ui.frame_bottom_west.width() == 80 and index != 0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_whatsapp)
                self.ui.footer_page_title.setText("WhatsApp")
                self.ui.frame_whatsapp.setStyleSheet("background:rgb(91,90,90)")

            elif self.ui.frame_bottom_west.width() == 160 and index != 1:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_whatsapp_help)
                self.ui.footer_page_title.setText("Ajuda WhatsApp")
                self.ui.frame_whatsapp.setStyleSheet("background:rgb(91,90,90)")

        elif button_name == "menu_email_button":
            if self.ui.frame_bottom_west.width() == 80 and index != 5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
                self.ui.footer_page_title.setText("E-mails")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)")

            elif self.ui.frame_bottom_west.width() == 160 and index != 4:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
                self.ui.footer_page_title.setText("Ajuda > E-mails")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)")

        elif button_name == "menu_user_button":
            if self.ui.frame_bottom_west.width() == 80 and index != 7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
                self.ui.footer_page_title.setText("Usuário")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)")
                UIFunction.user_stack_pages(self, "page_contact")

            elif self.ui.frame_bottom_west.width() == 160 and index != 3:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_android)
                self.ui.footer_page_title.setText("Ajuda > Usuário")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)")

        elif button_name == "menu_connection_button":
            if self.ui.frame_bottom_west.width() == 80 and index != 6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_cloud)
                self.ui.footer_page_title.setText("Conexão E-mail")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)")

            elif self.ui.frame_bottom_west.width() == 160 and index != 2:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cloud)
                self.ui.footer_page_title.setText("Ajuda > Conexão E-mail")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)")

    """
    Stackwidget each page function page functions
    code to perfomr the task in the stacked widget page
    what ever widget is in the stacked pages its action is
    evaluated here and then the rest function is passed.
    """

    def stack_page(self):

        self.ui.emails_connect_button.clicked.connect(
            lambda: APFunction.emails_connect(self)
        )
        self.ui.emails_clear_fields_button.clicked.connect(
            lambda: APFunction.emails_clear_fields(self)
        )

        self.ui.user_contact_button.clicked.connect(
            lambda: UIFunction.user_stack_pages(self, "page_contact")
        )
        self.ui.user_notations_button.clicked.connect(
            lambda: UIFunction.user_stack_pages(self, "page_notations")
        )
        self.ui.user_clean_button.clicked.connect(
            lambda: UIFunction.user_stack_pages(self, "page_clean")
        )
        self.ui.user_world_button.clicked.connect(
            lambda: UIFunction.user_stack_pages(self, "page_world")
        )

        self.ui.user_contact_edit_button.clicked.connect(lambda: User.edit_user(self))

        self.ui.user_contact_save_button.clicked.connect(lambda: User.save_user(self))

        self.ui.user_contact_delete_button.clicked.connect(
            lambda: User.delete_user(self)
        )

        self.ui.user_notations_input.setVerticalScrollBar(self.ui.vsb_gamepad)

        self.ui.user_notations_input.setText(
            "Utilize este espaço para suas anotações..."
        )

        # * Page Whatsapp
        self.ui.text_whatsapp_page_help.setVerticalScrollBar(
            self.ui.vsb_whatsapp_page_help
        )
        self.ui.text_whatsapp_page_help.setText(helpText)

    """
        
        :Args:
            
        :Returns:
            
    """

    def user_stack_pages(self, page):

        for each in self.ui.frame_android_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_contact":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_contact)
            self.ui.footer_page_title.setText("Usuário > Informações")
            self.ui.frame_android_contact.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_notations":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_game)
            self.ui.footer_page_title.setText("Usuário > Anotações")
            self.ui.frame_android_game.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_clean":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_clean)
            self.ui.footer_page_title.setText("Usuário > Clean")
            self.ui.frame_android_clean.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_world":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_world)
            self.ui.footer_page_title.setText("Usuário > World")
            self.ui.frame_android_world.setStyleSheet("background:rgb(91,90,90)")


class APFunction:
    def emails_connect(self):
        self.ui.emails_clear_fields_button.setEnabled(False)
        text_id = self.ui.emails_email_input.text()
        text_address = self.ui.emails_password_input.text()
        if text_id == "asd" and text_address == "1234":
            self.ui.emails_password_input.setText("")
            self.ui.emails_email_input.setText("")

        else:
            self.show_error(
                "E-mail ou senha incorreto", "assets/images/error.png", "Ok"
            )

    def emails_clear_fields(self):

        self.ui.emails_password_input.setText("")
        self.ui.emails_email_input.setText("")
