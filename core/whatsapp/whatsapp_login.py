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

from main import *

"""
    TODO: After in whatsapp web page,
     
    
    :Args:
        - selected_file_dataframe_content - Pandas Dataframe
          with two columns (name and number) 
          
    :Returns:
        - List of transformed contact detail ['name - number']
"""


def whatsapp_login(self):
    # Aguardar por 200s até o QR Code ser Scaneado
    search_xpath = '''//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'''

    try:
        elem = WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located((By.XPATH, search_xpath))
        )
    finally:
        try:
            elem.click()
            self.uniform_wait(2, 3)
        except UnboundLocalError:
            self.driver.quit()
            self.errorexec("Tempo expirado, logar novamente!",
                           "icons/1x/errorAsset 55.png", "Ok")
        
    return
