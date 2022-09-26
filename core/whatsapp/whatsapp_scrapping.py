# -*- coding: utf-8 -*-
#encoding: utf-8

import sys

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from core.scrapping.get_page import get_page

from core.scrapping.bot_process import BotProcess

from core.scrapping.configuration import Configuration

from core.whatsapp.select_contact_number import select_contact_number

from core.contacts.contacts import *

from main import *

from interface.error.error import errorUi

class WhatsAppScrapping(BotProcess, Configuration):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.error = errorUi()
         
    def get_page(self, page_url: str): get_page(self, page_url)

    def whatsapp_login(self):
        
        sys.settrace
                
        search_xpath = '''//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'''

        try:
            elem = WebDriverWait(self.driver, 200).until(
                EC.presence_of_element_located((By.XPATH, search_xpath))
            )
            print('Online!')
        finally:
            try:
                elem.click()
                self.uniform_wait(2, 3)
            except Exception:
                self.driver.quit()
                self.errorexec(f"Tempo expirado, logar novamente!",
                            "icons/1x/errorAsset 55.png", "Ok")

        return

    def select_contact_number(
        self, contact: str): select_contact_number(self, contact)
    
    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()
    
    