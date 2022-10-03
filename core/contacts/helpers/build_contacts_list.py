# -*- coding: utf-8 -*-
# encoding: utf-8

"""
    Get a dataframe with two columns
    (name and whatsapp number) to transform
    into a 'name - number' list
    
    :Args:
        - selected_file_dataframe_content - Pandas Dataframe
          with two columns (name and number) 
          
    :Returns:
        - List of transformed contact detail ['name - number']
"""


def build_contacts_list(selected_file_dataframe_content):

    # Copy of received datraframe
    table = selected_file_dataframe_content.copy()

    # Declaration of auxiliary lists
    names_and_numbers_list, contacts_list = [], []

    # Building list with two positions where
    # the first is a list of names and
    # the second is a list of numbers
    for index in range(0, len(table.columns)):
        contact = table[table.columns[index]]
        names_and_numbers_list.append(contact)

    # Building concat list, with a string:
    # 'name - number' of the contacts
    for index in range(0, len(table)):
        first_column = str(names_and_numbers_list[0][index])
        second_column = str(names_and_numbers_list[1][index])
        value = first_column + " - " + second_column
        contacts_list.append(value)

    return contacts_list
