# -*- coding: utf-8 -*-
# encoding: utf-8

from core.scrapping.get_page import get_page

from core.scrapping.bot_process import BotProcess

from core.scrapping.configuration import Configuration

from core.whatsapp.select_contact_number import select_contact_number

from core.contacts.contacts import *
from core.whatsapp.whatsapp_login import whatsapp_login

from main import *

from interface.error.error import errorUi


class WhatsAppScrapping(BotProcess, Configuration):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

        self.error = errorUi()

    def get_page(self, page_url: str):
        get_page(self, page_url)

    def whatsapp_login(self):
        whatsapp_login(self)

    def select_contact_number(self, contact: str):
        select_contact_number(self, contact)
