# -*- coding: utf-8 -*-
# encoding: utf-8

from core.scrapping.get_page import get_page

from core.scrapping.bot_process import BotProcess

from core.scrapping.configuration import Configuration
from core.whatsapp.check_contact import check_contact
from core.whatsapp.insert_message_image import insert_message_image

from core.whatsapp.select_contact_number import select_contact_number

from core.contacts.contacts import *

from core.whatsapp.whatsapp_login import whatsapp_login

from core.files_management.files import Files

from interface.error.error import ErrorUi


class WhatsAppScrapping(BotProcess, Configuration, Files):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

        self.error = ErrorUi()

    def get_page(self, page_url: str):
        get_page(self, page_url)

    def whatsapp_login(self):
        whatsapp_login(self)

    def select_contact_number(self, contact: str):
        select_contact_number(self, contact)

    def check_contact(self):
        return check_contact(self)

    def insert_message_image(self, image_path: str, message: str):
        insert_message_image(self, image_path, message)
