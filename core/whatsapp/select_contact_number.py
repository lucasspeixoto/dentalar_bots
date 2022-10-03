# -*- coding: utf-8 -*-
# encoding: utf-8


"""
    :Args:
        
    :Returns:
"""


def select_contact_number(self, contact: str):

    search_field_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'

    # Selecionar Campo de pesquisa de contato
    self.click(search_field_xpath, "xpath", 0.2, 0.8)

    # Limpar campo
    self.clear_field(search_field_xpath, "xpath", 0.2, 0.8)

    # Digitar número
    self.click_and_type(search_field_xpath, contact, "xpath", 0.2, 0.4)

    return
