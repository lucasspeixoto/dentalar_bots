# -*- coding: utf-8 -*-
# encoding: utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

"""
    :Args:
        
    :Returns:
"""


def check_contact(self) -> bool:

    not_found_msg_xpath: str = self.whatsapp_paths["not_found_msg_xpath"]

    contact_exists = self.check_if_exists(not_found_msg_xpath, "xpath", 0.2, 0.8)

    if contact_exists:
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    return contact_exists
