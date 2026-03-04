from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    def on_login(self):
        self.manager.current = "home"

    def clear_fields(self):
        self.ids.username.text = ""
        self.ids.password.text = ""