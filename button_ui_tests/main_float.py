import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyFloat(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    userinput = ObjectProperty(None)
    
    def btn(self):
        print("Name:", self.name.text, "email:", self.email.text)
        self.userinput.text = "User has entered - " + self.name.text + ", " + self.email.text
        self.name.text = ""
        self.email.text = ""
        

class MyFloatApp(App):
    def build(self):
        return MyFloat()

if __name__ == "__main__":
    MyFloatApp().run()