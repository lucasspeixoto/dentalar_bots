# -*- coding: utf-8 -*-
# encoding: utf-8

import os
import sys

import rootpath


class Configuration:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

        # Plataforma
        self.platform = sys.platform

        # Diretório Raiz
        self.root = ""

        # Definição do diretório raiz com base no sistema operacional
        self.check_system(self.platform)

        # Caminho Downloads
        self.downloaded_path = self.root + "\\src\\assets\\files\\"

        # Caminho dos arquivos cvs renomeados e do excel
        self.files_path = self.root + "\\src\\assets\\cvs"

        self.current_folder = os.path.dirname(os.path.abspath(__file__)) + "/"
        self.path = "/".join(self.current_folder.split("\\")[0:-2]) + "/"

    """
        :Args:
            
        :Returns:
    """

    def check_system(self, platform: str):
        # Verificação do sistema operacional
        if platform in ["linux", "linux2"]:
            try:
                self.root = os.path.dirname(self.base_path)
            except AttributeError:
                pass
        elif platform == "win32":
            try:
                self.root = rootpath.detect()
            except AttributeError:
                pass
        else:
            pass

        print(f"Platform: {platform}")

        return
