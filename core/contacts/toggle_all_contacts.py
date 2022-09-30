# -*- coding: utf-8 -*-
#encoding: utf-8

from main import *

"""
    Select and unselect all contacts in the list

    :Args:
    
    :Returns:
       
"""


def toggle_all_contacts(self):

    isChecked = self.ui.send_to_all_contacts_checkbox.isChecked()

    for index in range(self.ui.contacts_list.count()):
        if isChecked == False:
            self.ui.contacts_list.item(index).setSelected(False)
            self.ui.send_to_all_contacts_checkbox.setText('Nenhum')
        else:
            self.ui.contacts_list.item(index).setSelected(True)
            self.ui.send_to_all_contacts_checkbox.setText('Todos')

    return
