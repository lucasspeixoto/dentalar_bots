# -*- coding: utf-8 -*-
#encoding: utf-8

import sys


from PySide2.QtCore import (Qt, QThreadPool)
from PySide2.QtWidgets import *
from interface.dialog.dialog import dialogUi
from interface.error.error import errorUi
from workes.worker import Worker

from interface.ui_main import Ui_MainWindow

from ui_function import *

from core.scrapping.bot_process import *
from core.contacts.contacts import *
from core.whatsapp.whatsapp_scrapping import *
from core.files_management.files import *

# CONTAIN STRING VARIABLE CONTAINING THE ABOUT OF EACH PAGE IN THE APPLICATION
from help import *


# OUR APPLICATION MAIN WINDOW :
# -----> MAIN APPLICATION CLASS
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
        # EVENTHOW IT IS AVSENT THIS IS NECESSERY AS THE OPERATING SYSTEM RECOGNISES THE SOFTWARE SUING THIS NAME
        # SO YOU WILL SEE THE NAME ENTERED HERE IN THE TASKBAR, TITLEBAR, E.T.C
        # PASSING THE CODE TO SET THE TITLE TO THE CUSTOME TOPBAR IN OUR UI
        UIFunction.labelTitle(self, application_name)
        # THIS UOFunction CLASS IS IN THE FILE: ui_function.py.
        ###############################

        # -----> INITIAL STACKED WIDGET PAGE WIDGET AND TAB
        # THIS MAKE THE INITIAL WINDOW OF OUR APPLICATION, I.E. THE FIRST PAGE OR THE WELCOME PAGE/SCREEN            ---------(C5)
        # IN OUR APPLICATION THIS IS THE MENU BAR, TOODLE SWITCH, MIN, MAX, CLOSE BUTTONS, AND THE HOME PAGE.
        # ALL THIS GET INITIALISED HERE.
        # SINCE ALL THE FUNCTION RELATED STUFF IS DONE IN THE ui_function.py FILE, IT GOES THERE
        # REMEMBER THIS FUNCTION CAN ALSO BE DONE HERE, BUT DUE TO CONVINENCE IT IS SHIFTD TO A NEW FILE.
        UIFunction.initStackTab(self)
        ############################################################

        # ----> CERTAIN TOOLS LIKE DRAG, MAXIMISE, MINIMISE, CLOSE AND HIDING OF THE WINDOWS TOPBAR
        # THIS WINDOW INITIALISES THE BUTTONS NECESSERY FOR THE MAINWINDOW LIKE: CLOSE, MIN, MAX E.T.C.                ---------(C6)
        UIFunction.constantFunction(self)
        #############################################################

        # ----> TOODLE THE MENU HERE
        # THIS CODE DETETS THE BUTTON IN THE RIGHT TOP IS PRESSED OR NOT AND IF PRESSED IT CONNECT  TO A FUNCTION IN THE ui_function.py                 ---------(C7)
        # FILE, WHICH EXPANDS THE MENU BAR TO DOUBLE ITS WIDTH MAKING ROOM FOR THE ABOUT PAGES.
        # THIS EFFECT CALLED AS TOODLE, CAN BE MADE USE IN MANY WAYS. CHECK THE FUNCTION: toodleMenu: IN THE ui_function.py
        # FILE FOR THE CLEAR WORKING
        self.ui.toodle.clicked.connect(
            lambda: UIFunction.toodleMenu(self, 160, True))
        #############################################################

        # ----> MENU BUTTON PRESSED EVENTS
        # NOW SINCE OUR DEMO APPLICATION HAS ONLY 4 MENU BUTTONS: Home, Bug, Android, Cloud, WHEN USER PRESSES IT THE FOLLOWING CODE             ---------(C8)
        # REDIRECTS IT TO THE ui_function.py FILE buttonPressed() FUNCTION TO MAKE THE NECESSERY RESPONSES TO THE BUTTON PRESSED.
        # IT TAKES SELF AND THE BUTTON NAME AS THE RGUMENT, THIS IS ONLY TO RECOGNISE WHICH BUTTON IS PRESSED BY THE buttonPressed() FUNCTION.
        self.ui.bn_whatsapp.clicked.connect(
            lambda: UIFunction.buttonPressed(self, 'bn_whatsapp'))
        self.ui.bn_bug.clicked.connect(
            lambda: UIFunction.buttonPressed(self, 'bn_bug'))
        self.ui.bn_android.clicked.connect(
            lambda: UIFunction.buttonPressed(self, 'bn_android'))
        self.ui.bn_cloud.clicked.connect(
            lambda: UIFunction.buttonPressed(self, 'bn_cloud'))
        #############################################################

        # -----> STACK PAGE FUNCTION
        # OUR APPLICATION CHANGES THE PAGES BY USING THE STACKED WIDGET, THIS CODE POINTS TO A FUNCTION IN ui_function.py FILE             ---------(C9)
        # WHICH GOES AND SETS THE DEFAULT IN THESE PAGES AND SEARCHES FOR THE RESPONSES MADE BY THE USER IN THE CORRSPONDING PAGES.
        UIFunction.stackPage(self)
        #############################################################

        # ----> EXECUTING THE ERROR AND DIALOG BOX MENU : THIS HELP TO CALL THEM WITH THE FUNCTIONS.
        # THIS CODE INITIALISED THE DIALOGBOX AND THE ERRORBOX, MAKES AN OBJECT OF THE CORRESPONDING CLASS, SO THAT WE CAN CALL THEM         ---------(C10)
        # WHENEVER NECESSERY.
        self.diag = dialogUi()
        self.error = errorUi()
        #############################################################

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())

        # --PAGE WhatsApp---------------------------------:

        # - WhatsApp Login
        self.ui.whatsapp_login_button.clicked.connect(
            lambda: self.whatsapp_login())

        # --Set Default image path ----------------------:
        #self.contacts.selected_image = ''

        # --Load Contacts----------------------:
        self.ui.load_contacts_button.clicked.connect(
            lambda: Contacts.get_contacts_from_excel_file(self))

        # -- Check Load All Contacts Button
        self.ui.send_to_all_contacts_checkbox.toggled.connect(
            lambda: Contacts.toggle_all_contacts(self))

        # -- Clear All Contacts in the list Button
        self.ui.clear_contacts_list_button.clicked.connect(
            lambda: Contacts.clear_contacts_list(self))

        # -- Send messages
        self.ui.send_whatsapp_messages_button.clicked.connect(
            lambda: self.send_whatsapp_messages())

        # -- Load Image
        self.ui.load_image_button.clicked.connect(
            lambda: Files.load_image(self))

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

    """
    TODO Call whatsapp_login method from
    WhatsAppScrapping class
    :Args:    
    :Returns:
    """

    

    def whatsapp_login(self):
        def whatsapp_login_pointer():
            WhatsAppScrapping.whatsapp_login(self)
       
        worker = Worker(whatsapp_login_pointer)

        self.threadpool.start(worker)

    def send_whatsapp_messages(self):
        def send_whatsapp_messages_pointer():
            Contacts.send_whatsapp_messages(self)

        worker = Worker(send_whatsapp_messages_pointer)
        
        self.threadpool.start(worker)

    # ----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE: NECESSERY FOR THE moveWindow FUNCTION
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #############################################################

    # -----> FUNCTION WHICH OPENS THE DIALOG AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION dialogexec() WITH ALL THE PARAMETER
    # NOW WHENEVER YOU WANT A DIALOG BOX TO APPEAR IN THE APP LIKE IN PRESS OF CLODE BUTTON, THIS CAN BE DONE BY CALLING THIS FUNCTION.        ----------(C11)
    # IT TAKES DIALOG OBJECT(INITIALISED EARLIER), HEADER NAME OF DIALOG BOX, MESSAGE TO BE DISPLAYED, ICON, BUTTON NAMES.
    # THIS CODE EXECUTES THE DIALOGBOX AND SO WE CAN SEE THE DIALOG BOX IN THE SCREEN.
    # DURING THE APPEARENCE OF THIS WINDOW, YOU CANNOT USE THE MAINWINDOW, YOU SHPULD EITHER PRESS ANY ONE OFT HE PROVIDED BUTTONS
    # OR JUST CLODE THE DIALOG BOX.
    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()
    #############################################################

    # -----> FUNCTION WHICH OPENS THE ERROR BOX AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION errorexec() WITH ALL THE PARAMETER
    # SAME AS COMMEND (C11), EXCEPT THIS IS FOR THE ERROR BOX.

    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()
    ##############################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
