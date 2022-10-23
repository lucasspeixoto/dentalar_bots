# -*- coding: utf-8 -*-
# encoding: utf-8


class User:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    """

    :Args:

    :Returns:

    """

    def load_user_details(self):
        try:
            with open("user.txt") as file:
                try:
                    user = {
                        user_detail.split(":")[0]
                        .strip(): user_detail.split(":")[1]
                        .strip()
                        for user_detail in file.readlines()
                    }
                    try:
                        user_name = user["name"]
                        splited_name = user_name.split(" ")
                        if len(splited_name) >= 2:
                            user_name = "".join(
                                splited_name[0] + " " + splited_name[-1]
                            )

                        self.ui.user_name_label.setText(user_name)

                        self.ui.user_contact_name_input.setText(user["name"])
                        self.ui.user_contact_tel_input.setText(user["tel"])
                        self.ui.user_contact_org_input.setText(user["org"])
                        self.ui.user_contact_email_input.setText(user["email"])

                    except KeyError:
                        self.ui.user_name_label.setText("Usuário")

                except IndexError:
                    pass

        except FileNotFoundError:
            try:
                open("user.txt", "a").close()
            except OSError:
                print("Failed creating the user.txt file")
                pass

            self.ui.user_name_label.setText("Usuário")

        return

    """

    :Args:

    :Returns:

    """

    def edit_user(self):
        self.ui.user_contact_name_input.setEnabled(True)
        self.ui.user_contact_tel_input.setEnabled(True)
        self.ui.user_contact_org_input.setEnabled(True)
        self.ui.user_contact_email_input.setEnabled(True)

        self.ui.user_contact_save_button.setEnabled(True)
        self.ui.user_contact_edit_button.setEnabled(False)
        self.ui.user_contact_delete_button.setEnabled(False)

    """

    :Args:

    :Returns:

    """

    def save_user(self):
        new_user = {
            "name": self.ui.user_contact_name_input.text(),
            "tel": self.ui.user_contact_tel_input.text(),
            "org": self.ui.user_contact_org_input.text(),
            "email": self.ui.user_contact_email_input.text(),
        }

        try:
            with open("user.txt", "w") as file:
                for user_detail in new_user:
                    file.write(f"{user_detail}:{new_user[user_detail]}")
                    file.write("\n")

            try:
                user_name = new_user["name"]
                splited_name = user_name.split(" ")
                if len(splited_name) >= 2:
                    user_name = "".join(splited_name[0] + " " + splited_name[-1])

                self.ui.user_name_label.setText(user_name)

            except KeyError:
                self.ui.user_name_label.setText("Usuário")

        except FileNotFoundError:
            try:
                open("user.txt", "a").close()
            except OSError:
                print("Failed save new user in user.txt file")
                pass

        self.ui.user_contact_name_input.setEnabled(False)
        self.ui.user_contact_tel_input.setEnabled(False)
        self.ui.user_contact_org_input.setEnabled(False)
        self.ui.user_contact_email_input.setEnabled(False)

        self.ui.user_contact_save_button.setEnabled(False)
        self.ui.user_contact_edit_button.setEnabled(True)
        self.ui.user_contact_delete_button.setEnabled(True)

        return

    def delete_user(self):
        """ self.show_dialog(
            "Atenção!",
            "Este usuário será excluído, Deseja continuar ?",
            "assets/images/error.png",
            "Cancelar",
            "Sim",
        ) """

        try:
            file = open("user.txt","w")
            file.close()
        except FileNotFoundError:
            pass

        self.ui.user_name_label.setText("Usuário")
        
        self.ui.user_contact_name_input.setText("")
        self.ui.user_contact_tel_input.setText("")
        self.ui.user_contact_org_input.setText("")
        self.ui.user_contact_email_input.setText("")

        self.ui.user_contact_name_input.setEnabled(False)
        self.ui.user_contact_tel_input.setEnabled(False)
        self.ui.user_contact_org_input.setEnabled(False)
        self.ui.user_contact_email_input.setEnabled(False)

        self.ui.user_contact_save_button.setEnabled(False)
        self.ui.user_contact_edit_button.setEnabled(True)
        self.ui.user_contact_delete_button.setEnabled(True)
    
        return