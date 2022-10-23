# -*- coding: utf-8 -*-
# encoding: utf-8

import pandas as pd

from core.contacts.helpers.build_contacts_list import build_contacts_list
from main import *

"""
    :Args:
        
    :Returns:
"""


def get_contacts_from_excel_file(self):
    file_name: str = QFileDialog.getOpenFileName(
        self, "Carregar Contatos", "", "XLSX(*.xlsx)"
    )

    try:
        table = pd.read_excel(file_name[0])
        self.selected_file_dataframe_content = table.copy()
        self.contacts_list = build_contacts_list(table)

    except FileNotFoundError:
        self.ui.contacts_list.clear()
        self.ui.whatsapp_page_contacts_frame_text.setText("Contatos")
        self.show_error("Nenhum arquivo carregado!", "assets/images/error.png", "Ok")

        return

    selected_contacts = len(self.contacts_list)

    if selected_contacts > 0:
        self.ui.whatsapp_page_contacts_frame_text.setText(
            "Contatos - {}".format(selected_contacts)
        )
        self.ui.contacts_list.clear()

        for contact in self.contacts_list:
            self.ui.contacts_list.addItem(contact)

        self.ui.send_to_all_contacts_checkbox.setEnabled(True)
        self.ui.clear_contacts_list_button.setEnabled(True)

    else:
        self.ui.validate_whatsapp_sending_button.setEnabled(False)

    return
