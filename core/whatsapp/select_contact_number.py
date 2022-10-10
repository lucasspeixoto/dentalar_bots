# -*- coding: utf-8 -*-
# encoding: utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""
    :Args:
        
    :Returns:
"""


def select_contact_number(self, number: str):

    search_field_xpath: str = self.whatsapp_paths["search_field_xpath"]
    not_found_msg_xpath: str = self.whatsapp_paths["not_found_msg_xpath"]

    # Select the search contact field
    self.click(search_field_xpath, "xpath", 0.2, 0.8)

    # Clean the field if has value
    self.clear_field(search_field_xpath, "xpath", 0.2, 0.8)

    # Type the contact number
    self.click_and_type(search_field_xpath, number, "xpath", 0.1, 0.2)

    # Check if contact was found
    """ try:
        self.click(not_found_msg_xpath, "xpath", 0.2, 0.8)
    except Exception:
        ActionChains(self.driver).send_keys(Keys.ENTER).perform() """

    return
