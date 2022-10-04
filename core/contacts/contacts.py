# -*- coding: utf-8 -*-
# encoding: utf-8

from core.files_management.files import *

from core.contacts.get_contacts_from_excel_file import get_contacts_from_excel_file

from core.contacts.toggle_all_contacts import toggle_all_contacts

from core.contacts.clear_contacts_list import clear_contacts_list

from core.whatsapp.whatsapp_scrapping import *


class Contacts(Files):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args = args
        self.kwargs = kwargs

        self.ui = None
        self.whatsapp_scrapping = None

        self.contacts_list = []
        self.selected_contacts = []

        self.error = errorUi()

    def get_contacts_from_excel_file(self):
        get_contacts_from_excel_file(self)

    def toggle_all_contacts(self):
        toggle_all_contacts(self)

    def clear_contacts_list(self):
        clear_contacts_list(self)

    """
            
    :Args:
        
    :Returns:
    """

    def send_whatsapp_messages(self):

        contacts: list = self.ui.contacts_list.selectedItems()

        self.whatsapp_scrapping.start_driver()

        self.whatsapp_scrapping.get_page("https://web.whatsapp.com/")

        self.whatsapp_scrapping.whatsapp_login()

        for contact in contacts:
            number: str = contact.text().split(" - ")[-1]

            self.whatsapp_scrapping.select_contact_number(number)

        return
