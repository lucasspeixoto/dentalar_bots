# -*- coding: utf-8 -*-
# encoding: utf-8

from core.files_management.files import *

from core.contacts.get_contacts_from_excel_file import get_contacts_from_excel_file

from core.contacts.toggle_all_contacts import toggle_all_contacts

from core.contacts.clear_contacts_list import clear_contacts_list

from main import *

from interface.error.error import errorUi
from core.whatsapp.whatsapp_scrapping import *


class Contacts():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self.contacts_list = []
        self.selected_contacts = []

        self.error = errorUi()

    def get_contacts_from_excel_file(self): get_contacts_from_excel_file(self)

    def toggle_all_contacts(self): toggle_all_contacts(self)

    def clear_contacts_list(self): clear_contacts_list(self)

    def send_whatsapp_messages(self):

        message: str = self.ui.whatsapp_message_input.toPlainText()
        selected_image: str = self.files.selected_image
        contacts: list = self.ui.contacts_list.selectedItems()
        
         # * Tratamento de erros (Sem contatos, sem imagem ou sem mensagem)
        has_error = len(contacts) == 0 or selected_image == '' or message == ''
   
        if (has_error == True):
            self.errorexec("Informaçãoes faltando. Seleciona ao menos um contato, a imagem e insira o texto para enviar!",
                           "icons/1x/errorAsset 55.png", "Ok")
            return
        
        else:
            """ self.whatsapp_scrapping.start_driver()

            self.whatsapp_scrapping.get_page('https://web.whatsapp.com/')

            self.whatsapp_scrapping.whatsapp_login()

            for contact in contacts:
                number: str = contact.text().split(' - ')[-1]

                self.whatsapp_scrapping.select_contact_number(number) """

            return

    """ def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_() """
