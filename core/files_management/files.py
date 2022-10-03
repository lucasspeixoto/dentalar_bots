# -*- coding: utf-8 -*-
#encoding: utf-8

from PySide2.QtWidgets import QFileDialog

from interface.error.error import errorUi

from main import *


class Files():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self.error = errorUi()
        
        self.whatsapp_paths = {}
        
        self.set_default_image_and_file()
        
        self.load_paths()
        
    
    def load_paths(self):
        try:
            with open('paths.txt') as file:
                
                self.whatsapp_paths = {path.split(":")[0]: path.split(":")[
                    1] for path in file.readlines()}
        except FileNotFoundError:
            
            self.errorexec("O arquivo 'paths.txt' foi removido ou renomeado, inclua novamente para iniciar!",
                           "icons/1x/errorAsset 55.png", "Ok")
    
        return

    def set_default_image_and_file(self):
        self.selected_image = ''
        self.selected_file = ''
        
        return

    def load_image(self):

        image_path: str = QFileDialog.getOpenFileName(
            self, "Carregar Imagem", "", "Arquivo de imagem (*.png *.jpg)")

        selected_image = image_path[0]

        if (selected_image != ''):
            self.files.selected_image = image_path[0]
            self.ui.selected_whatsapp_image_path_text.setText(
                "Imagem: " + self.files.selected_image)
            self.ui.selected_whatsapp_image_path_text.setWordWrap(True)
        else:
            self.errorexec("Nenhuma imagem selecionada!",
                           "icons/1x/errorAsset 55.png", "Ok")
            self.files.selected_image = ''
            self.ui.selected_whatsapp_image_path_text.setText(
                self.files.selected_image)
            
        return

    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstruct(self.error, heading, icon, btnOk)
        self.error.exec_()
        
        return
