# -*- coding: utf-8 -*-
#encoding: utf-8

from core.scrapping.get_page import get_page

from core.bot_process import BotProcess
from core.configuration import Configuration


class WhatsAppScrapping(Configuration, BotProcess):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_page(self, page_url: str): get_page(self, page_url)
