# -*- coding: utf-8 -*-
# encoding: utf-8

import sys

from PySide2.QtCore import Qt, QThreadPool
from PySide2.QtWidgets import *

from core.validations.validations import *
from interface.dialog.dialog import DialogUi
from interface.error.error import ErrorUi
from workes.worker import Worker

from ui_main import Ui_MainWindow

from ui_function import *

from core.scrapping.bot_process import *
from core.contacts.contacts import *
from core.whatsapp.whatsapp_scrapping import *
from core.files_management.files import *

from help import *


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.contacts = Contacts()

        self.files = Files()

        self.configuration = Configuration()

        self.bot = BotProcess()

        self.whatsapp_scrapping = WhatsAppScrapping()

        application_name = "Automações"
        self.setWindowTitle(application_name)

        UIFunction.label_title(self, application_name)

        UIFunction.init_stack_tab(self)

        UIFunction.constant_function(self)

        self.ui.toodle.clicked.connect(lambda: UIFunction.toodle_menu(self, 160, True))

        self.ui.menu_whatsapp_button.clicked.connect(
            lambda: UIFunction.change_user_page(self, "menu_whatsapp_button")
        )
        self.ui.menu_email_button.clicked.connect(
            lambda: UIFunction.change_user_page(self, "menu_email_button")
        )

        self.ui.menu_user_button.clicked.connect(
            lambda: UIFunction.change_user_page(self, "menu_user_button")
        )
        self.ui.menu_connection_button.clicked.connect(
            lambda: UIFunction.change_user_page(self, "menu_connection_button")
        )

        UIFunction.stack_page(self)

        self.dialog = DialogUi()

        self.error = ErrorUi()

        self.thread_pool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.thread_pool.maxThreadCount()
        )

        self.ui.load_contacts_button.clicked.connect(
            lambda: Contacts.get_contacts_from_excel_file(self)
        )

        self.ui.send_to_all_contacts_checkbox.toggled.connect(
            lambda: Contacts.toggle_all_contacts(self)
        )

        self.ui.clear_contacts_list_button.clicked.connect(
            lambda: Contacts.clear_contacts_list(self)
        )

        self.ui.validate_whatsapp_sending_button.clicked.connect(
            lambda: Validations.validate_whatsapp_needed_data(self)
        )

        self.ui.reset_validations_whatsapp_sending_button.clicked.connect(
            lambda: Validations.reset_validate_whatsapp_needed_data(self)
        )

        self.ui.send_whatsapp_messages_button.clicked.connect(
            lambda: self.send_whatsapp_messages()
        )

        self.ui.load_image_button.clicked.connect(lambda: Files.load_image(self))

        self.dragPos = self.pos()

        def move_window(event):
            if UIFunction.return_status() == 1:
                UIFunction.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        """ 
        Widget to move: we choose the topmost frame where
        the application name is present as the area to move
        the window. calling the function to change the
        position of the window during mouse drag
        """
        self.ui.frame_appname.mouseMoveEvent = move_window

    def send_whatsapp_messages_pointer(self):
        Contacts.send_whatsapp_messages(self)

        return

    def send_whatsapp_messages(self):
        worker = Worker(self.send_whatsapp_messages_pointer)

        self.thread_pool.start(worker)

        return

    """
    function to capture the initial position of the mouse: necessary for the move window function
    """

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    """ Function which opens the dialog and displays it: so to call dialog box just call
    the function show_dialog() with all the parameter now whenever you want a dialog box
    to appear in the app like in press of clode button, this can be done by calling this function. 
    it takes dialog object(initialised earlier), header name of dialog box, message to be displayed,
    icon, button names. This code executes the dialogbox and so we can see the dialog box in the screen.
    during the appearence of this window, you cannot use the mainwindow, you shpuld either press
    any one oft he provided buttons  or just clode the dialog box.
    """

    def show_dialog(
        self,
        heading: str,
        message: str,
        icon: str,
        button_cancel_text: str,
        button_ok_text: str,
    ):
        DialogUi.dialog_construct(
            self.dialog, heading, message, icon, button_cancel_text, button_ok_text
        )
        self.dialog.exec_()

    """
    Function which opens the error box and displays it: so to call dialog box just call
    the function show_error() with all the parameter same as commend (c11),
    except this is for the error box. 
    """

    def show_error(self, heading: str, icon: str, button_ok_text: str) -> None:
        ErrorUi.error_construct(self.error, heading, icon, button_ok_text)
        self.error.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
