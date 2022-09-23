# -*- coding: utf-8 -*-
#encoding: utf-8

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

"""
    TODO: Search for a contact on whatsapp page
    by the number and check if this contact exists
     
"""   
def select_contact(self, contact: str):
        
    search_field_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    
    # Selecionar Campo de pesquisa de contato
    self.click(search_field_xpath, 'xpath',  0.2, 0.8)
    

    # Limpar campo
    self.clear_field(search_field_xpath, 'xpath',  0.2, 0.8)
    
    
    # Digitar número
    self.click_and_type(search_field_xpath, contact, 'xpath', 0.2, 0.4)
    
    return
