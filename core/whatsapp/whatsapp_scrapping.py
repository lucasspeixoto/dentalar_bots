# -*- coding: utf-8 -*-
#encoding: utf-8

from PySide2.QtCore import QObject, QThread, Signal

from core.scrapping.get_page import get_page

from core.scrapping.bot_process import BotProcess

from core.scrapping.configuration import Configuration

from core.whatsapp.select_contact import select_contact

from core.whatsapp.whatsapp_login import whatsapp_login

from core.contacts.contacts import *

from time import sleep

from main import *


class WhatsAppScrapping(QObject, Configuration, BotProcess):

    def __init__(self, *args, **kwargs):
        super(WhatsAppScrapping, self).__init__(*args, **kwargs)

    def get_page(self, page_url: str):
        for i in range(10):
            sleep(1)
            print(i)

        return

    def whatsapp_login(self): whatsapp_login(self)

    def select_contact(self, contact: str): select_contact(self, contact)
