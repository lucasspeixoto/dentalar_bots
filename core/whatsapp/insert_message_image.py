# -*- coding: utf-8 -*-
# encoding: utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""
    :Args:
        
    :Returns:
"""


def insert_message_image(self, image_path: str, message: str):

    clip_button_xpath: str = self.whatsapp_paths["clip_button_xpath"]
    insert_media_button_xpath: str = self.whatsapp_paths["insert_media_button_xpath"]
    insert_image_message_field_xpath: str = self.whatsapp_paths[
        "insert_image_message_field_xpath"
    ]
    
    # Enter in contact page
    ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    # Click in the clip button
    self.click(clip_button_xpath, "xpath", 0.2, 0.8)

    # Insert the image
    self.send_keys(insert_media_button_xpath, image_path, "xpath", 1, 2)

    # Insert the text
    self.send_keys(insert_image_message_field_xpath, message, "xpath", 0.2, 0.8)

    # Click 'Enter'
    ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    return
