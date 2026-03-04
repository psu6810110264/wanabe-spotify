from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    def on_login(self):
        u = self.ids.username.text.strip()
        p = self.ids.password.text.strip()
        if not u or not p:
            self.ids.msg.text = "Please enter username and password."
            return
        self.ids.msg.text = ""
        self.manager.current = "home"

    def clear_fields(self):
        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.msg.text = "Cleared!"