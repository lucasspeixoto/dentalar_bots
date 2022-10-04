# -*- coding: utf-8 -*-
# encoding: utf-8


"""
    :Args:
        
    :Returns:
"""


def select_contact_number(self, contact: str):

    search_field_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'

    # Select the search contact field
    self.click(search_field_xpath, "xpath", 0.2, 0.8)

    # Clean the field if has value
    self.clear_field(search_field_xpath, "xpath", 0.2, 0.8)

    # Type the contact number
    self.click_and_type(search_field_xpath, contact, "xpath", 0.2, 0.4)

    return
