# -*- coding: utf-8 -*-
# encoding: utf-8


from core.files_management.files import *


from core.contacts.get_contacts_from_excel_file import get_contacts_from_excel_file

from main import *

from PySide2.QtCore import QObject

from core.whatsapp.whatsapp_scrapping import *


class Contacts():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self.contacts_list = []
        self.selected_contacts = []

    def get_contacts_from_excel_file(self): get_contacts_from_excel_file(self)

    def toggle_all_contacts(self):
        
        print(self.files.test)
        isChecked = self.ui.send_to_all_contacts_checkbox.isChecked()

        for index in range(self.ui.contacts_list.count()):
            if isChecked == False:
                self.ui.contacts_list.item(index).setSelected(False)
                self.ui.send_to_all_contacts_checkbox.setText('Nenhum')
            else:
                self.ui.contacts_list.item(index).setSelected(True)
                self.ui.send_to_all_contacts_checkbox.setText('Todos')

    def clear_contacts_list(self):
        self.ui.contacts_list.clear()
        self.ui.whatsapp_page_right_side_title.setText('Contatos')
        self.ui.send_whatsapp_messages_button.setEnabled(False)
        self.ui.clear_contacts_list_button.setEnabled(False)
        self.ui.send_to_all_contacts_checkbox.setText('Nenhum')
        self.ui.send_to_all_contacts_checkbox.setChecked(False)

    def send_whatsapp_messages(self):
        """ if (len(self.ui.contacts_list.selectedItems()) == 0):
            self.errorexec("Selecione ao menos um contato para envio desta mensagem!",
                           "icons/1x/errorAsset 55.png", "Ok")

            return """

        """ print([item.text() for item in self.ui.contacts_list.selectedItems()])
            print(self.selected_image)
            print(self.ui.whatsapp_message_input.toPlainText())
        """
        self.whatsapp_scrapping.start_driver()

        self.whatsapp_scrapping.get_page('https://web.whatsapp.com/')

        self.whatsapp_scrapping.whatsapp_login()

        self.whatsapp_scrapping.select_contact_number(
            self.ui.whatsapp_message_input.toPlainText())

        return
