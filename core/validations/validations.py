# -*- coding: utf-8 -*-
# encoding: utf-8

from core.contacts.contacts import *
from core.validations.update_whatsapp_validation_state import (
    reset_validate_whatsapp_needed_data,
    validate_whatsapp_needed_data,
)

"""
Class with methods to check validations that need
interface updates as enabled and disable buttons.
"""


class Validations:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    """
    Reset the validated data state by disabling the submit button
    and enabling the contact list, image selection button and image
    insert input
        
    :Args:
        
    :Returns:
    """

    def reset_validate_whatsapp_needed_data(self):

        reset_validate_whatsapp_needed_data(self)

    """
    Check the data needed to trigger whatsapp messages.
    The validations will be regarding the existence of the paths.txt file,
    the insertion of a message, selection of at least 1 contact and selection
    of the image file. Once valid, the sending will be enabled, otherwise not
        
    :Args:
        
    :Returns:
    """

    def validate_whatsapp_needed_data(self):

        # Checking for the existence of a paths.txt file with
        # the xpaths for the submissions
        if any(self.files.whatsapp_paths) == False:
            self.errorexec(
                "O arquivo 'paths.txt' foi removido ou renomeado, inclua novamente para enviar as mensagens!",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            self.ui.validate_whatsapp_sending_button.setEnabled(False)
            return

        # List of contacts
        contacts: list = self.ui.contacts_list.selectedItems()

        # Whatsapp message
        message: str = self.ui.whatsapp_message_input.toPlainText()

        # Selected image machine path
        selected_image: str = self.files.selected_image

        # Check all errors
        has_error = len(contacts) == 0 or selected_image == "" or message == ""

        # If has any error, show the message and disabled send messages button,
        # enable, load imagem button, message input and contacts list
        if has_error == True:
            self.errorexec(
                "Para o envio é necessário selecionar um ou mais contatos, inserir a mensagem e selecionar a imagem.",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            reset_validate_whatsapp_needed_data(self)

        # If there isn't error, enable send messages button,
        # disable load imagem button, message input and contacts list
        else:
            validate_whatsapp_needed_data(self)

        return
