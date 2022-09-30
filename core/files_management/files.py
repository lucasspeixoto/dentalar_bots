# -*- coding: utf-8 -*-
#encoding: utf-8

from PySide2.QtWidgets import QFileDialog

from main import *

class Files():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
                
        
    def set_default_image_and_file(self):
        self.selected_image = ''
        self.selected_file = ''
        
    def load_image(self):
               
        
        image_path: str = QFileDialog.getOpenFileName(
            self, "Carregar Imagem", "", "Arquivo de imagem (*.png *.jpg)")

        selected_image = image_path[0]

        if (selected_image != ''):
            self.files.selected_image = image_path[0]
            self.ui.selected_whatsapp_image_path_text.setText("Imagem: " + self.files.selected_image)
            self.ui.selected_whatsapp_image_path_text.setWordWrap(True)
        else:
            self.errorexec("Nenhuma imagem selecionada!",
                           "icons/1x/errorAsset 55.png", "Ok")
            self.files.selected_image = ''
            self.ui.selected_whatsapp_image_path_text.setText(self.files.selected_image)

        return
