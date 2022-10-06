# -*- coding: utf-8 -*-
# encoding: utf-8

from random import uniform
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager


class BotProcess:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args = args
        self.kwargs = kwargs

    """
    :Args:
        
    :Returns:
    """

    def config_bot(self):
        self.find_options = {
            "class": By.CLASS_NAME,
            "xpath": By.XPATH,
            "id": By.ID,
            "tag": By.TAG_NAME,
        }

        # Configuration
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-extensions")

        # Disable the banner "Chrome is being controlled by automated test software"
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Configurações do Navegador
        self.prefs = {
            "safebrowsing.enabled": False,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "profile.default_content_setting_values.automatic_downloads": 1,
        }

        self.options.add_experimental_option("prefs", self.prefs)
        self.capabilities = DesiredCapabilities().CHROME
        self.capabilities.update(self.options.to_capabilities())

        return

    """
    :Args:
        
    :Returns:
    """

    def start_driver(self):
        self.config_bot()
        try:
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=self.options,
                desired_capabilities=self.capabilities,
            )
        except WebDriverException:
            self.show_error(
                "Página fechada, logar novamente!", "icons/1x/errorAsset 55.png", "Ok"
            )
            return

    """   
    :Args:
        
    :Returns:
    """

    def quit_driver(self):
        self.driver.quit()
        return

    """
    :Args:
        
    :Returns:
    """

    @staticmethod
    def uniform_wait(first_timer: int, last_timer: int):
        sleep(
            uniform(uniform(first_timer, last_timer), uniform(first_timer, last_timer))
        )

        return

    """
    :Args:
        
    :Returns:
    """

    def check_if_exists(
        self, element: str, etype: str, first_timer: int, last_timer: int
    ) -> bool:

        try:
            self.driver.find_element(by=self.find_options[etype], value=element)
            contacts_exists = False
        except Exception:
            contacts_exists = True

        self.uniform_wait(2 * first_timer, 2 * last_timer)

        return contacts_exists

    """
    :Args:
        
    :Returns:
    """

    def normal_send(self, found, word: str, first_timer: int, last_timer: int):
        found.send_keys(word)
        self.uniform_wait(first_timer, last_timer)

        return

    """
    :Args:
        
    :Returns:
    """

    def dummy_send(self, found, word: str, first_timer: int, last_timer: int):
        for char in word:
            found.send_keys(char)
            self.uniform_wait(first_timer, last_timer)

        return

    """
    :Args:
        
    :Returns:
    """

    def clear_field(self, element: str, etype: str, first_timer: int, last_timer: int):
        try:
            found = self.driver.find_element(by=self.find_options[etype], value=element)
        except Exception as error:
            print(f"Error Inside clear_field function: {error}")
            pass

        finally:
            found.clear()
            self.uniform_wait(first_timer, last_timer)

        return

    """
    :Args:
        
    :Returns:
    """

    def click(self, element: str, etype: str, first_timer: int, last_timer: int):
        try:
            found = self.driver.find_element(by=self.find_options[etype], value=element)

        except Exception as error:
            print(f"Error Inside click function: {error}")
            pass

        finally:
            found.click()
            self.uniform_wait(first_timer, last_timer)

        return

    """
    :Args:
        
    :Returns:
    """

    def send_keys(
        self, element: str, text: str, etype: str, first_timer: int, last_timer: int
    ):
        try:
            found = self.driver.find_element(by=self.find_options[etype], value=element)
            self.uniform_wait(first_timer, last_timer)
        except Exception as error:
            print(f"Error Inside send_keys function: {error}")
            pass

        finally:
            self.normal_send(found, text, first_timer, last_timer)
            self.uniform_wait(first_timer, last_timer)

        return

    """
    :Args:
        
    :Returns:
    """

    def click_and_type(
        self, element: str, text: str, etype: str, first_timer: int, last_timer: int
    ):
        self.click(element, etype, first_timer, last_timer)
        try:
            found = self.driver.find_element(by=self.find_options[etype], value=element)

        except Exception as error:
            print(f"Error Inside click_and_type function: {error}")
            pass

        finally:
            self.dummy_send(found, text, first_timer, last_timer)
            self.uniform_wait(first_timer, last_timer)

        return

    """
    :Args:
        
    :Returns:
    """

    def get_element_text(
        self, element: str, element_type: str, first_timer: int, last_timer: int
    ) -> str:
        try:
            found = self.driver.find_element(
                by=self.find_options[element_type], value=element
            )
        except Exception as error:
            print(f"Error Inside get_element_text function: {error}")
            pass

        finally:
            text = found.text
            self.uniform_wait(first_timer, last_timer)

        return text
