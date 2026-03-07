from kivy.uix.screenmanager import Screen

from data_store import authenticate_account, set_current_user


class LoginScreen(Screen):
    def on_login(self):
        u = self.ids.username.text.strip()
        p = self.ids.password.text.strip()

        if not u and not p:
            self.ids.msg.text = "Please enter username and password."
            return

        if not u:
            self.ids.msg.text = "Please enter username."
            return

        if not p:
            self.ids.msg.text = "Please enter password."
            return

        if len(u) < 4:
            self.ids.msg.text = "Username must be at least 4 characters."
            return

        if len(p) < 6:
            self.ids.msg.text = "Password must be at least 6 characters."
            return

        if not authenticate_account(u, p):
            self.ids.msg.text = "Invalid username or password."
            return

        set_current_user(u)
        self.ids.msg.text = "Login success!"
        self.manager.current = "home"

    def go_register(self):
        self.ids.msg.text = ""
        self.manager.current = "register"

    def clear_fields(self):
        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.msg.text = ""