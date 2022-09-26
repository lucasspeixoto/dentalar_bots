# -*- coding: utf-8 -*-
#encoding: utf-8

from PySide2.QtWidgets import QFileDialog

from main import *

class Files():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
                
        self.selected_image = ''
        self.selected_file = ''
        
        self.test = 'TESTTTTT'

    def load_image(self):
               
        
        image_path: str = QFileDialog.getOpenFileName(
            self, "Carregar Imagem", "", "Arquivo de imagem (*.png *.jpg)")

        selected_image = image_path[0]

        if (selected_image != ''):
            self.selected_image = image_path[0]

        else:
            self.errorexec("Nenhuma imagem selecionada!",
                           "icons/1x/errorAsset 55.png", "Ok")

        return
