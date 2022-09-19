# -*- coding: utf-8 -*-
#encoding: utf-8


import random
from random import uniform
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


class BotProcess:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    '''
    # TODO: Configurar
    # Configura o driver
    '''

    def config_bot(self):
        self.find_options = {
            'class': By.CLASS_NAME,
            'xpath': By.XPATH,
            'id': By.ID,
            'tag': By.TAG_NAME
        }

        # Configuração
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-infobars')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--disable-extensions')

        # Disable the banner "Chrome is being controlled by automated test software"
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option(
            "excludeSwitches", ['enable-automation'])

        # Configurações do Navegador
        self.prefs = {
            "safebrowsing.enabled": False,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "profile.default_content_setting_values.automatic_downloads": 1
        }

        self.options.add_experimental_option('prefs', self.prefs)
        self.capabilities = DesiredCapabilities().CHROME
        self.capabilities.update(self.options.to_capabilities())

        return

    '''
    # TODO: Configurar e iniciar uma instância de driver
    # Chama a configuração do selenium e inicia um driver
    '''

    def start_driver(self):
        self.config_bot()
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self.options,
            desired_capabilities=self.capabilities
        )
        
        self.driver.get('https://www.youtube.com')

        return

    '''
    # TODO: Finalizar uma sessão de driver.
    '''

    def quit_driver(self):
        self.driver.quit()
        return

    '''
    # TODO: Pausa com tempo aleatória
    # Gera por um tempo aleatório entre dois valores
    # recebidos,
    '''

    def uniform_wait(self, first_timer: int, last_timer: int):
        sleep(uniform(uniform(first_timer, last_timer),
                      uniform(first_timer, last_timer)))

        return

    '''
    # TODO: Digitar pausadamente um texto
    # Recebe uma referência de um elemento de input,
    # um texto e digita pausadamente
    '''

    def dummy_send(self, found, word: str, first_timer: int, last_timer: int):
        for char in word:
            found.send_keys(char)
            self.uniform_wait(first_timer, last_timer)

        return

    '''
    # TODO: Apagar texto inserido em um elemento
    # Recebe uma referência de um elemento de input,
    # e apaga o texto que eventualmente existir
    '''

    def clear_field(self, element: str, etype: str, first_timer: int, last_timer: int):
        try:
            found = self.driver.find_element(
                by=self.find_options[etype], value=element)

        except Exception as error:
            print(f'Error Inside clear_field function: {error}')
            pass

        finally:
            found.clear()
            self.uniform_wait(first_timer, last_timer)

        return

    '''
    # TODO: Clicar em um elemento
    # Recebe uma referência de um elemento e clica
    '''

    def click(self, element: str, etype: str, first_timer: int, last_timer: int):
        try:
            found = self.driver.find_element(
                by=self.find_options[etype], value=element)
        except Exception as error:
            print(f'Error Inside click function: {error}')
            pass

        finally:
            found.click()
            self.uniform_wait(first_timer, last_timer)

        return

    '''
    # TODO: Clicar e inserir textos em inputs
    # Recebe uma referência de um elemento, um texto
    # e clica no elemento digitando o texto recebido
    # na sequência
    '''

    def click_and_type(self, element: str, text: str, etype: str, first_timer: int, last_timer: int):
        self.click(element, etype, first_timer, last_timer)
        try:
            found = self.driver.find_element(
                by=self.find_options[etype], value=element)

        except Exception as error:
            print(f'Error Inside click_and_type function: {error}')
            pass
        finally:
            self.dummy_send(found, text, first_timer, last_timer)
            self.uniform_wait(first_timer, last_timer)

        return

    '''
    # TODO: Obter a label de um elemento
    # Recebe as referências para determinado elemento
    # e retorna o texto 
    '''

    def get_element_text(self, element: str, etype: str, first_timer: int, last_timer: int) -> str:
        try:
            found = self.driver.find_element(
                by=self.find_options[etype], value=element)
        except Exception as error:
            print(f'Error Inside get_element_text function: {error}')
            pass

        finally:
            text = found.text
            self.uniform_wait(first_timer, last_timer)

        return text