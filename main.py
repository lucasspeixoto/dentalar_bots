# -*- coding: utf-8 -*-
# encoding: utf-8

from PySide2.QtCore import Qt, QThreadPool
from PySide2.QtWidgets import *

import sys

from ui_main import Ui_MainWindow

from interface.dialog.dialog import dialogUi
from interface.error.error import errorUi


from ui_function import *

from core.scrapping.bot_process import *
from core.contacts.contacts import *
from core.whatsapp.whatsapp_scrapping import *
from core.files_management.files import *
from core.validations.validations import *

from help import *
from workes.worker import Worker


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

        UIFunction.labelTitle(self, application_name)

        UIFunction.initStackTab(self)

        UIFunction.constantFunction(self)

        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))

        self.ui.bn_whatsapp.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_whatsapp")
        )
        self.ui.bn_bug.clicked.connect(lambda: UIFunction.buttonPressed(self, "bn_bug"))

        self.ui.bn_android.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_android")
        )
        self.ui.bn_cloud.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_cloud")
        )

        UIFunction.stackPage(self)

        self.diag = dialogUi()

        self.error = errorUi()

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
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

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE: WE CHOOSE THE TOPMOST FRAME WHERE THE APPLICATION NAME IS PRESENT AS THE AREA TO MOVE THE WINDOW.
        # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE WINDOW DURING MOUSE DRAG
        self.ui.frame_appname.mouseMoveEvent = moveWindow

    def send_whatsapp_messages_pointer(self):
        Contacts.send_whatsapp_messages(self)

        return

    def send_whatsapp_messages(self):

        worker = Worker(self.send_whatsapp_messages_pointer)

        self.threadpool.start(worker)

        return

    """
    FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE: NECESSERY FOR THE
    moveWindow FUNCTION
    """

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    """ FUNCTION WHICH OPENS THE DIALOG AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION dialogexec() WITH ALL THE PARAMETER
     NOW WHENEVER YOU WANT A DIALOG BOX TO APPEAR IN THE APP LIKE IN PRESS OF CLODE BUTTON, THIS CAN BE DONE BY CALLING THIS FUNCTION.        ----------(C11)
     IT TAKES DIALOG OBJECT(INITIALISED EARLIER), HEADER NAME OF DIALOG BOX, MESSAGE TO BE DISPLAYED, ICON, BUTTON NAMES.
     THIS CODE EXECUTES THE DIALOGBOX AND SO WE CAN SEE THE DIALOG BOX IN THE SCREEN.
     DURING THE APPEARENCE OF THIS WINDOW, YOU CANNOT USE THE MAINWINDOW, YOU SHPULD EITHER PRESS ANY ONE OFT HE PROVIDED BUTTONS
     OR JUST CLODE THE DIALOG BOX.
     """

    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()

    """ FUNCTION WHICH OPENS THE ERROR BOX AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION errorexec() WITH ALL THE PARAMETER
    SAME AS COMMEND (C11), EXCEPT THIS IS FOR THE ERROR BOX. """

    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstruct(self.error, heading, icon, btnOk)
        self.error.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
