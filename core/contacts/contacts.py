# -*- coding: utf-8 -*-
# encoding: utf-8

from core.files_management.files import *

from core.contacts.get_contacts_from_excel_file import get_contacts_from_excel_file

from core.contacts.toggle_all_contacts import toggle_all_contacts

from core.contacts.clear_contacts_list import clear_contacts_list

from core.whatsapp.whatsapp_scrapping import *


class Contacts:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args = args
        self.kwargs = kwargs

        self.contacts_list = []
        self.selected_contacts = []

        self.error = ErrorUi()

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
        image_path: str = self.files.selected_image
        paragraphs: str = self.ui.whatsapp_message_input.toPlainText().split("\n\n")

        self.whatsapp_scrapping.start_driver()

        self.whatsapp_scrapping.get_page("https://web.whatsapp.com/")

        self.whatsapp_scrapping.whatsapp_login()

        for contact in contacts:

            number = contact.text().split(" - ")[-1]

            self.whatsapp_scrapping.select_contact_number(number)

            contact_exists: bool = self.whatsapp_scrapping.check_contact()

            print(f"{number} - {contact_exists}")

            if contact_exists == True:
                self.whatsapp_scrapping.insert_message_image(image_path, paragraphs)

        self.whatsapp_scrapping.quit_driver()

        # self.show_error("Processo Encerrado!", "assets/images/error.png", "Ok")

        return
    
    
