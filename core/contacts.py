# -*- coding: utf-8 -*-
#encoding: utf-8

import pandas as pd

from PySide2.QtWidgets import QFileDialog
from core.helpers.create_box import create_box

from core.files import *

from main import *


class Contacts(Files):

    def __init__(self, *args, **kwargs):
        super(Contacts, self).__init__(*args, **kwargs)
        
        self.contacts_list = []
        self.selected_contacts = []
        
    def load_contacts(self):

        file_name: str = QFileDialog.getOpenFileName(
            self, "Carregar Contatos", "", "XLSX(*.xlsx)")

        try:
            file_ok = pd.read_excel(file_name[0])
            self.selected_file_dataframe_content = file_ok.copy()
            self.contacts_list = create_box(file_ok)

        except FileNotFoundError:
            self.errorexec("Nenhum arquivo carregado!",
                           "icons/1x/errorAsset 55.png", "Ok")

            return

        selected_contacts = len(self.contacts_list)
        
        if (selected_contacts > 0):
            self.ui.whatsapp_page_right_side_title.setText('Contatos - {}'.format(selected_contacts))
            self.ui.contacts_list.clear()

            for contact in self.contacts_list:
                self.ui.contacts_list.addItem(contact)

            self.ui.send_whatsapp_messages_button.setEnabled(True)
            self.ui.send_to_all_contacts_checkbox.setEnabled(True)
            self.ui.clear_contacts_list_button.setEnabled(True)

        return

    def toggle_all_contacts(self):
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
        """ print([item.text() for item in self.ui.contacts_list.selectedItems()])
        print(self.selected_image)
        print(self.ui.whatsapp_message_input.toPlainText()) """
        self.whatsapp_scrapping.start_driver()
        self.whatsapp_scrapping.get_page('https://www.google.com')
