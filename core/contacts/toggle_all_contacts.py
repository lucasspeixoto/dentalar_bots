# -*- coding: utf-8 -*-
# encoding: utf-8


"""
    Select and unselect all contacts in the list

    :Args:
    
    :Returns:
       
"""


def toggle_all_contacts(self):
    is_checked: bool = self.ui.send_to_all_contacts_checkbox.isChecked()

    for index in range(self.ui.contacts_list.count()):
        if not is_checked:
            self.ui.contacts_list.item(index).setSelected(False)
            self.ui.send_to_all_contacts_checkbox.setText("Nenhum")
        else:
            self.ui.contacts_list.item(index).setSelected(True)
            self.ui.send_to_all_contacts_checkbox.setText("Todos")

    return


def clear_selected_contacts(self):
    for index in range(self.ui.contacts_list.count()):
        self.ui.contacts_list.item(index).setSelected(False)
        self.ui.send_to_all_contacts_checkbox.setText("Nenhum")

        self.ui.send_to_all_contacts_checkbox.setChecked(False)

    return
