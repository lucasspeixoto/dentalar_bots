# -*- coding: utf-8 -*-
# encoding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
    After in whatsapp web page wait 200s for QR code
    scanned and check for logged search contact field
    With exists, set as logged with not, set as not logged
        
    :Args:
        
    :Returns:
"""


def whatsapp_login(self):

    # Definição de xpath do campo de pesquisa de contatos
    search_xpath = """//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]"""

    try:
        elem = WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located((By.XPATH, search_xpath))
        )
    finally:
        try:
            elem.click()
            self.uniform_wait(2, 3)
            self.is_logged = True
        except UnboundLocalError:
            self.driver.quit()

    return
