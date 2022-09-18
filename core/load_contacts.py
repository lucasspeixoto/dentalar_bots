import pandas as pd

from PySide2.QtWidgets import QFileDialog
from core.helpers.create_box import create_box

from main import *


class Contacts():

    def __init__(self, contacts_list=[]):
        self.contacts_list = contacts_list

    def load_contacts(self):

        file_name: str = QFileDialog.getOpenFileName(
            self, "Carregar Contatos", "", "XLSX(*.xlsx)")

        try:
            file_ok = pd.read_excel(file_name[0])
            self.selected_file_dataframe_content = file_ok.copy()
            self.contacts_list = create_box(file_ok)

        except FileNotFoundError:
            self.errorexec("Nenhum arquivo carregado!",
                           "icons/1x/errorAsset 55.png", "Ok")

            return

        if (len(self.contacts_list) > 0):
            self.ui.contacts_list.clear()

            for contact in self.contacts_list:
                self.ui.contacts_list.addItem(contact)

            self.ui.send_whatsapp_messages_button.setEnabled(True)
            self.ui.send_to_all_contacts_radio_button.setEnabled(True)

        return

    def send_whatsapp_messages(self):
        print([item.text() for item in self.ui.contacts_list.selectedItems()])

    def toggle_all_contacts(self):
        isChecked = self.ui.send_to_all_contacts_radio_button.isChecked()

        for index in range(self.ui.contacts_list.count()):
            if isChecked == False:
                self.ui.contacts_list.item(index).setSelected(False)
            else:
                self.ui.contacts_list.item(index).setSelected(True)
