# -*- coding: utf-8 -*-
#encoding: utf-8

from main import *

"""
    Clear User interface contacts_list and update
    Contacts text title and toggle all contacts radio
    button text

    :Args:
        
    :Returns:
        
"""


def clear_contacts_list(self):
    self.ui.contacts_list.clear()
    self.ui.whatsapp_page_contacts_frame_text.setText('Contatos')
    self.ui.send_whatsapp_messages_button.setEnabled(False)
    self.ui.clear_contacts_list_button.setEnabled(False)
    self.ui.send_to_all_contacts_checkbox.setText('Nenhum')
    self.ui.send_to_all_contacts_checkbox.setChecked(False)
