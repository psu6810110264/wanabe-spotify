from kivy.uix.screenmanager import Screen

from data_store import register_account


class RegisterScreen(Screen):
    def on_create_account(self):
        u = self.ids.reg_username.text.strip()
        p = self.ids.reg_password.text.strip()
        c = self.ids.reg_confirm_password.text.strip()
        role = self.ids.reg_role.text.strip()

        if not u and not p:
            self.ids.reg_msg.text = "Please enter username and password."
            return

        if not u:
            self.ids.reg_msg.text = "Please enter username."
            return

        if not p:
            self.ids.reg_msg.text = "Please enter password."
            return

        if len(u) < 4:
            self.ids.reg_msg.text = "Username must be at least 4 characters."
            return

        if len(p) < 6:
            self.ids.reg_msg.text = "Password must be at least 6 characters."
            return

        if p != c:
            self.ids.reg_msg.text = "Password confirmation does not match."
            return

        if role == "Select account type":
            self.ids.reg_msg.text = "Please select account type."
            return

        success, message = register_account(u, p, role.lower())
        self.ids.reg_msg.text = message
        if success:
            self.ids.reg_password.text = ""
            self.ids.reg_confirm_password.text = ""
            self.ids.reg_role.text = "Select account type"

    def go_login(self):
        self.ids.reg_msg.text = ""
        self.manager.current = "login"

    def clear_fields(self):
        self.ids.reg_username.text = ""
        self.ids.reg_password.text = ""
        self.ids.reg_confirm_password.text = ""
        self.ids.reg_role.text = "Select account type"
        self.ids.reg_msg.text = ""
