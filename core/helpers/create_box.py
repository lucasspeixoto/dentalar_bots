def create_box(selected_file_dataframe_content):

    # Formatação Nomes
    file_ok = selected_file_dataframe_content.copy()

    listbox_inf, listbox_union = [], []
    for ind in range(0, len(file_ok.columns)):
        listbox_inf.append(file_ok[file_ok.columns[ind]])

    for ind in range(0, len(file_ok)):
        value = str(listbox_inf[0][ind]) + " - " + str(listbox_inf[1][ind])
        listbox_union.append(value)

    return listbox_union