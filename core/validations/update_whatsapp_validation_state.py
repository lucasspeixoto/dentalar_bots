# -*- coding: utf-8 -*-
# encoding: utf-8

"""
     Reset the validation state by disabling the send message
     button and enable the contact list, the image selection
     button and the message insertion field.
        
    :Args:
        
    :Returns:
"""


def reset_validate_whatsapp_needed_data(self):

    # Disable 'Send' button to trigger messages
    self.ui.send_whatsapp_messages_button.setEnabled(False)

    # Enable 'Image' button for image selection
    self.ui.load_image_button.setEnabled(True)

    # Enable input for message insertion
    self.ui.whatsapp_message_input.setEnabled(True)

    # Enable Contact List for Selection
    self.ui.contacts_list.setEnabled(True)
    
    # Enable Select or Unselect all contacts checkbox
    self.ui.send_to_all_contacts_checkbox.setEnabled(True)
    
    # Enable clean all contacts button
    self.ui.clear_contacts_list_button.setEnabled(True)

    return


"""
    Validate the data status by enabling the button for sending
    the messages and disabling the contact list, the image selection
    button, and the message insertion field.
        
    :Args:
        
    :Returns:
"""


def validate_whatsapp_needed_data(self):

    # Enabled 'Send' button to trigger messages
    self.ui.send_whatsapp_messages_button.setEnabled(True)

    # Disabled 'Image' button for image selection
    self.ui.load_image_button.setEnabled(False)

    # Disabled input for message insertion
    self.ui.whatsapp_message_input.setEnabled(False)

    # Disabled Contact List for Selection
    self.ui.contacts_list.setEnabled(False)
    
    # Disabled Select or Unselect all contacts checkbox
    self.ui.send_to_all_contacts_checkbox.setEnabled(False)
    
    # Disabled clean all contacts button
    self.ui.clear_contacts_list_button.setEnabled(False)

    return
