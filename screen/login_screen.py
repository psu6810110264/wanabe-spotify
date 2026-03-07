from kivy.uix.screenmanager import Screen


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

        valid_username = "admin"
        valid_password = "123456"

        if u != valid_username or p != valid_password:
            self.ids.msg.text = "Invalid username or password."
            return

        self.ids.msg.text = "Login success!"
        self.manager.current = "home"

    def clear_fields(self):
        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.msg.text = ""