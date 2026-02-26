from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):

    def on_login(self):
        print("Login button pressed")

    def clear_fields(self):
        self.ids.username.text = ""
        self.ids.password.text = ""
        print("Fields cleared")